from action import BotFaceBook
import time 
    
if __name__ == '__main__':
    path_acc = "E:/Data/AI_Files/KLTN/account.txt"
    bot_1 = BotFaceBook('Default')
    user_name, user_pass = bot_1.read_user_info(path_acc, 'nguyengiahuy100514@gmail.com')
    id_path = 'E:/Data/AI_Files/KLTN/data/id_data.txt'
    images_path = 'E:/Data/AI_Files/KLTN/data/images/'
    data_status_path = 'E:/Data/AI_Files/KLTN/data/data_status.txt'

    while True:
        print('----------------------------Menu----------------------------')
        print('0: Exit')
        print('1: Sign in facebook (only if you not sign in yet)')
        print('2: Post a status')
        print('3: Get profile from list friend')
        print("4: Comment on someone's timeline")
        print("5: Get status")
        print("6: React status")
        print("7: Share status")
        input_key = input('Mời bạn nhập vào lựa chọn: ')
        if input_key == '0':
            break
        elif input_key == '1':
            bot_1.sign_in_fb(user_name, user_pass)
        elif input_key == '2':
            input_status = input("Ban nhap status muon post: ")
            bot_1.post_status(input_key)
        elif input_key == '3':
            input_status = int(input("Ban nhap profile ban muon lay: "))
            bot_1.get_profile()
        elif input_key == '4':
            input_cmt= input("Ban nhap comment muon post: ")
            num_cmt = int(input("Ban nhap so luong post ban muon comment: "))
            profile_cmt = input("Ban nhap profile muon post: ")
            bot_1.comment_timeline()
        elif input_key == '5':
            profile_get = input("Ban nhap profile muon post: ")
            num_stt = int(input("Ban nhap so status ban muon lay: "))
            bot_1.get_status(profile_get, num_stt, id_path, data_status_path, images_path)
        elif input_key == '6':
            code_react = int(input("Kieu cam xuc ban muon chon: "))
            post_url = input("Ban nhap profile muon post: ")
            bot_1.get_fb(post_url)
            bot_1.react_status(code_react)
        elif input_key == '7':
            post_url = input("Ban nhap profile muon post: ")
            code_share = int(input("Kieu share ban muon: "))
            caption = input("Kieu share ban muon: ")
            bot_1.get_fb(post_url)
            bot_1.share_status(caption, code_share)
