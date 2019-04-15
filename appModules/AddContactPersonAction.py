#encoding=utf-8
import sys
sys.path.append('..')
import importlib
import time, traceback
from appModules.LoginAction import LoginAction
from selenium import webdriver
importlib.reload(sys)
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
class AddContactPerson(object):
	def __init__(self):
		print("add contact person")

	@staticmethod 
	def add(driver, contactName, contactEmail, isStar, contactPhone, contactComment):
		try:
			hp = HomePage(driver)
			hp.addressLink().click()
			time.sleep(10)
			apb = AddressBookPage(driver)
			apb.createContactPersonButton().click()
			if contactName:
				apb.contactPersonName().send_keys(contactName)
				apb.contactPersonEmail().send_keys(contactEmail)
				if isStar == u"是":
					apb.starContacts().click()
				if contactPhone:
					apb.contactPersonMobile().send_keys(contactPhone)
				if contactComment:
					apb.contactPersonComment().send_keys(contactComment)
				apb.saveContacePerson().click()
		except Exception as e:
			print(traceback.print_exc())
			raise e

if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.get("http://mail.126.com")
	#driver.implicitly_wait(60)
	driver.maximize_window()
	time.sleep(10)
	LoginAction.login(driver, "ouyang8603","198603")
	time.sleep(10)
	AddContactPerson.add(driver, u"张三","zs@qq.com", "", "", "")
	time.sleep(10)
	assert u"张三" in driver.page_source
	driver.quit()
							
