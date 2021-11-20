from urllib.parse import urldefrag
from instapy import InstaPy
from random import randint,choice,shuffle,random
import os
import string
from instapy.browser import set_selenium_local_session
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from instapy.comment_util import comment_image
import selenium
import time
import pass_insta
#from webdriver_manager.chrome import ChromeDriverManager

def spammbot():
    username_insta=pass_insta.username
    pwd=pass_insta.password

    f = open("...", "r") # path to usernames csv
    names = f.readlines()

    coments=[]
    letters = string.digits
    for i in range(0,len(names)):
        number = int(randint(0,2))
        user = str('@' + names[i].rstrip().lower()+ '_' + ''.join([choice(letters) for i in range(number)]))
        coments.append(user)

    def reshape(lst, n):
        return [lst[i*n:(i+1)*n] for i in range(len(lst)//n)]

    shuffle(coments)

    coments = reshape(coments,2)

    comment = []
    for i in range(0,len(coments)):
        comment.append(str(coments[i][0] + ' ' + coments[i][1]))




    # driver = webdriver.Chrome(ChromeDriverManager().install())
    url1=[#links here]
    session = InstaPy(username=...,password=...).login()
    session.interact_by_URL(urls=url1)

    # session.browser.minimize_window()

    session.browser.find_element_by_class_name('wpO6b').click()

    counter = 0
    for i in comment:
        try:
            inputElement = session.browser.find_element_by_class_name("Ypffh")

            inputElement.send_keys(i + ' vamos ganhar!!')
            time.sleep(random())
            session.browser.find_element_by_class_name('sqdOP').click()
            
            time.sleep(randint(10,15))

            inputElement.clear()

            counter=counter+1
        except:
            try:
                inputElement.send_keys(i)
                time.sleep(random())
                session.browser.find_element_by_class_name('sqdOP').click()
                
                time.sleep(randint(10,15))

                inputElement.clear()
            except:
                print(i,counter)
                time.sleep(random())
                session.browser.refresh()
    print("Numero de comentários: " + str(counter))
    session.end()


spammbot()
