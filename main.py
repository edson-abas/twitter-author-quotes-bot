from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import os

TWITTER_NAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


class QuotesBot:

    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.quote = ""

    def get_quotes(self):
        with open("quotes.txt", "r", encoding="utf-8") as file:
            content = file.readlines()
            self.quote = content[random.randint(1, len(content) - 1)]
        return self.quote

    def tweet_maker(self):
        self.driver.get("https://twitter.com/")
        time.sleep(6)
        login = self.driver.find_element(By.CSS_SELECTOR, '.css-901oao.r-1awozwy.r-1cvl2hr.r-6koalj.r-18u37iz'
                                                          '.r-16y2uox.r-37j5jr.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe'
                                                          '.r-bcqeeo.r-q4m81j.r-qvutc0')
        login.click()
        time.sleep(6)

        user_input = self.driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
        user_input.send_keys(TWITTER_NAME)
        user_input.send_keys(Keys.ENTER)
        time.sleep(6)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(6)

        new_quote = self.get_quotes()
        tweet_input = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Texto do Tweet')]")
        tweet_input.send_keys(new_quote)
        time.sleep(6)

        tweet_button = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        tweet_button.click()
        time.sleep(6)

        self.driver.quit()


def main():
    bot = QuotesBot()
    bot.tweet_maker()


if __name__ == "__main__":
    main()
