from cyber_tools import get_hashed_password, hashes_match, get_popular_passwords_from_file

popular_passwords_list = []
count = 0
get_popular_passwords_from_file("passwords.txt", popular_passwords_list)
username1 = input("enter username: ")
user = username1
password = input("enter password: ")

with open("passwords.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        username, pw = line.split(" ")
        for popular_password in popular_passwords_list:
            result = get_hashed_password(password, "md5")
            userhash = get_hashed_password(username1, "md5")
            if hashes_match(username, userhash):
                if hashes_match(result, pw):
                    print("welcome " + user)

