import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from credentials import username, password, email_address
from webdriver_manager.chrome import ChromeDriverManager
""" class TwitterBot is the template for all bots """


class TwitterBot:
    def __init__(self, email_address, password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://twitter.com/home?lang=en")
        time.sleep(2)
        # Enter your email address
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input') \
            .send_keys(email_address)
        # Enter your password
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input') \
            .send_keys(password)
        # Click on login
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div') \
            .click()
    '''
        def unusual_activity_clause(self, username, password):
        # Only use it when a page opens asking for your username and password due to some unusual activity
        # Enter username
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input') \
            .send_keys(username)
        # Enter password again
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input') \
            .send_keys(password)
        # Click Login
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div') \
            .click()
        time.sleep(4)
    '''


    def type_in_search(self, search_text):
        # Typing for something in the search bar and pressing enter
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div'
                                          '/div[1]/div/div/div/form/div[1]/div/div/div[2]/input') \
            .send_keys(search_text)
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div'
                                          '/div[1]/div/div/div/form/div[1]/div/div/div[2]/input') \
            .send_keys(Keys.ENTER)
        time.sleep(2)


my_twitter_bot = TwitterBot(email_address, password)
#my_twitter_bot.unusual_activity_clause(username, password)
my_twitter_bot.type_in_search("lamborghini")
