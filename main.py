import pyautogui as pag
import keyboard
from time import sleep
import mouse

def main():
    on = False
    n = 0
    i = 0
    lm = 0
    rm = 0
    rclick = 0
    lclick = 0
    Lclicks = True
    Rclicks = False
    coords = [[],[]] #0 = x, 1 = y
    leftclicked = [[],[]] #0 = x, 1 = y
    rightclicked = [[],[]]
    while True:
        if keyboard.is_pressed('Ctrl + Space'):
            on = True
        while on:
            coords[0].append(pag.position().x)
            coords[1].append(pag.position().y)
            if mouse.is_pressed('left'):
                lm += 1
                print(f'Debug: Left Clicked Count{lm}')
                leftclicked[0].append(coords[0][i])
                leftclicked[1].append(coords[1][i])
            if mouse.is_pressed('right'):
                rm += 1
                print(f'Debug: Right Clicked Count {rm}')
                rightclicked[0].append(coords[0][i])
                rightclicked[1].append(coords[1][i])
            while n <= len(coords[0]):
                PositionStr = 'X: ' + str(coords[0][i]).rjust(4) +'Y: ' + str(coords[1][i]).rjust(4)
                print(PositionStr, end='')
                print('\b'* len(coords[0]), end='', flush=True)
                n += 1
            i += 1
            sleep(0.07)
            if keyboard.is_pressed('Ctrl + L'):
                on = False
        if keyboard.is_pressed('Ctrl + E'):
            for a in range(len(coords[0])):
                pag.moveTo(coords[0][a], coords[1][a])
                if Lclicks == True:
                    if len(leftclicked[0]) != 0:
                        if leftclicked[0][lclick] == coords[0][a] and leftclicked[1][lclick] == coords[1][a]:
                            pag.click()
                            lclick += 1
                            if lclick >= len(leftclicked[0]):
                                Lclicks = False
                if Rclicks == True:
                    if len(rightclicked[0]) != 0:
                        if rightclicked[0][rclick] == coords[0][a] and rightclicked[1][rclick] == coords[1][a]:
                            pag.rightClick()
                            rclick += 1
                            if Rclicks >= len(rightclicked[0]):
                                Lclicks = False

if __name__ == '__main__':    
    main()