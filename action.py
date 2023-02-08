from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

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


    def post_status(self, status_str: str = "just a status"):
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

