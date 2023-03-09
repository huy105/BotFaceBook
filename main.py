from action import BotFaceBook
import time 
    
if __name__ == '__main__':
    path_acc = "E:/Data/AI_Files/KLTN/account.txt"
    bot_1 = BotFaceBook('Default')
    user_name, user_pass = bot_1.read_user_info(path_acc, 'nguyengiahuy100514@gmail.com')
    status_fb = "Life is 10% what happens to you and 90% how you react to it." 
    # bot_1.get_fb()
    # bot_1.sign_in_fb(user_name, user_pass)
    # bot_1.post_status(status_fb)
    # bot_1.get_profile()
    fb_target = 'https://www.facebook.com/luonggia.huy.105/'
    id_path = 'E:/Data/AI_Files/KLTN/data/id_data.txt'
    data_status_path = 'E:/Data/AI_Files/KLTN/data/data_status.txt'
    images_path = 'E:/Data/AI_Files/KLTN/data/images/'
    bot_1.get_status(fb_target, 2, id_path, data_status_path, images_path)
    # bot_1.react_status(fb_target, 6, 2)
    # bot_1.comment_timeline(fb_target, 2, list_comment)
    # data_path = 'E:/Data/AI_Files/KLTN/data_status.txt'
    # bot_1.get_status(fb_target, data_path, 5)
    # time.sleep(5)
