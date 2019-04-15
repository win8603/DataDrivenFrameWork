#encoding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

def getElement(driver, locateType, locatorExpression):
	try:
		element = WebDriverWait(driver, 30).until\
		   (lambda x: x.find_element(by = locateType, value = locatorExpression))
		return element
	except Exception as e:
		raise e

def getElements(driver, locateType, locatorExpression):
	try:
		elements = WebDriverWait(driver, 30).until\
		  (lambda x: x.find_elements(by = locateType, value = locatorExpression))
		return elements
	except Exception as e:
		raise e

if __name__ == '__main__':
   driver = webdriver.Chrome()
   driver.get("https://www.baidu.com")
   searchbox = getElement(driver, "id", "kw")
   print(searchbox.tag_name)

   aList = getElements(driver, "tag name", "a")
   print(len(aList))
   driver.quit()		  

