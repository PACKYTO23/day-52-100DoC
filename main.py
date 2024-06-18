import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACCOUNT = ""
USERNAME = "..."
PASSWORD = "..."
INSTAGRAM = "https://www.instagram.com/"
SEARCH = "https://www.instagram.com/encorainc/following/"

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(INSTAGRAM)

        time.sleep(3)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)

        time.sleep(1)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)

        time.sleep(1)
        log_in = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
        log_in.click()

        time.sleep(5)
        info_button = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Ahora no')]")
        if info_button:
            info_button.click()

        time.sleep(2)
        noti_button = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Ahora no')]")
        if noti_button:
            noti_button.click()

    def find_followers(self):
        time.sleep(3)
        self.driver.get(SEARCH)

        time.sleep(2)
        followers_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, value=" seguidos")
        followers_button.click()

        # time.sleep(2)
        # scroll = 0
        # followers_xpath = '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]'
        # followers_list = self.driver.find_element(By.XPATH, value=followers_xpath)
        # while scroll < 3:
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight",
        #                                followers_list)
        #     scroll += 1
        #     time.sleep(2)

    def follow(self):
        time.sleep(3)
        follow_accounts = self.driver.find_elements(By.CSS_SELECTOR, value="._aade")

        for account in follow_accounts:
            try:
                account.click()
                time.sleep(1.5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Cancelar')]")
                cancel_button.click()
                time.sleep(1.5)


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
