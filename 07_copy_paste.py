'''
螢幕 x = 0 ~ 775
左分頁爲試算表，右爲 MusicYoutube
於 macbook air 2014 作業，瀏覽器爲 safari
設定切換瀏覽器分頁之快捷鍵爲 command + option + 左右方向鍵
測試專輯列表：https://docs.google.com/spreadsheets/d/1zcPXfjUMzrjbT6minYaC59XlzLpET1lzIn-OwfpUw38/edit#gid=0
'''
from pyautogui import *
hotkey('command','tab')#切換回瀏覽器
def copySearched():
    hotkey('shiftleft','right')#選擇兩格資料
    hotkey('command','c')#複製資料

    click(575,92)#切到youtubeMusic 分頁
    click(475,134)#點選搜尋(475,134)
    hotkey('command','v')#貼上資料
    sleep(1)#等待停留
    press('enter')#按下搜尋

    sleep(2)#等待停留搜尋時間
    #從熱門搜尋結果
    click(189,321)#按連結(189,321)、(185,388)=〔目前顯示的是以下查詢字詞的搜尋結果〕用
    sleep(2)#連結時間
    click(400,50)#點網址列
    sleep(0.5)
    hotkey('command','x')#剪連結
    sleep(0.5)
    press('esc')#跳出網址列選單
    sleep(0.5)
    click(634,139)#按下畫面打叉、去除搜尋結果
    sleep(0.5)
    
    hotkey('command','option','left')#換回試算表分頁
    sleep(0.5)
    press('right')#移到正確輸入格
    sleep(0.2)#停頓
    press('right')
    hotkey('command','v')#貼上資料
    sleep(0.5)
    press(['left','left','down'])
    sleep(0.5)

for i in range(20):#作幾次，看試算表有幾筆資料
    copySearched()