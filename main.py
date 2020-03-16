#Official libraries
import ctypes

#Imported libraries
import keyboard
import pygetwindow as gw
import win32api

#Defining all the shortcuts
sc_kill = 'ctrl+alt+§'
sc_mini = 'shift+§'
sc_fullscreen = 'ctrl+§'
sc_region1 = 'ctrl+1'
sc_region2 = 'ctrl+2'
sc_region3 = 'ctrl+3'
sc_region4 = 'ctrl+4'


def screen_information(monitor_nb):  
    return (((win32api.EnumDisplayMonitors()[monitor_nb][2][2]) - (win32api.EnumDisplayMonitors()[monitor_nb][2][0])), win32api.EnumDisplayMonitors()[monitor_nb][2][3])


def taskbar_information():
    monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0,0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    return monitor_area[3]-work_area[3]


def go_fullscreen():
    activeWindow =  gw.getActiveWindow()
    if activeWindow.isMaximized:
        activeWindow.restore()
    else:
        activeWindow.maximize()


def go_region1():
    activeWindow =  gw.getActiveWindow()
    screenSize = screen_information(0)
    taskbar = taskbar_information()
    
    width = screenSize[0] /2
    heigth = screenSize[1] - taskbar

    activeWindow.restore()
    activeWindow.moveTo(0,0)
    activeWindow.resizeTo(int(width), int(heigth))


def go_region2():
    activeWindow =  gw.getActiveWindow()
    screenSize = screen_information(0)
    taskbar = taskbar_information()
    
    width = screenSize[0] /2
    heigth = screenSize[1] - taskbar

    activeWindow.restore()
    activeWindow.moveTo(int(width),0)
    activeWindow.resizeTo(int(width), int(heigth))


def go_region3():
    activeWindow =  gw.getActiveWindow()
    screenSize = screen_information(1)
    monitor1 = screen_information(0)
    taskbar = taskbar_information()
    
    width = screenSize[0] /2
    heigth = screenSize[1] - taskbar

    activeWindow.restore()
    activeWindow.moveTo(int(monitor1[0]),0)
    activeWindow.resizeTo(int(width), int(heigth))


def go_region4():
    activeWindow =  gw.getActiveWindow()
    screenSize = screen_information(1)
    monitor1 = screen_information(0)
    taskbar = taskbar_information()
    
    width = screenSize[0] /2
    heigth = screenSize[1] - taskbar

    activeWindow.restore()
    activeWindow.moveTo(int(monitor1[0]) + int(width),0)
    activeWindow.resizeTo(int(width), int(heigth))


def go_mini():
    activeWindow =  gw.getActiveWindow()
    activeWindow.minimize()


def main():
    #keyboard.add_hotkey(sc_setup, go_setup)
    keyboard.add_hotkey(sc_mini, go_mini)
    keyboard.add_hotkey(sc_fullscreen, go_fullscreen)
    keyboard.add_hotkey(sc_region1, go_region1)
    keyboard.add_hotkey(sc_region2, go_region2)
    keyboard.add_hotkey(sc_region3, go_region3)
    keyboard.add_hotkey(sc_region4, go_region4)
    keyboard.wait(sc_kill)


if __name__ == '__main__':
    main()
