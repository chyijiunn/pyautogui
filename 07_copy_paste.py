'''
螢幕 x = 0 ~ 775
左分頁爲試算表，右爲 MusicYoutube
於 macbook air 2014 作業，瀏覽器爲 safari
設定切換瀏覽器分頁之快捷鍵爲 command + option + 左右方向鍵
測試專輯列表：https://docs.google.com/spreadsheets/d/1zcPXfjUMzrjbT6minYaC59XlzLpET1lzIn-OwfpUw38/edit#gid=0

'''
import pyautogui
pyautogui.hotkey('command','tab')#切換回瀏覽器
def copySearched():
    pyautogui.hotkey('shiftleft','right')#選擇兩格資料
    pyautogui.hotkey('command','c')#複製資料

    pyautogui.click(575,92)#切到youtubeMusic 分頁
    pyautogui.click(475,134)#點選搜尋(475,134)
    pyautogui.hotkey('command','v')#貼上資料
    pyautogui.sleep(1)#等待停留
    pyautogui.press('enter')#按下搜尋

    pyautogui.sleep(2)#等待停留搜尋時間
    #從熱門搜尋結果
    pyautogui.click(189,321)#按連結(189,321)、(185,388)=〔目前顯示的是以下查詢字詞的搜尋結果〕用
    pyautogui.sleep(2)#連結時間
    pyautogui.click(400,50)#點網址列
    pyautogui.sleep(0.5)
    pyautogui.hotkey('command','x')#剪連結
    pyautogui.sleep(0.5)
    pyautogui.press('esc')#跳出網址列選單
    pyautogui.sleep(0.5)
    pyautogui.click(634,139)#按下畫面打叉、去除搜尋結果
    pyautogui.sleep(0.5)

    #換回試算表分頁
    pyautogui.hotkey('command','option','left')
    pyautogui.sleep(0.5)
    pyautogui.press(['right','right'])#移到正確輸入格
    pyautogui.hotkey('command','v')#貼上資料
    pyautogui.sleep(0.5)
    pyautogui.press(['left','left','down'])
    pyautogui.sleep(0.5)

for i in range(1):#作幾次，看試算表有幾筆資料
    copySearched()