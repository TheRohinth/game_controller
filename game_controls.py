import pyautogui

def press_up():
    pyautogui.press('up')

def press_down():
    pyautogui.press('down')

def press_left():
    pyautogui.press('left')

def press_right():
    pyautogui.press('right')

def hold_up():
    pyautogui.keyUp('down')
    pyautogui.keyDown('up')

def hold_down():
    pyautogui.keyUp('up')
    pyautogui.keyDown('down')

def hold_left():
    pyautogui.keyUp('right')
    pyautogui.keyDown('left')

def hold_right():
    pyautogui.keyUp('left')
    pyautogui.keyDown('right')

def release_l_f():
    pyautogui.keyUp('right')
    pyautogui.keyUp('left')