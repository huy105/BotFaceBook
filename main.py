from action import BotFaceBook
import time 
    
if __name__ == '__main__':
    path_acc = "E:/Data/AI_Files/KLTN/account.txt"
    bot_1 = BotFaceBook()
    user_name, user_pass = bot_1.read_user_info(path_acc, 'nguyengiahuy100514@gmail.com')
    status_fb = "Life is 10% what happens to you and 90% how you react to it." 
    bot_1.get_fb()
    # bot_1.sign_in_fb(user_name, user_pass)
    # bot_1.post_status(status_fb)
    bot_1.get_profile()
    time.sleep(5)
