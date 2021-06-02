import pyautogui
pyautogui.moveTo(100,100,duration=0.5)#移動到100,100 以速度 0.5 的時間過去
pyautogui.moveTo(200,200)#移動到200,200
pyautogui.move(100,-100,duration=0.5)#相對移動往右上
print(pyautogui.position())#得到滑鼠座標
