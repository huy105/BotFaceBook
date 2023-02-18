from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from typing import List
import random
import pyautogui as pag
import time

class BotFaceBook():
    def __init__(self, profile: str = 'Profile 1', dir_path: str = 'C:/Users/luong/AppData/Local/Google/Chrome/User Data') -> None:
        
        """
        dir_path: path of profile directory
        
        """

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--user-data-dir=" + dir_path)
        self.options.add_argument('--profile-directory=' + profile)
        self.ser = Service("E:/Data/AI_Files/KLTN/envDriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service= self.ser, chrome_options= self.options)


    def get_fb(self, url: str = 'https://vi-vn.facebook.com/'):
        self.driver.get(url)

    def read_user_info(self, path_dir: str, user_name_valid):
        f = open(path_dir, "r")
        user_name = f.readline().strip()
        user_pass = f.readline().strip()
        assert user_name == user_name_valid
        return user_name, user_pass

    def sign_in_fb(self, user_name: str, user_pass: str):

        self.driver.implicitly_wait(5)

        user_box = self.driver.find_element(by=By.NAME, value="email")
        pass_box = self.driver.find_element(by=By.NAME, value="pass")
        login_button = self.driver.find_element(by=By.NAME, value="login")

        user_box.send_keys(user_name)
        pass_box.send_keys(user_pass)
        login_button.click()
        print("Login succesfull")


    def post_status(self, status_str: str = "Life is 10% what happens to you and 90% how you react to it."):
        valueXPath = '//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]'
        status_box_button = self.driver.find_element(by=By.XPATH, value=valueXPath)                         
        status_box_button.click()

        self.driver.implicitly_wait(5)

        valueXPath = '//div[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw x9f619 x1lliihq x5yr21d xh8yej3 notranslate"]'
        type_status = self.driver.find_element(by=By.XPATH, value=valueXPath) 
        type_status.send_keys(status_str)

        self.driver.implicitly_wait(5)

        valueXPath = '//div[@aria-label="Đăng" and @role="button"]'
        status_post_button = self.driver.find_element(by=By.XPATH, value=valueXPath)
        status_post_button.click()

    def get_profile(self, num_profiles: int = 5):
        """
        open profile in new tab and get infomation
        num_profiles is number of profiles you wanna get
        """
        
        link = self.driver.find_element(By.XPATH, '//a[@href="/friends/"]')
        action_chain = ActionChains(self.driver)
        action_chain.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        self.driver.switch_to.window(self.driver.window_handles[-1])

        list_profile = []
        # loop to get multiple profile
        for i in range(1, num_profiles + 1):
            
            profile_getted = self.driver.find_element(By.XPATH, f'//div[@class="xsag5q8"]/div/div[{i}]')
            action_chain.key_down(Keys.CONTROL).click(profile_getted).key_up(Keys.CONTROL).perform()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            
            url_profile = self.driver.current_url[0:33] + self.driver.current_url[45:]
            list_profile.append(url_profile)

            pag.hotkey('ctrl', 'w')
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)

        print('-------------------------------profile-------------------------------')
        print(list_profile)

    def comment_timeline(self, profile_url: str, num_post: int = 1, list_comment: List = ['.']):
        """
        profile_url: url of profile which you wanna comment
        num_post: number of status,.. you wanna comment
        """
        self.driver.get(profile_url)
    
        try:
            list_element_comment = self.driver.find_elements(By.XPATH, '//div[@class="x1n2onr6"]/div[@aria-label= "Viết bình luận..."]')
            num_post_get = len(list_element_comment)
            amount_scroll = 0
            tries_time = 0

            while num_post_get < num_post:
                list_element_comment = self.driver.find_elements(By.XPATH, '//div[@class="x1n2onr6"]/div[@aria-label= "Viết bình luận..."]')
                num_post_get = len(list_element_comment)
                ActionChains(self.driver).scroll_by_amount(0, amount_scroll).perform()
                
                amount_scroll += 2000
                tries_time += 1
                if tries_time > 5:
                    break
            
            time.sleep(20)
            count = 0
            for e in list_element_comment:
                ActionChains(self.driver).click(e).send_keys(random.choice(list_comment)).send_keys(Keys.ENTER).perform()
                count += 1
                if count == num_post + 1: 
                    break
                time.sleep(20)
            
        except:
            print("Could not find element.")