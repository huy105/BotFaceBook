from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with
from typing import List
import pyautogui as pag
import urllib.request
import random
import time
import os

class BotFaceBook():
    
    list_react = ['Thích', 'Yêu Thích', 'Thương thương', 'Haha', 'Wow', 'Buồn', 'Phẫn nộ']

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
                ActionChains(self.driver).scroll_by_amount(0, amount_scroll).perform()
                list_element_comment = self.driver.find_elements(By.XPATH, '//div[@class="x1n2onr6"]/div[@aria-label= "Viết bình luận..."]')
                num_post_get = len(list_element_comment)
                
                amount_scroll += 2000
                tries_time += 1
                if tries_time > 5:
                    break
            count = 0
            for e in list_element_comment:
                ActionChains(self.driver).click(e).send_keys(random.choice(list_comment)).send_keys(Keys.ENTER).perform()
                count += 1
                if count == num_post:
                    break
        except:
            print("Could not find element.")


    def get_status(self, profile_url: str, num_status: int, id_path: str, data_status_path: str, images_path: str):
        """
        There is 2 kinds of status, ones is with image(or share smt), second is only string
        profile_url: url of profile which you wanna get status
        data_path: path of file text we save status 
        num_status: number of status,.. you wanna get
        """
        xpath_txt = "//div[@class='x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a']"
        xpath_post = "//span[@class='x4k7w5x x1h91t0o x1h9r5lt xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j x1jfb8zj']"
        xpath_stt1 = "//img[@class='x1ey2m1c xds687c x5yr21d x10l6tqk x17qophe x13vifvy xh8yej3 xl1xv1r']"
        xpath_stt2 = "//div[@class='xzsf02u xngnso2 xo1l8bm x1qb5hxa']"

        self.driver.get(profile_url)
        self.driver.implicitly_wait(5)
    
        list_ele_stt1 = self.driver.find_elements(By.XPATH, xpath_stt1)
        list_ele_stt2 = self.driver.find_elements(By.XPATH, xpath_stt2)
        
        num_post_get = len(list_ele_stt1) + len(list_ele_stt2) 
        amount_scroll = 0
        tries_time = 0
        
        # get element untill enough
        while num_post_get < num_status:
            ActionChains(self.driver).scroll_by_amount(0, amount_scroll).perform()
            self.driver.implicitly_wait(5)
            
            list_ele_stt1 = self.driver.find_elements(By.XPATH, xpath_stt1)
            list_ele_stt2 = self.driver.find_elements(By.XPATH, xpath_stt2)
            num_post_get = len(list_ele_stt1) + len(list_ele_stt2) 
            
            amount_scroll += 2000
            tries_time += 1
            if tries_time > 5:
                break
        
        with open(id_path, 'r', encoding="utf-8") as f:
            id_data = int(f.read())
            f.close()

        if os.path.isfile(data_status_path):
            action = 'a'
        else:
            action = 'x'
        
        count = 0
        with open(data_status_path, action, encoding="utf-8") as f:
            for e in (list_ele_stt1 + list_ele_stt2):
                if count == num_status:
                    break
                
                id_data += 1
                if count < len(list_ele_stt1):
                    url_image =  e.get_attribute('src')
                    urllib.request.urlretrieve(url_image, images_path + '/{}.png'.format(id_data))
                    e = self.driver.find_element(locate_with(By.XPATH, xpath_txt).above(e))

                e_post = self.driver.find_element(locate_with(By.XPATH, xpath_post).above(e))
                ActionChains(self.driver).key_down(Keys.CONTROL).click(e_post).key_up(Keys.CONTROL).perform()
                url_post = self.driver.current_url
                pag.hotkey('ctrl', 'w')
                
                f.write(id_data + '\n')
                f.write(url_post + '\n')
                f.write(e.text + '\n')
                count += 1
                
            f.close()
            
        with open(id_path, 'w', encoding="utf-8") as f:
            f.write(str(id_data))  
            f.close()

    def react_status(self, post_url_id: str, emotion: int, num_status: int = 1):
        """
        emotion: is the kind of emotion we want to react
        (0: Thích, 1: Yêu Thích, 2: Thương Thương, 3: Haha, 4: Wow, 5: Buồn, 6: Phẫn nộ) 
        num_status: number of status,.. you want react
        """
        self.driver.get(post_url_id)
        self.driver.implicitly_wait(5)
        hover_e_react = self.driver.find_element(By.XPATH, '//div[@aria-label="Thích"]')

        ActionChains(self.driver).move_to_element(hover_e_react).perform()
        self.driver.implicitly_wait(5)
        try:
            element = self.driver.find_element(By.XPATH, "//div[@aria-label='{}' and @role='button']".format(self.list_react[emotion]))
            if element.is_displayed():
                element.click()
            else:
                print("Element is not visible.")
        except:
            print("Could not find element.")
        
        time.sleep(5)