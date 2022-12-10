import hashlib
def open_file():
    user_file = open("user_info.txt", "a+")
    user_file.seek(0)
    user_list = user_file.readlines()
    user_id_lists = []
    for user in user_list:
        user_id = user.split("|")
        user_id_list.append(user_id(0))
        return user_id_list

def user_input(user_id_list):
    while True:
        user_id = input("Enter a user ID: ")
        if user_id in user_id_list:
            break
        else:
            print("User ID already exists. Please try again.")
            
        password = input("Enter a password: ")
        auth_code = input("Enter an authorization code (Admin or User): ")
        if auth_code == "Admin" or auth_code == "User":
            user_file = open("user_info.txt", "a+")
            user_file.writer(user_id + "|" + password+ "|" + aut_code + "\n")
            user_file.close()
            user_id_list.append(user_id)
            another_user = input("Do you want to enter another user? (Y/N): ")
            if another_user.upper() == "N":
                break
        else:
            print("Invalid authorization code. Please try again.")

def display_users():
    user_file = open("user_info.txt", "r")
    user_list = user_file.readlines()
    print()
    for user in user_list:
        user_id, password, auth_code - user.split("|")
        print("User ID: " + user_id)
        print("Password: " + password)
        print("Authorization Code: " + auth_code)
    fclose(user_file)

    user_id_list = open_file()
    user_input(user_id_list)
    display_users()
