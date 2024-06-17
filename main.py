import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SIMILAR_ACCOUNT = ""
USERNAME = "..."
PASSWORD = "..."
INSTAGRAM = "https://www.instagram.com/"

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(INSTAGRAM)

        time.sleep(2)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)

        time.sleep(0.5)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)

        time.sleep(0.5)
        log_in = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
        log_in.click()

        time.sleep(3)
        information = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_C9"]/div/div/div[2]/div/div/div[1]/'
                                                               'div[1]/div[2]/section/main/div/div/div/div/div')
        information.click()

        time.sleep(1.5)
        notifications = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/'
                                                                 'div[2]/div/div/div[3]/button[2]')
        notifications.click()

    def find_followers(self):
        pass

    def follow(self):
        pass

    # time.sleep(5)
    # driver.quit()


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
