import requests
import random
import string
import concurrent.futures

result = open(r"workingGhosts.txt","a+")
length = 5
url ="https://ghostbin.co/paste/"

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters+ string.digits) for i in range(length))
    return result_str

def lol(finalUrl):
    global counter  # add this line
    r = requests.get(finalUrl)
    counter= counter +1
    if r.status_code != 404:
        result.write(finalUrl + "\n")
        print(finalUrl)


print("""   _____ _               _   ____  _         _____       __      __   _ _     _ 
  / ____| |             | | |  _ \(_)       / ____|      \ \    / /  | (_)   | |
 | |  __| |__   ___  ___| |_| |_) |_ _ __  | |     ___    \ \  / /_ _| |_  __| |
 | | |_ | '_ \ / _ \/ __| __|  _ <| | '_ \ | |    / _ \    \ \/ / _` | | |/ _` |
 | |__| | | | | (_) \__ \ |_| |_) | | | | |_ |____ (_) |    \  / (_| | | | (_| |
  \_____|_| |_|\___/|___/\__|____/|_|_| |_(_)_____\___/      \/ \__,_|_|_|\__,_|""")
print("CREDITS INSTAGRAM: socialmediaboosterlb TELEGRAM: socialmediaboosterlb")

times = int(input("how many tries do you want to make?"))

list_urls=[]

counter = 0
for x in range(times):
    stringA = url + get_random_string(length)
    list_urls.append(stringA)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(lol,list_urls)