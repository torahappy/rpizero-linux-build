from PyQt6.QtCore import Qt
import struct

K = Qt.Key


qtkeys = {
        "Key_Escape": K.Key_Escape,
        "Key_Tab": K.Key_Tab,
        "Key_Backtab": K.Key_Backtab,
        "Key_Backspace": K.Key_Backspace,
        "Key_Return": K.Key_Return,
        "Key_Enter": K.Key_Enter,
        "Key_Insert": K.Key_Insert,
        "Key_Delete": K.Key_Delete,
        "Key_Pause": K.Key_Pause,
        "Key_Print": K.Key_Print,
        "Key_SysReq": K.Key_SysReq,
        "Key_Clear": K.Key_Clear,
        "Key_Home": K.Key_Home,
        "Key_End": K.Key_End,
        "Key_Left": K.Key_Left,
        "Key_Up": K.Key_Up,
        "Key_Right": K.Key_Right,
        "Key_Down": K.Key_Down,
        "Key_PageUp": K.Key_PageUp,
        "Key_PageDown": K.Key_PageDown,
        "Key_Shift": K.Key_Shift,
        "Key_Control": K.Key_Control,
        "Key_Meta": K.Key_Meta,
        "Key_Alt": K.Key_Alt,
        "Key_CapsLock": K.Key_CapsLock,
        "Key_NumLock": K.Key_NumLock,
        "Key_ScrollLock": K.Key_ScrollLock,
        "Key_F1": K.Key_F1,
        "Key_F2": K.Key_F2,
        "Key_F3": K.Key_F3,
        "Key_F4": K.Key_F4,
        "Key_F5": K.Key_F5,
        "Key_F6": K.Key_F6,
        "Key_F7": K.Key_F7,
        "Key_F8": K.Key_F8,
        "Key_F9": K.Key_F9,
        "Key_F10": K.Key_F10,
        "Key_F11": K.Key_F11,
        "Key_F12": K.Key_F12,
        "Key_F13": K.Key_F13,
        "Key_F14": K.Key_F14,
        "Key_F15": K.Key_F15,
        "Key_F16": K.Key_F16,
        "Key_F17": K.Key_F17,
        "Key_F18": K.Key_F18,
        "Key_F19": K.Key_F19,
        "Key_F20": K.Key_F20,
        "Key_F21": K.Key_F21,
        "Key_F22": K.Key_F22,
        "Key_F23": K.Key_F23,
        "Key_F24": K.Key_F24,
        "Key_F25": K.Key_F25,
        "Key_F26": K.Key_F26,
        "Key_F27": K.Key_F27,
        "Key_F28": K.Key_F28,
        "Key_F29": K.Key_F29,
        "Key_F30": K.Key_F30,
        "Key_F31": K.Key_F31,
        "Key_F32": K.Key_F32,
        "Key_F33": K.Key_F33,
        "Key_F34": K.Key_F34,
        "Key_F35": K.Key_F35,
        "Key_Super_L": K.Key_Super_L,
        "Key_Super_R": K.Key_Super_R,
        "Key_Menu": K.Key_Menu,
        "Key_Hyper_L": K.Key_Hyper_L,
        "Key_Hyper_R": K.Key_Hyper_R,
        "Key_Help": K.Key_Help,
        "Key_Direction_L": K.Key_Direction_L,
        "Key_Direction_R": K.Key_Direction_R,
        "Key_Space": K.Key_Space,
        "Key_Any": K.Key_Any,
        "Key_Exclam": K.Key_Exclam,
        "Key_QuoteDbl": K.Key_QuoteDbl,
        "Key_NumberSign": K.Key_NumberSign,
        "Key_Dollar": K.Key_Dollar,
        "Key_Percent": K.Key_Percent,
        "Key_Ampersand": K.Key_Ampersand,
        "Key_Apostrophe": K.Key_Apostrophe,
        "Key_ParenLeft": K.Key_ParenLeft,
        "Key_ParenRight": K.Key_ParenRight,
        "Key_Asterisk": K.Key_Asterisk,
        "Key_Plus": K.Key_Plus,
        "Key_Comma": K.Key_Comma,
        "Key_Minus": K.Key_Minus,
        "Key_Period": K.Key_Period,
        "Key_Slash": K.Key_Slash,
        "Key_0": K.Key_0,
        "Key_1": K.Key_1,
        "Key_2": K.Key_2,
        "Key_3": K.Key_3,
        "Key_4": K.Key_4,
        "Key_5": K.Key_5,
        "Key_6": K.Key_6,
        "Key_7": K.Key_7,
        "Key_8": K.Key_8,
        "Key_9": K.Key_9,
        "Key_Colon": K.Key_Colon,
        "Key_Semicolon": K.Key_Semicolon,
        "Key_Less": K.Key_Less,
        "Key_Equal": K.Key_Equal,
        "Key_Greater": K.Key_Greater,
        "Key_Question": K.Key_Question,
        "Key_At": K.Key_At,
        "Key_A": K.Key_A,
        "Key_B": K.Key_B,
        "Key_C": K.Key_C,
        "Key_D": K.Key_D,
        "Key_E": K.Key_E,
        "Key_F": K.Key_F,
        "Key_G": K.Key_G,
        "Key_H": K.Key_H,
        "Key_I": K.Key_I,
        "Key_J": K.Key_J,
        "Key_K": K.Key_K,
        "Key_L": K.Key_L,
        "Key_M": K.Key_M,
        "Key_N": K.Key_N,
        "Key_O": K.Key_O,
        "Key_P": K.Key_P,
        "Key_Q": K.Key_Q,
        "Key_R": K.Key_R,
        "Key_S": K.Key_S,
        "Key_T": K.Key_T,
        "Key_U": K.Key_U,
        "Key_V": K.Key_V,
        "Key_W": K.Key_W,
        "Key_X": K.Key_X,
        "Key_Y": K.Key_Y,
        "Key_Z": K.Key_Z,
        "Key_BracketLeft": K.Key_BracketLeft,
        "Key_Backslash": K.Key_Backslash,
        "Key_BracketRight": K.Key_BracketRight,
        "Key_AsciiCircum": K.Key_AsciiCircum,
        "Key_Underscore": K.Key_Underscore,
        "Key_QuoteLeft": K.Key_QuoteLeft,
        "Key_BraceLeft": K.Key_BraceLeft,
        "Key_Bar": K.Key_Bar,
        "Key_BraceRight": K.Key_BraceRight,
        "Key_AsciiTilde": K.Key_AsciiTilde,
        "Key_nobreakspace": K.Key_nobreakspace,
        "Key_exclamdown": K.Key_exclamdown,
        "Key_cent": K.Key_cent,
        "Key_sterling": K.Key_sterling,
        "Key_currency": K.Key_currency,
        "Key_yen": K.Key_yen,
        "Key_brokenbar": K.Key_brokenbar,
        "Key_section": K.Key_section,
        "Key_diaeresis": K.Key_diaeresis,
        "Key_copyright": K.Key_copyright,
        "Key_ordfeminine": K.Key_ordfeminine,
        "Key_guillemotleft": K.Key_guillemotleft,
        "Key_notsign": K.Key_notsign,
        "Key_hyphen": K.Key_hyphen,
        "Key_registered": K.Key_registered,
        "Key_macron": K.Key_macron,
        "Key_degree": K.Key_degree,
        "Key_plusminus": K.Key_plusminus,
        "Key_twosuperior": K.Key_twosuperior,
        "Key_threesuperior": K.Key_threesuperior,
        "Key_acute": K.Key_acute,
        "Key_mu": K.Key_mu,
        "Key_paragraph": K.Key_paragraph,
        "Key_periodcentered": K.Key_periodcentered,
        "Key_cedilla": K.Key_cedilla,
        "Key_onesuperior": K.Key_onesuperior,
        "Key_masculine": K.Key_masculine,
        "Key_guillemotright": K.Key_guillemotright,
        "Key_onequarter": K.Key_onequarter,
        "Key_onehalf": K.Key_onehalf,
        "Key_threequarters": K.Key_threequarters,
        "Key_questiondown": K.Key_questiondown,
        "Key_Agrave": K.Key_Agrave,
        "Key_Aacute": K.Key_Aacute,
        "Key_Acircumflex": K.Key_Acircumflex,
        "Key_Atilde": K.Key_Atilde,
        "Key_Adiaeresis": K.Key_Adiaeresis,
        "Key_Aring": K.Key_Aring,
        "Key_AE": K.Key_AE,
        "Key_Ccedilla": K.Key_Ccedilla,
        "Key_Egrave": K.Key_Egrave,
        "Key_Eacute": K.Key_Eacute,
        "Key_Ecircumflex": K.Key_Ecircumflex,
        "Key_Ediaeresis": K.Key_Ediaeresis,
        "Key_Igrave": K.Key_Igrave,
        "Key_Iacute": K.Key_Iacute,
        "Key_Icircumflex": K.Key_Icircumflex,
        "Key_Idiaeresis": K.Key_Idiaeresis,
        "Key_ETH": K.Key_ETH,
        "Key_Ntilde": K.Key_Ntilde,
        "Key_Ograve": K.Key_Ograve,
        "Key_Oacute": K.Key_Oacute,
        "Key_Ocircumflex": K.Key_Ocircumflex,
        "Key_Otilde": K.Key_Otilde,
        "Key_Odiaeresis": K.Key_Odiaeresis,
        "Key_multiply": K.Key_multiply,
        "Key_Ooblique": K.Key_Ooblique,
        "Key_Ugrave": K.Key_Ugrave,
        "Key_Uacute": K.Key_Uacute,
        "Key_Ucircumflex": K.Key_Ucircumflex,
        "Key_Udiaeresis": K.Key_Udiaeresis,
        "Key_Yacute": K.Key_Yacute,
        "Key_THORN": K.Key_THORN,
        "Key_ssharp": K.Key_ssharp,
        "Key_division": K.Key_division,
        "Key_ydiaeresis": K.Key_ydiaeresis,
        "Key_AltGr": K.Key_AltGr,
        "Key_Multi_key": K.Key_Multi_key,
        "Key_Codeinput": K.Key_Codeinput,
        "Key_SingleCandidate": K.Key_SingleCandidate,
        "Key_MultipleCandidate": K.Key_MultipleCandidate,
        "Key_PreviousCandidate": K.Key_PreviousCandidate,
        "Key_Mode_switch": K.Key_Mode_switch,
        "Key_Kanji": K.Key_Kanji,
        "Key_Muhenkan": K.Key_Muhenkan,
        "Key_Henkan": K.Key_Henkan,
        "Key_Romaji": K.Key_Romaji,
        "Key_Hiragana": K.Key_Hiragana,
        "Key_Katakana": K.Key_Katakana,
        "Key_Hiragana_Katakana": K.Key_Hiragana_Katakana,
        "Key_Zenkaku": K.Key_Zenkaku,
        "Key_Hankaku": K.Key_Hankaku,
        "Key_Zenkaku_Hankaku": K.Key_Zenkaku_Hankaku,
        "Key_Touroku": K.Key_Touroku,
        "Key_Massyo": K.Key_Massyo,
        "Key_Kana_Lock": K.Key_Kana_Lock,
        "Key_Kana_Shift": K.Key_Kana_Shift,
        "Key_Eisu_Shift": K.Key_Eisu_Shift,
        "Key_Eisu_toggle": K.Key_Eisu_toggle,
        "Key_Hangul": K.Key_Hangul,
        "Key_Hangul_Start": K.Key_Hangul_Start,
        "Key_Hangul_End": K.Key_Hangul_End,
        "Key_Hangul_Hanja": K.Key_Hangul_Hanja,
        "Key_Hangul_Jamo": K.Key_Hangul_Jamo,
        "Key_Hangul_Romaja": K.Key_Hangul_Romaja,
        "Key_Hangul_Jeonja": K.Key_Hangul_Jeonja,
        "Key_Hangul_Banja": K.Key_Hangul_Banja,
        "Key_Hangul_PreHanja": K.Key_Hangul_PreHanja,
        "Key_Hangul_PostHanja": K.Key_Hangul_PostHanja,
        "Key_Hangul_Special": K.Key_Hangul_Special,
        "Key_Dead_Grave": K.Key_Dead_Grave,
        "Key_Dead_Acute": K.Key_Dead_Acute,
        "Key_Dead_Circumflex": K.Key_Dead_Circumflex,
        "Key_Dead_Tilde": K.Key_Dead_Tilde,
        "Key_Dead_Macron": K.Key_Dead_Macron,
        "Key_Dead_Breve": K.Key_Dead_Breve,
        "Key_Dead_Abovedot": K.Key_Dead_Abovedot,
        "Key_Dead_Diaeresis": K.Key_Dead_Diaeresis,
        "Key_Dead_Abovering": K.Key_Dead_Abovering,
        "Key_Dead_Doubleacute": K.Key_Dead_Doubleacute,
        "Key_Dead_Caron": K.Key_Dead_Caron,
        "Key_Dead_Cedilla": K.Key_Dead_Cedilla,
        "Key_Dead_Ogonek": K.Key_Dead_Ogonek,
        "Key_Dead_Iota": K.Key_Dead_Iota,
        "Key_Dead_Voiced_Sound": K.Key_Dead_Voiced_Sound,
        "Key_Dead_Semivoiced_Sound": K.Key_Dead_Semivoiced_Sound,
        "Key_Dead_Belowdot": K.Key_Dead_Belowdot,
        "Key_Dead_Hook": K.Key_Dead_Hook,
        "Key_Dead_Horn": K.Key_Dead_Horn,
        "Key_Back": K.Key_Back,
        "Key_Forward": K.Key_Forward,
        "Key_Stop": K.Key_Stop,
        "Key_Refresh": K.Key_Refresh,
        "Key_VolumeDown": K.Key_VolumeDown,
        "Key_VolumeMute": K.Key_VolumeMute,
        "Key_VolumeUp": K.Key_VolumeUp,
        "Key_BassBoost": K.Key_BassBoost,
        "Key_BassUp": K.Key_BassUp,
        "Key_BassDown": K.Key_BassDown,
        "Key_TrebleUp": K.Key_TrebleUp,
        "Key_TrebleDown": K.Key_TrebleDown,
        "Key_MediaPlay": K.Key_MediaPlay,
        "Key_MediaStop": K.Key_MediaStop,
        "Key_MediaPrevious": K.Key_MediaPrevious,
        "Key_MediaNext": K.Key_MediaNext,
        "Key_MediaRecord": K.Key_MediaRecord,
        "Key_HomePage": K.Key_HomePage,
        "Key_Favorites": K.Key_Favorites,
        "Key_Search": K.Key_Search,
        "Key_Standby": K.Key_Standby,
        "Key_OpenUrl": K.Key_OpenUrl,
        "Key_LaunchMail": K.Key_LaunchMail,
        "Key_LaunchMedia": K.Key_LaunchMedia,
        "Key_Launch0": K.Key_Launch0,
        "Key_Launch1": K.Key_Launch1,
        "Key_Launch2": K.Key_Launch2,
        "Key_Launch3": K.Key_Launch3,
        "Key_Launch4": K.Key_Launch4,
        "Key_Launch5": K.Key_Launch5,
        "Key_Launch6": K.Key_Launch6,
        "Key_Launch7": K.Key_Launch7,
        "Key_Launch8": K.Key_Launch8,
        "Key_Launch9": K.Key_Launch9,
        "Key_LaunchA": K.Key_LaunchA,
        "Key_LaunchB": K.Key_LaunchB,
        "Key_LaunchC": K.Key_LaunchC,
        "Key_LaunchD": K.Key_LaunchD,
        "Key_LaunchE": K.Key_LaunchE,
        "Key_LaunchF": K.Key_LaunchF,
        "Key_MediaLast": K.Key_MediaLast,
        "Key_Select": K.Key_Select,
        "Key_Yes": K.Key_Yes,
        "Key_No": K.Key_No,
        "Key_Context1": K.Key_Context1,
        "Key_Context2": K.Key_Context2,
        "Key_Context3": K.Key_Context3,
        "Key_Context4": K.Key_Context4,
        "Key_Call": K.Key_Call,
        "Key_Hangup": K.Key_Hangup,
        "Key_Flip": K.Key_Flip,
        "Key_unknown": K.Key_unknown,
        "Key_Execute": K.Key_Execute,
        "Key_Printer": K.Key_Printer,
        "Key_Play": K.Key_Play,
        "Key_Sleep": K.Key_Sleep,
        "Key_Zoom": K.Key_Zoom,
        "Key_Cancel": K.Key_Cancel,
        "Key_MonBrightnessUp": K.Key_MonBrightnessUp,
        "Key_MonBrightnessDown": K.Key_MonBrightnessDown,
        "Key_KeyboardLightOnOff": K.Key_KeyboardLightOnOff,
        "Key_KeyboardBrightnessUp": K.Key_KeyboardBrightnessUp,
        "Key_KeyboardBrightnessDown": K.Key_KeyboardBrightnessDown,
        "Key_PowerOff": K.Key_PowerOff,
        "Key_WakeUp": K.Key_WakeUp,
        "Key_Eject": K.Key_Eject,
        "Key_ScreenSaver": K.Key_ScreenSaver,
        "Key_WWW": K.Key_WWW,
        "Key_Memo": K.Key_Memo,
        "Key_LightBulb": K.Key_LightBulb,
        "Key_Shop": K.Key_Shop,
        "Key_History": K.Key_History,
        "Key_AddFavorite": K.Key_AddFavorite,
        "Key_HotLinks": K.Key_HotLinks,
        "Key_BrightnessAdjust": K.Key_BrightnessAdjust,
        "Key_Finance": K.Key_Finance,
        "Key_Community": K.Key_Community,
        "Key_AudioRewind": K.Key_AudioRewind,
        "Key_BackForward": K.Key_BackForward,
        "Key_ApplicationLeft": K.Key_ApplicationLeft,
        "Key_ApplicationRight": K.Key_ApplicationRight,
        "Key_Book": K.Key_Book,
        "Key_CD": K.Key_CD,
        "Key_Calculator": K.Key_Calculator,
        "Key_ToDoList": K.Key_ToDoList,
        "Key_ClearGrab": K.Key_ClearGrab,
        "Key_Close": K.Key_Close,
        "Key_Copy": K.Key_Copy,
        "Key_Cut": K.Key_Cut,
        "Key_Display": K.Key_Display,
        "Key_DOS": K.Key_DOS,
        "Key_Documents": K.Key_Documents,
        "Key_Excel": K.Key_Excel,
        "Key_Explorer": K.Key_Explorer,
        "Key_Game": K.Key_Game,
        "Key_Go": K.Key_Go,
        "Key_iTouch": K.Key_iTouch,
        "Key_LogOff": K.Key_LogOff,
        "Key_Market": K.Key_Market,
        "Key_Meeting": K.Key_Meeting,
        "Key_MenuKB": K.Key_MenuKB,
        "Key_MenuPB": K.Key_MenuPB,
        "Key_MySites": K.Key_MySites,
        "Key_News": K.Key_News,
        "Key_OfficeHome": K.Key_OfficeHome,
        "Key_Option": K.Key_Option,
        "Key_Paste": K.Key_Paste,
        "Key_Phone": K.Key_Phone,
        "Key_Calendar": K.Key_Calendar,
        "Key_Reply": K.Key_Reply,
        "Key_Reload": K.Key_Reload,
        "Key_RotateWindows": K.Key_RotateWindows,
        "Key_RotationPB": K.Key_RotationPB,
        "Key_RotationKB": K.Key_RotationKB,
        "Key_Save": K.Key_Save,
        "Key_Send": K.Key_Send,
        "Key_Spell": K.Key_Spell,
        "Key_SplitScreen": K.Key_SplitScreen,
        "Key_Support": K.Key_Support,
        "Key_TaskPane": K.Key_TaskPane,
        "Key_Terminal": K.Key_Terminal,
        "Key_Tools": K.Key_Tools,
        "Key_Travel": K.Key_Travel,
        "Key_Video": K.Key_Video,
        "Key_Word": K.Key_Word,
        "Key_Xfer": K.Key_Xfer,
        "Key_ZoomIn": K.Key_ZoomIn,
        "Key_ZoomOut": K.Key_ZoomOut,
        "Key_Away": K.Key_Away,
        "Key_Messenger": K.Key_Messenger,
        "Key_WebCam": K.Key_WebCam,
        "Key_MailForward": K.Key_MailForward,
        "Key_Pictures": K.Key_Pictures,
        "Key_Music": K.Key_Music,
        "Key_Battery": K.Key_Battery,
        "Key_Bluetooth": K.Key_Bluetooth,
        "Key_WLAN": K.Key_WLAN,
        "Key_UWB": K.Key_UWB,
        "Key_AudioForward": K.Key_AudioForward,
        "Key_AudioRepeat": K.Key_AudioRepeat,
        "Key_AudioRandomPlay": K.Key_AudioRandomPlay,
        "Key_Subtitle": K.Key_Subtitle,
        "Key_AudioCycleTrack": K.Key_AudioCycleTrack,
        "Key_Time": K.Key_Time,
        "Key_Hibernate": K.Key_Hibernate,
        "Key_View": K.Key_View,
        "Key_TopMenu": K.Key_TopMenu,
        "Key_PowerDown": K.Key_PowerDown,
        "Key_Suspend": K.Key_Suspend,
        "Key_ContrastAdjust": K.Key_ContrastAdjust,
        "Key_MediaPause": K.Key_MediaPause,
        "Key_MediaTogglePlayPause": K.Key_MediaTogglePlayPause,
        "Key_LaunchG": K.Key_LaunchG,
        "Key_LaunchH": K.Key_LaunchH,
        "Key_ToggleCallHangup": K.Key_ToggleCallHangup,
        "Key_VoiceDial": K.Key_VoiceDial,
        "Key_LastNumberRedial": K.Key_LastNumberRedial,
        "Key_Camera": K.Key_Camera,
        "Key_CameraFocus": K.Key_CameraFocus,
        "Key_TouchpadToggle": K.Key_TouchpadToggle,
        "Key_TouchpadOn": K.Key_TouchpadOn,
        "Key_TouchpadOff": K.Key_TouchpadOff,
        "Key_MicMute": K.Key_MicMute,
        "Key_Red": K.Key_Red,
        "Key_Green": K.Key_Green,
        "Key_Yellow": K.Key_Yellow,
        "Key_Blue": K.Key_Blue,
        "Key_ChannelUp": K.Key_ChannelUp,
        "Key_ChannelDown": K.Key_ChannelDown,
        "Key_Guide": K.Key_Guide,
        "Key_Info": K.Key_Info,
        "Key_Settings": K.Key_Settings,
        "Key_Exit": K.Key_Exit,
        "Key_MicVolumeUp": K.Key_MicVolumeUp,
        "Key_MicVolumeDown": K.Key_MicVolumeDown,
        "Key_New": K.Key_New,
        "Key_Open": K.Key_Open,
        "Key_Find": K.Key_Find,
        "Key_Undo": K.Key_Undo,
        "Key_Redo": K.Key_Redo,
        "Key_Dead_Stroke": K.Key_Dead_Stroke,
        "Key_Dead_Abovecomma": K.Key_Dead_Abovecomma,
        "Key_Dead_Abovereversedcomma": K.Key_Dead_Abovereversedcomma,
        "Key_Dead_Doublegrave": K.Key_Dead_Doublegrave,
        "Key_Dead_Belowring": K.Key_Dead_Belowring,
        "Key_Dead_Belowmacron": K.Key_Dead_Belowmacron,
        "Key_Dead_Belowcircumflex": K.Key_Dead_Belowcircumflex,
        "Key_Dead_Belowtilde": K.Key_Dead_Belowtilde,
        "Key_Dead_Belowbreve": K.Key_Dead_Belowbreve,
        "Key_Dead_Belowdiaeresis": K.Key_Dead_Belowdiaeresis,
        "Key_Dead_Invertedbreve": K.Key_Dead_Invertedbreve,
        "Key_Dead_Belowcomma": K.Key_Dead_Belowcomma,
        "Key_Dead_Currency": K.Key_Dead_Currency,
        "Key_Dead_a": K.Key_Dead_a,
        "Key_Dead_A": K.Key_Dead_A,
        "Key_Dead_e": K.Key_Dead_e,
        "Key_Dead_E": K.Key_Dead_E,
        "Key_Dead_i": K.Key_Dead_i,
        "Key_Dead_I": K.Key_Dead_I,
        "Key_Dead_o": K.Key_Dead_o,
        "Key_Dead_O": K.Key_Dead_O,
        "Key_Dead_u": K.Key_Dead_u,
        "Key_Dead_U": K.Key_Dead_U,
        "Key_Dead_Small_Schwa": K.Key_Dead_Small_Schwa,
        "Key_Dead_Capital_Schwa": K.Key_Dead_Capital_Schwa,
        "Key_Dead_Greek": K.Key_Dead_Greek,
        "Key_Dead_Lowline": K.Key_Dead_Lowline,
        "Key_Dead_Aboveverticalline": K.Key_Dead_Aboveverticalline,
        "Key_Dead_Belowverticalline": K.Key_Dead_Belowverticalline,
        "Key_Dead_Longsolidusoverlay": K.Key_Dead_Longsolidusoverlay,
}

inv_qtkeys = {v: [p1 for p1, p2 in qtkeys.items() if p2 == v] for v in qtkeys.values()}

shift_table = {
    K.Key_1 : K.Key_Exclam, # ``1`` and ``!``
    K.Key_2 : K.Key_At, # ``2`` and ``@``
    K.Key_3 : K.Key_NumberSign, # ``3`` and ``#``
    K.Key_4 : K.Key_Dollar, # ``4`` and ``$``
    K.Key_5 : K.Key_Percent, # ``5`` and ``%``
    K.Key_6 : K.Key_AsciiCircum, # ``6`` and ``^``
    K.Key_7 : K.Key_Ampersand, # ``7`` and ``&``
    K.Key_8 : K.Key_Asterisk, # ``8`` and ``*``
    K.Key_9 : K.Key_ParenLeft, # ``9`` and ``(``
    K.Key_0 : K.Key_ParenRight, # ``0`` and ``)``
    K.Key_Minus : K.Key_Underscore, # ``-` and ``_``
    K.Key_Equal : K.Key_Plus, # ``:` and ``+``
    K.Key_BracketLeft : K.Key_BraceLeft, # ``[`` and ``{``
    K.Key_BracketRight : K.Key_BraceRight, # ``]`` and ``}``
    K.Key_Backslash : K.Key_Bar, # ``\`` and ``|``
#    POUND : 0x32, # ``#`` and ``~`` (Non-US keyboard)
    K.Key_Semicolon : K.Key_Colon, # ``;`` and ``:``
    K.Key_Apostrophe : K.Key_QuoteDbl, # ``'`` and ``"``
    K.Key_QuoteLeft : K.Key_AsciiTilde, # :literal:`\`` and ``~``
    K.Key_Comma : K.Key_Less, # ``,`` and ``<``
    K.Key_Period : K.Key_Greater, # ``.`` and ``>``
    K.Key_Slash : K.Key_Question, # ``/`` and ``?``
}

unshift_table = {v: k for k, v in shift_table.items()}

keymap = {
    K.Key_A : 0x04, # ``a`` and ``A``
    K.Key_B : 0x05, # ``b`` and ``B``
    K.Key_C : 0x06, # ``c`` and ``C``
    K.Key_D : 0x07, # ``d`` and ``D``
    K.Key_E : 0x08, # ``e`` and ``E``
    K.Key_F : 0x09, # ``f`` and ``F``
    K.Key_G : 0x0A, # ``g`` and ``G``
    K.Key_H : 0x0B, # ``h`` and ``H``
    K.Key_I : 0x0C, # ``i`` and ``I``
    K.Key_J : 0x0D, # ``j`` and ``J``
    K.Key_K : 0x0E, # ``k`` and ``K``
    K.Key_L : 0x0F, # ``l`` and ``L``
    K.Key_M : 0x10, # ``m`` and ``M``
    K.Key_N : 0x11, # ``n`` and ``N``
    K.Key_O : 0x12, # ``o`` and ``O``
    K.Key_P : 0x13, # ``p`` and ``P``
    K.Key_Q : 0x14, # ``q`` and ``Q``
    K.Key_R : 0x15, # ``r`` and ``R``
    K.Key_S : 0x16, # ``s`` and ``S``
    K.Key_T : 0x17, # ``t`` and ``T``
    K.Key_U : 0x18, # ``u`` and ``U``
    K.Key_V : 0x19, # ``v`` and ``V``
    K.Key_W : 0x1A, # ``w`` and ``W``
    K.Key_X : 0x1B, # ``x`` and ``X``
    K.Key_Y : 0x1C, # ``y`` and ``Y``
    K.Key_Z : 0x1D, # ``z`` and ``Z``

    K.Key_1 : 0x1E, # ``1`` and ``!``
    K.Key_2 : 0x1F, # ``2`` and ``@``
    K.Key_3 : 0x20, # ``3`` and ``#``
    K.Key_4 : 0x21, # ``4`` and ``$``
    K.Key_5 : 0x22, # ``5`` and ``%``
    K.Key_6 : 0x23, # ``6`` and ``^``
    K.Key_7 : 0x24, # ``7`` and ``&``
    K.Key_8 : 0x25, # ``8`` and ``*``
    K.Key_9 : 0x26, # ``9`` and ``(``
    K.Key_0 : 0x27, # ``0`` and ``)``
    K.Key_Return : 0x28, # Enter (Return)
    K.Key_Escape : 0x29, # Escape
    K.Key_Backspace : 0x2A, # Delete backward (Backspace)
    K.Key_Tab : 0x2B, # Tab and Backtab
    K.Key_Space : 0x2C, # Spacebar
    K.Key_Minus : 0x2D, # ``-` and ``_``
    K.Key_Equal : 0x2E, # ``:` and ``+``
    K.Key_BracketLeft : 0x2F, # ``[`` and ``{``
    K.Key_BracketRight : 0x30, # ``]`` and ``}``
    K.Key_Backslash : 0x31, # ``\`` and ``|``
#    POUND : 0x32, # ``#`` and ``~`` (Non-US keyboard)
    K.Key_Semicolon : 0x33, # ``;`` and ``:``
    K.Key_Apostrophe : 0x34, # ``'`` and ``"``
    K.Key_QuoteLeft : 0x35, # :literal:`\`` and ``~``
    K.Key_Comma : 0x36, # ``,`` and ``<``
    K.Key_Period : 0x37, # ``.`` and ``>``
    K.Key_Slash : 0x38, # ``/`` and ``?``

    K.Key_CapsLock : 0x39, # Caps Lock

    K.Key_F1 :  0x3A, # Function key F1
    K.Key_F2 :  0x3B, # Function key F2
    K.Key_F3 :  0x3C, # Function key F3
    K.Key_F4 :  0x3D, # Function key F4
    K.Key_F5 :  0x3E, # Function key F5
    K.Key_F6 :  0x3F, # Function key F6
    K.Key_F7 :  0x40, # Function key F7
    K.Key_F8 :  0x41, # Function key F8
    K.Key_F9 :  0x42, # Function key F9
    K.Key_F10 :  0x43, # Function key F10
    K.Key_F11 :  0x44, # Function key F11
    K.Key_F12 :  0x45, # Function key F12

#    K.Key_Print : 0x46, # Print Screen (SysRq)
    K.Key_ScrollLock : 0x47, # Scroll Lock
    K.Key_Pause : 0x48, # Pause (Break)

    K.Key_Insert : 0x49, # Insert
    K.Key_Home : 0x4A, # Home (often moves to beginning of line)
    K.Key_PageUp : 0x4B, # Go back one page
    K.Key_Delete : 0x4C, # Delete forward
    K.Key_End : 0x4D, # End (often moves to end of line)
    K.Key_PageDown : 0x4E, # Go forward one page

    K.Key_Right : 0x4F, # Move the cursor right
    K.Key_Left : 0x50, # Move the cursor left
    K.Key_Down : 0x51, # Move the cursor down
    K.Key_Up : 0x52, # Move the cursor up

    K.Key_NumLock : 0x53, # Num Lock (Clear on Mac)
#    KEYPAD_FORWARD_SLASH : 0x54, # Keypad ``/``
#    KEYPAD_ASTERISK : 0x55, # Keypad ``*``
#    KEYPAD_MINUS : 0x56, # Keyapd ``-``
#    KEYPAD_PLUS : 0x57, # Keypad ``+``
#    KEYPAD_ENTER : 0x58, # Keypad Enter
#    KEYPAD_ONE : 0x59, # Keypad ``1`` and End
#    KEYPAD_TWO : 0x5A, # Keypad ``2`` and Down Arrow
#    KEYPAD_THREE : 0x5B, # Keypad ``3`` and PgDn
#    KEYPAD_FOUR : 0x5C, # Keypad ``4`` and Left Arrow
#    KEYPAD_FIVE : 0x5D, # Keypad ``5``
#    KEYPAD_SIX : 0x5E, # Keypad ``6`` and Right Arrow
#    KEYPAD_SEVEN : 0x5F, # Keypad ``7`` and Home
#    KEYPAD_EIGHT : 0x60, # Keypad ``8`` and Up Arrow
#    KEYPAD_NINE : 0x61, # Keypad ``9`` and PgUp
#    K.Key_Launch0 : 0x62, # Keypad ``0`` and Ins
#    K.Key_periodcentered : 0x63, # Keypad ``.`` and Del
#    KEYPAD_BACKSLASH : 0x64, # Keypad ``\\`` and ``|`` (Non-US)

#    K.Key_Menu : 0x65, # Application: also known as the Menu key (Windows)
#    K.Key_PowerDown : 0x66, # Power (Mac)
#    KEYPAD_EQUALS : 0x67, # Keypad ``:`` (Mac)
#    K.Key_F13 :  0x68, # Function key F13 (Mac)
#    K.Key_F14 :  0x69, # Function key F14 (Mac)
#    K.Key_F15 :  0x6A, # Function key F15 (Mac)
#    K.Key_F16 :  0x6B, # Function key F16 (Mac)
#    K.Key_F17 :  0x6C, # Function key F17 (Mac)
#    K.Key_F18 :  0x6D, # Function key F18 (Mac)
#    K.Key_F19 :  0x6E, # Function key F19 (Mac)

    K.Key_Control : 0xE0, # Control modifier left of the spacebar
    K.Key_Shift : 0xE1, # Shift modifier left of the spacebar
    K.Key_Alt : 0xE2, # Alt modifier left of the spacebar
    K.Key_Super_L : 0xE3, # GUI modifier left of the spacebar
    K.Key_Meta : 0xE3, 
#    GUI : LEFT_GUI, # Alias for LEFT_GUI; GUI is also known as the Windows key, Command (Mac), or Meta
#    RIGHT_CONTROL : 0xE4, # Control modifier right of the spacebar
#    RIGHT_SHIFT : 0xE5, # Shift modifier right of the spacebar
#    RIGHT_ALT : 0xE6, # Alt modifier right of the spacebar
#    RIGHT_GUI : 0xE7, # GUI modifier right of the spacebar
}

def modifier_bit(keycode):
    """Return the modifer bit to be set in an HID keycode report if this is a
    modifier key; otherwise return None."""
    return 1 << (keycode - 0xE0) if keymap[K.Key_Control] <= keycode else None

def create_key_report(list_of_keys, n=6):
    list_of_keys = list_of_keys[:n]
    mod = 0
    rep = [0] * n
    i = 0
    for k in list_of_keys:
        if k in keymap:
            k = keymap[k]
            m = modifier_bit(k)
            if m is not None:
                mod |= m
            else:
                rep[i] = k
                i += 1
    return struct.pack('<' + 'B' * (2 + n), mod, 0, *rep)
