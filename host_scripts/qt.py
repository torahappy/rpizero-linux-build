import sys
import struct
import subprocess
import datetime
from typing import Callable

from PyQt6.QtCore import QSize, QTimer, Qt, QEvent, QPoint
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from keymap import unshift_table, create_key_report

COEFF_MOVE = 1.0
WINDOW_SIZE = 500

Key = Qt.Key

from config import HOST_AND_USER

import atexit
import time

ssh_process = subprocess.Popen(["ssh", HOST_AND_USER, "sudo", "python", "allsync.py"], stdin=subprocess.PIPE, stdout=None, stderr=None)

def handler_exit():
    reset_payload()
    time.sleep(1)
    ssh_process.terminate()
    ssh_process.wait()

atexit.register(handler_exit)

type MouseCallbackArgs = tuple[tuple[int, int], tuple[int, int], set[int], int]
type KeyCallback = Callable[[set[int]], None] | None 
type MouseCallback = Callable[[MouseCallbackArgs], None] | None

class StateManager():
    def __init__(self):
        self.pressed_keys: set[int] = set()
        self.pressed_buttons: set[int] = set()
        # self.current_pos = None
        # self.current_pos_old = None
        self.center: tuple[int, int] | None = None

        self.key_callback: KeyCallback = None
        self.pos_callback: MouseCallback = None
        self.button_callback: MouseCallback = None
        self.wheel_callback: MouseCallback = None
    
    def reset_states(self):
        print('reset states...')
        self.pressed_buttons = set()
        self.pressed_keys = set()
        self.center = None
    
    def set_center(self, p: tuple[int, int] | None):
        self.center = p
    
    def change_pos(self, p: tuple[int, int]):
        if self.center != p and self.center is not None:
            # self.current_pos = p
            if self.pos_callback is not None:
                self.pos_callback((self.center, p, self.pressed_buttons, 0))
    
    def add_key_dry(self, k: int):
        if k in unshift_table:
            k = unshift_table[k]
        c = self.pressed_keys.copy()
        if not k in c:
            c.add(k)
        return c

    def remove_key_dry(self, k: int):
        if k in unshift_table:
            k = unshift_table[k]
        c = self.pressed_keys.copy()
        if k in c:
            c.remove(k)
        return c

    def add_key(self, k: int):
        if k in unshift_table:
            k = unshift_table[k]
        if not k in self.pressed_keys:
            self.pressed_keys.add(k)
            if self.key_callback is not None:
                self.key_callback(self.pressed_keys)
    
    def remove_key(self, k: int):
        if k in unshift_table:
            k = unshift_table[k]
        if k in self.pressed_keys:
            self.pressed_keys.remove(k)
            if self.key_callback is not None:
                self.key_callback(self.pressed_keys)

    def add_button(self, b: int):
        if not b in self.pressed_buttons and self.center is not None:
            self.pressed_buttons.add(b)
            if self.button_callback is not None:
                self.button_callback((self.center, self.center, self.pressed_buttons, 0))
    
    def remove_button(self, b: int):
        if b in self.pressed_buttons and self.center is not None:
            self.pressed_buttons.remove(b)
            if self.button_callback is not None:
                self.button_callback((self.center, self.center, self.pressed_buttons, 0))
    
    def do_wheel(self, val: int):
        if self.wheel_callback is not None and self.center is not None:
            self.wheel_callback((self.center, self.center, self.pressed_buttons, val))

    def set_pos_callback(self, cb: MouseCallback):
        self.pos_callback = cb

    def set_key_callback(self, cb: KeyCallback):
        self.key_callback = cb

    def set_button_callback(self, cb: MouseCallback):
        self.button_callback = cb

    def set_wheel_callback(self, cb: MouseCallback):
        self.wheel_callback = cb

sm = StateManager()

def send_payload(payload):
    ssh_process.stdin.write(payload) # type: ignore
    ssh_process.stdin.flush() # type: ignore

def reset_payload():
    print('sending reset payload...')
    send_payload(b'\x01' + b'\0' * 7)
    send_payload(b'\x02' + b'\0' * 8)

def mouse_func(x: MouseCallbackArgs):
    (oldpos, newpos, btns, wheel) = x

    if oldpos != None and newpos != None:
        dx, dy = newpos[0] - oldpos[0], newpos[1] - oldpos[1]
        intersection = btns & {1, 2, 4} # 1: left, 2: right, 4:middle
        payload = struct.pack('<Bhhh', sum(intersection), dx, dy, wheel)
        print('pos+btn', payload)
        send_payload(b'\x01' + payload)

def key_func(keys: set[int]):
    print(keys)
    payload = create_key_report(list(keys))
    # print([inv_qtkeys[k] for k in list(keys)])
    print('key', keys, payload)
    send_payload(b'\x02' + payload)

sm.set_pos_callback(mouse_func)

sm.set_key_callback(key_func)

sm.set_button_callback(mouse_func)

sm.set_wheel_callback(mouse_func)

def specialRound(num: float):
    if num >= 0:
        return int(num) + 1
    else:
        return int(num) - 1

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.SHORTCUT_GRAB = {Key.Key_G, Key.Key_Alt}
        self.SHORTCUT_RESET = {Key.Key_R, Key.Key_Alt}
        self.SHORTCUT_QUIT = {Key.Key_Q, Key.Key_Alt}
        self.SHORTCUTS = [self.SHORTCUT_GRAB, self.SHORTCUT_RESET, self.SHORTCUT_QUIT]

        self.grabEnabled = True
        self.mainwidth = WINDOW_SIZE

        self.frametimer = QTimer(self)
        self.frametimer.setInterval(10)
        self.frametimer.timeout.connect(self.frame_process)
        self.frametimer.start()

        self.setWindowTitle("My App")
        self.view = QGraphicsView()
        self.view.setFixedSize(QSize(self.mainwidth,self.mainwidth))
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.setCentralWidget(self.view)
        # self.setMouseTracking(True)
        self.setFixedSize(QSize(self.mainwidth,self.mainwidth))

        self.center_mouse_time = datetime.datetime.now()
        self.focus_out_reset_done = False

        self.setWindowOpacity(0.2)

    def enableGrab(self):
        self.grabEnabled = True

    def disableGrab(self):
        self.grabEnabled = False
        reset_payload()
        sm.reset_states()

    def frame_process(self):
        if self.isActiveWindow():
            self.focus_out_reset_done = False
        elif self.focus_out_reset_done == False:
            self.disableGrab()
            self.focus_out_reset_done = True
        
        if self.grabEnabled == True:
            self.center_mouse()
            self.setCursor(Qt.CursorShape.BlankCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)
    
    def handle_shortcuts(self, keys_dry):
        if keys_dry == self.SHORTCUT_GRAB:
            if self.grabEnabled:
                self.disableGrab()
            else:
                self.enableGrab()
        
        if keys_dry == self.SHORTCUT_RESET:
            reset_payload()
            sm.reset_states()

        if keys_dry == self.SHORTCUT_QUIT:
            app.exit()
    
    def center_mouse(self):
        new_time = datetime.datetime.now()
        if new_time - self.center_mouse_time < datetime.timedelta(milliseconds=20):
            QCursor.setPos(self.view.mapToGlobal(QPoint(self.mainwidth//2,self.mainwidth//2)))
        self.center_mouse_time = new_time
        sm.set_center((self.mainwidth//2,self.mainwidth//2))

    def eventFilter(self, source, event): # type: ignore
        if event.type() == QEvent.Type.MouseMove: # type: ignore
            sm.change_pos((int(event.pos().x() * COEFF_MOVE), int(event.pos().y() * COEFF_MOVE)))
            return True
        elif event.type() == QEvent.Type.KeyPress and not event.isAutoRepeat(): # type: ignore
            keys_dry = sm.add_key_dry(event.key())
            if not keys_dry in self.SHORTCUTS:
                sm.add_key(event.key())
            else:
                self.handle_shortcuts(keys_dry)
            return True
        elif event.type() == QEvent.Type.KeyRelease and not event.isAutoRepeat(): # type: ignore
            keys_dry = sm.remove_key_dry(event.key())
            if not keys_dry in self.SHORTCUTS:
                sm.remove_key(event.key())
            else:
                self.handle_shortcuts(keys_dry)
            return True
        elif event.type() == QEvent.Type.MouseButtonPress: # type: ignore
            print("press", event.button().value)
            sm.add_button(event.button().value)
            return True
        elif event.type() == QEvent.Type.MouseButtonRelease: # type: ignore
            print("remove", event.button().value)
            sm.remove_button(event.button().value)
            return True
        elif event.type() == QEvent.Type.Wheel: # type: ignore
            print("angleDelta", event.angleDelta())
            print("pixelDelta", event.pixelDelta())
            if event.pixelDelta().y() != 0:
                sm.do_wheel(specialRound(event.pixelDelta().y() / 120))
            return True
        return QMainWindow.eventFilter(self, source, event)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.installEventFilter(window)

app.exec()

