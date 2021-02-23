from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = r'C:\Program Files (x86)\chromedriver.exe'
MAIL = 'dylan.tintenfich@alumnos.frm.utn.edu.ar'
WIN_LENGTH = 900
WIN_HEIGHT = 900
SLEEP_TIME = 2


class UTNBot:

    def __init__(self, username, password):

        self.driver = webdriver.Chrome(PATH)
        self.driver.set_window_size(WIN_LENGTH, WIN_HEIGHT)
        self.mail = MAIL
        self.username = username
        self.password = password
        self.logged_in = False

    def auto_gestion(self):
        self.driver.get('https://sysacad.frm.utn.edu.ar/login.php')
        time.sleep(SLEEP_TIME)
        dni = self.driver.find_element_by_xpath('//input[@name="username"]')
        pwd = self.driver.find_element_by_xpath('//input[@name="password"]')
        dni.send_keys(self.username)
        pwd.send_keys(self.password, Keys.RETURN)
        time.sleep(SLEEP_TIME)
        self.driver.find_element_by_class_name('habilitado').click()

    def mail_login(self):
        self.driver.get('https://alumnos.frm.utn.edu.ar/webmail2/')
        if not self.logged_in:
            time.sleep(SLEEP_TIME)
            mail = self.driver.find_element_by_xpath('//input[@name="_user"]')
            pwd = self.driver.find_element_by_xpath('//input[@name="_pass"]')
            mail.send_keys(self.mail)
            pwd.send_keys(self.password, Keys.RETURN)
            self.logged_in = True
