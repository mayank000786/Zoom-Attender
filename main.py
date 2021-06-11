import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pswd):
    #Opens up the zoom app
    #change the path specific to your computer
    
    #If on windows use below line for opening zoom
    #subprocess.call('C:\\myprogram.exe')
    
    #If on mac / Linux use below line for opening zoom
    subprocess.call([r"C:\Users\manish mishra\AppData\Roaming\Zoom\bin\Zoom.exe"])
       
    time.sleep(10)

    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    time.sleep(10)

    # Type the meeting ID
    pyautogui.write(meetingid)

    # Disables both the camera and the mic
    media_btn = pyautogui.locateAllOnScreen('media_btn.png')

    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)

    # Hits the join button
    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

     # Hits the join button
    join_code = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    pyautogui.moveTo(join_code)
    pyautogui.click()

    #Types the password and hits enter
    time.sleep(5)
    pyautogui.write(pswd,interval=0.25)
    pyautogui.press('enter')
    


# Reading the file
df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in(m_id, m_pswd)
       time.sleep(60)
       print('signed in')
