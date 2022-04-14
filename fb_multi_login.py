
from selenium.webdriver.common.by import By
from selenium import webdriver
from csv import reader
import time

# create web scraping function to use it after and many times
def logIn(mail, passw):
    if mail != "" and passw != "":
        driver = webdriver.Chrome("chromedriver.exe")
        try:
            driver.get('https://www.facebook.com/')

            # mail fiel box
            # get xpath by name of input
            email_field = driver.find_element(by=By.XPATH, value='//input[@name="email"]')
            email_field.clear()
            email_field.send_keys(mail)

            time.sleep(2)

            # passwword field box
            password_field = driver.find_element(by=By.XPATH, value='//input[@name="pass"]')
            password_field.clear()
            password_field.send_keys(passw) 
            
            # Login Button
            # get xpath by name of the button
            login = driver.find_element(by=By.XPATH, value='//button[@name="login"]')
            login.click()

            # provides some time to be able to see what's going on
            time.sleep(10)
            driver.quit()
        except:
            driver.quit()
    else:
        print("Username or password is invalid or null")

    
# read my file of users (There is 4 records in my file)
with open('users.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    # pass delimiter (;) because csv is separated by (;), if it's (,) don't pass the delimiter
    csv_reader = reader(read_obj, delimiter =';')
    # Pass reader object to list() to get a list of lists
    users_list = list(csv_reader)

# Loop through my list of users
for i in range(len(users_list)):
    mail = users_list[i][0]  #column 0 - row 0,1,2 & 3
    passw = users_list[i][1] #column 1 - row 0,1,2 & 3
    print(i)
    print("Login Mail: ", mail)
    print("Login Password: ", passw)

    logIn(mail, passw)