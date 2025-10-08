# Raspberry pi zero kernel build tool & other scripts

This is a script to build a custom raspberry pi kernel, including a kernel patch to fix dwc2 wakeup issue. I haven't tested, but probably works for Pi4 or Pi5.

A note for Pi5: in order for usb gadgets to work, it may be required to use Thunderbolt 4 or USB 4 cable specifically. You may also have to supply an additional 5V3A power supply through the GPIO pins after you connect a Thunderbolt or USB4 cable to your PC. Alternatively, you can also try using a USB 3.0 A-to-C cable and connect to the USB-A port on your PC, or if your PC doesn't have USB-A ports, combine a USB A-to-C cable and a A-to-C adapter.

Also, the directory `raspi_scripts` contains utilities to setup HID keyboard, RNDIS or ECM. Using a python library by @Danny-Dasilva (<https://github.com/Danny-Dasilva/Py_Keyboard>)

Patch reference: <https://github.com/pikvm/packages/blob/master/packages/linux-rpi-pikvm/1003-remote-wakeup.patch> <https://github.com/raspberrypi/linux/issues/3977> <http://www.dt8.jp/cgi-bin/adiary/adiary.cgi/0583>

1. Move to the project directory.
1. (if you are using selinux, run this script to allow write access from docker) `sudo sh selinux.sh`
1. `ln -s build.config.32_2709.sh build.config.sh` (change `build.config.32_2709.sh` according to the CPU and architecture. See <https://www.raspberrypi.com/documentation/computers/linux_kernel.html#cross-compiled-build-configuration> for instructions.)
1. `sh download.sh`
1. `sh docker.sh`
1. (inside docker) `cd /rpizero-linux-build`
1. (inside docker) `sh clean.sh`
1. (inside docker) `sh build.sh`
1. (inside docker) `exit`
1. Create a file named `names.sh` and set the contents as follows.
   ```
   MYHOSTNAME=<hostname of rpi zero including .local, or the ip address of it>
   MYUSERNAME=<username of rpi zero>
   MY_KERNEL_SUFFIX=wakeup
   MY_KERNEL_NAME=kernel-$MY_KERNEL_SUFFIX
   ```
1. `sh pack.sh`
1. `sh packsend.sh` make sure you have SSH access to the rpi zero and it is connected to the local network.  Alternatively, you can just copy generated files at `install/` to the SD card. First, copy `boot/firmware` into `/` of the EFI partition (usually the first partition). Second, copy `lib/modules` into `lib/modules` of the root partition (usually the second partition). Beware of file ownership. All files should be owned by `root`.
1. ssh into the rpizero and edit `/boot/firmware/config.txt`. Add following lines to the boot configuration. Alternatively, you can edit the SD. The file is at `/config.txt` in the EFI partition. If anything wrong happens (eg. the system doesn't start), please edit SD directly and delete these lines to revert all changes made to the system.
   ```
   [all]
   dtoverlay=dwc2
   kernel=kernel-wakeup.img
   ```
1. ssh into the rpizero and reboot

## scripts and configs for rpi zero

- `raspi_scripts/`: scripts to be run inside raspberry pi
   - `etc/rc.local`: rc file to enable HID mouse and keyboard on startup
   - `home/someusername`: scripts to control USB device
      - `keyboard2.py`: control HID keyboard via command line  
         Example1 : `p CONTROL ALT DEL`  
         Example2 : `p ALT F4`  
         Example3 : `p DOWN_ARROW`  
         Example4 : `w sometext12345`
   - `root/`: scripts to enable HID/Ether feature on startup
      - `geth.sh`: Enable an old driver for ethernet over USB using RNDIS. On windows, you have to install a special driver to connect to the rpi zero. Go to <https://www.catalog.update.microsoft.com/Search.aspx?q=USB%20RNDIS%20Gadget>, and download the driver file named "Acer Incorporated. - Other hardware - USB Ethernet/RNDIS Gadget". On linux, it works without any configration.
      - `hid-and-eth.sh`: enable both HID and Ethernet-over-USB at the same time using a new driver. Unfortunately, there is no signed Windows driver for it.
      - `hid-double.sh`: enable both HID keyboard and Mouse.
      - `hid.sh`: enable only HID keyboard.
      - `remove.sh`: unloads all drivers so that you can use any of these scripts again. very unstable, so it is better to restart the rpi zero instead.

- `host_scripts/`: scripts to be run from the remote computer that will control raspberry pi
  - `qt.py`: Use PyQt5 to synchronize keyboard input and mouse movement  
    USAGE: Alt+G to toggle mouse grabbing. After switching mouse grabbing on, just type text or moving mouse. Note that on MacOS, CTRL is interpreted as COMMAND/WINDOWS key, and COMMAND/WINDOWS is interpreted as CTRL key. The window is transparent, so you can use this application as a overlay, working together with remote desktop app such as RustDesk.
  - `mouse.py`: Use Xlib to synchronize mouse movement
