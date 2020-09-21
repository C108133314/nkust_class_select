
from selenium.webdriver.chrome.options import Options
import selenium.webdriver as webdriver
import time
import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import sys

def set_header_user_agent():
    user_agent = UserAgent()
    return user_agent.random

def wait(x_path):
    WebDriverWait(driver, 60, 0.1).until(EC.presence_of_element_located((By.XPATH,x_path)))

def class_select(nums):
    time.sleep(1)
    #wait('/html/body/div[1]/div[1]/div[2]/div/section/div[1]/div/div/div[2]/form/div[6]/input[2]')
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/section/div[1]/div/div/div[2]/form/div[6]/input[2]').send_keys(nums) # 課號
    wait('/html/body/div[1]/div[1]/div[2]/div/section/div[1]/div/div/div[2]/form/div[8]/button')
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/section/div[1]/div/div/div[2]/form/div[8]/button').click()
    
    
    WebDriverWait(driver, 60, 0.3).until(EC.presence_of_element_located((By.ID, nums)))
    choice = driver.find_elements_by_id(nums)
    
    for a in choice:
        try:
            a.click()
            time.sleep(1.5)
            print("嘗試課號{}".format(nums))
            print(len(choice))
        except:
            continue
    
   
    



def start():
    driver.get(url)
    wait('/html/body/div[2]/div/div/div/div[2]/form/div[3]/div/button')
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div[1]/div/input').send_keys(account) #輸入帳號(需更改)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div[2]/div/input').send_keys(password) #輸入你的密碼(需更改)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div[3]/div/button').click() #登入
    
    wait('/html/body/div/nav/ul[1]/li[1]/a/i')
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div/nav/ul[1]/li[1]/a/i').click()
    time.sleep(0.5)
    wait('/html/body/div[1]/aside[1]/div/nav/ul/li[1]/a')
    driver.find_element_by_xpath('/html/body/div[1]/aside[1]/div/nav/ul/li[1]/a').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div/aside[1]/div/nav/ul/li[1]/ul/li[1]/a').click()
    
    
    for a in choices:
        class_select(a)
    driver.close()
    


if __name__ == "__main__":
    account = input("請輸入學號 ")
    password = input("請輸入密碼 ")
    choices = []
    
    while True:
        class_nums = input("請輸入課號(輸入-1結束) ")
        if class_nums == '-1':
            break
        choices.append(class_nums)
    print("學號: {}\n密碼: {}\n要搶的課為:".format(account, password))
    for c in choices:
        print("         "+c)
    ans = input("確認(y/n)")
    if ans == 'n':
        sys.exit()
        print('再見')
    print("開始搶課")        

    a = 1
    while True:
        print("第{}輪".format(a))
        try:
            driver_path = r'C:\\Users\\Jason\\Documents\\python\\webdriver\\chromedriver.exe'
            user_agent = set_header_user_agent()    
            opts = Options().add_argument("user-agent={}".format(user_agent))
            driver = webdriver.Chrome(driver_path, options=opts)
            url = 'https://aais5.nkust.edu.tw/selcrs_std'
            
            
            start()
            a+=1
        except:
            continue

