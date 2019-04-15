# encoding = utf-8
import time
from selenium import webdriver
import sys 
sys.path.append("..")
from pageObjects.LoginPage import LoginPage


class LoginAction(object):
	"""docstring for ClassName"""
	def __init__(self):
		print("login...")

	@staticmethod
	def login(driver, username, password):
		try:
			logins = LoginPage(driver)

			logins.switchToFrame()
			logins.userNameObj().send_keys(username)
			logins.passwordObj().send_keys(password)
			logins.loginButton().click()
			logins.switchToDefaultFrame()
		except Exception as e:
			raise e 
if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.get("https://mail.126.com")
	time.sleep(5)
	LoginAction.login(driver, username = "ouyang8603", password = "198603")
	time.sleep(5)
	driver.quit()			

