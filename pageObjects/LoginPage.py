#encoding=utf-8
import sys
sys.path.append('..')
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from selenium import webdriver
import time

class LoginPage(object):
	def __init__(self, driver):
		self.driver = driver
		self.parseCF = ParseConfigFile()
		self.loginOptions = self.parseCF.getItemsSection("126mail_login")
		print(self.loginOptions)

		
	def switchToFrame(self):
		'''try:
			locatorExpression = self.loginOptions\
			    ["loginPage.frame".lower()].split(">")[1]
			self.driver.switch_to.frame(locatorExpression)
		except Exception as e:
			raise e'''
		self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[starts-with(@id,'x-URS-iframe')]"))	   


	def switchToDefaultFrame(self):
		try:
			self.driver.switch_to.default_content()
		except Exception as e:
			raise e 
		#self.driver.switch_to.default_content()

	def userNameObj(self):
		try:
			locateType, locatorExpression = self.loginOptions\
			    ["loginPage.username".lower()].split(">")
			elementObj = getElement(self.driver, locateType, locatorExpression)
			return elementObj
		except Exception as e:
			raise e

	def passwordObj(self):
		try:
			locateType, locatorExpression = self.loginOptions\
			    ["loginPage.password".lower()].split(">")
			elementObj = getElement(self.driver, locateType, locatorExpression)
			return elementObj
		except Exception as e:
			raise e

	def loginButton(self):
		try:
			locateType, locatorExpression = self.loginOptions\
			    ["loginPage.loginbutton".lower()].split(">")
			elementObj = getElement(self.driver, locateType, locatorExpression)
			return elementObj
		except Exception as e:
			raise e

	'''def quit(self):
		self.driver.quit()'''	

if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.get("https://mail.126.com")
	time.sleep(5)
	login = LoginPage(driver)
	login.switchToFrame()
	time.sleep(10)
	login.userNameObj().send_keys("ouyang8603")
	login.passwordObj().send_keys("198603")
	login.loginButton().click()
	time.sleep(10)
	login.switchToDefaultFrame()
	assert u"未读邮件" in driver.page_source
	login.quit()