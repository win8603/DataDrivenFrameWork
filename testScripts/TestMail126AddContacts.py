#encoding=utf-8
import sys
sys.path.append('..')
from pageObjects.LoginPage import LoginPage
from appModules.LoginAction import LoginAction
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from appModules.AddContactPersonAction import AddContactPerson
from selenium.webdriver.chrome.options import Options
import traceback
import importlib
import time
from selenium import webdriver
from util.Log import *
importlib.reload(sys)

excelObj = ParseExcel()
excelObj.loadWorkBook(dataFilePath)

def LaunchBrower():
	chrome_options = Options()
	chrome_options.add_argument("--disable-extensions")
	chrome_options.add_experimental_option\
	    ("excludeSwitches", ["ignore-certificate-errors"])
	chrome_options.add_argument('--start-maximzed')
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("http://mail.126.com")
	time.sleep(3)
	return driver

def test126MailAddContacts():
	logging.info(u"126邮箱添加联系人数据驱动测试开始...")
	try:
		userSheet = excelObj.getSheetByName(u"126账号")
		isExecuteUser = excelObj.getColumn(userSheet, account_isExecute)
		dataBookColumn = excelObj.getColumn(userSheet, account_dataBook)
		print(u"测试为126邮箱添加联系人执行开始...")
		for idx, i in enumerate(isExecuteUser[1:]):
			if i.value == "y":
				userRow = excelObj.getRow(userSheet, idx + 2)
				username = userRow[account_username - 1].value
				password = str(userRow[account_password - 1].value)
				print(username, password)

				driver = LaunchBrower()
				logging.info(u"启动服务器,访问126邮箱主页")

				LoginAction.login(driver, username, password)
				time.sleep(3)
				try:
					assert u"收 信" in driver.page_source
					logging.info\
					    (u"用户%s登陆后，断言页面关键字收 信成功" %username)
				except AssertionError as e:
					logging.debug(u"失败,"
						u"异常信息: %s" %(username, str(traceback.print_exc())))    
				dataBookName = dataBookColumn[idx + 1].value
				dataSheet = excelObj.getSheetByName(dataBookName)
				isExecuteData = excelObj.getColumn(dataSheet, contacts_isExecute)
				contactNum = 0
				isExecuteNum = 0
				for id, data in enumerate(isExecuteData[1:]):
					if data.value == "y":
						isExecuteNum += 1
						rowContent = excelObj.getRow(dataSheet, id + 2)
						contactPersonName = rowContent[contacts_contactPersonName - 1].value
						contactPersonEmail = rowContent[contacts_contactPersonEmail - 1].value
						isStar = rowContent[contacts_isStar - 1].value
						contactPersonPhone = rowContent[contacts_contactPersonMobile - 1].value
						contactPersonComment = rowContent[contacts_contactPersonComment -1].value
						assertKeyWord = rowContent[contacts_assertKeyWords - 1].value
						print(contactPersonName, contactPersonEmail, assertKeyWord)
						print(contactPersonComment, contactPersonPhone, isStar)
						AddContactPerson.add(driver,
							contactPersonName,
							contactPersonEmail,
							isStar,
							contactPersonPhone,
							contactPersonComment)
						time.sleep(3)
						logging.info(u"添加联系人%s成功" %contactPersonEmail)
						excelObj.writeCellCurrentTime(dataSheet,
							rowNo = id +2 ,colsNo = contacts_runTime)
						try:
							assert assertKeyWord in driver.page_source
						except AssertionError as e:
							excelObj.writeCell(dataSheet, "faild", rowNo = id + 2,
								colsNo = contacts_testResult, style="red")
							logging.info(u"断言关键字%s失败" %assertKeyWord)
					else:
						excelObj.writeCell(dataSheet, "pass", rowNo = id + 2,
							colsNo = contacts_testResult,style="green")
						contactNum += 1
						logging.info(u"断言关键字%s成功" %assertKeyWord)
				print("contactNum = %s, isExecuteNum = %s"\
				      %(contactNum, isExecuteNum))
				if contactNum == isExecuteNum:
					excelObj.writeCell(userSheet, "pass", rowNo = idx + 2,
						colsNo = account_testResult, style="green")
					print(u"为用户 %s添加 %d个联系人，测试通过！"\
						    % (username, contactNum))
				else:
					excelObj.writeCell(userSheet, "faild", rowNo = idx + 2,
						colsNo = account_testResult, style="red")
					logging.info(u"为用户%s添加%d个联系人,%d个成功\n"\
						 % (username, isExecuteNum, contactNum))
			else:
				ignoreUserName = excelObj.getCellOfValue\
					   (userSheet, rowNo = idx + 2, colsNo = account_username)
				logging.info(u"用户%s被为忽略执行！,"%ignoreUserName)
			driver.quit()
	except Exception as e:
		logging.debug(u"异常信息: %s"\
			%str(traceback.format_exc()))

				      		




if __name__ == '__main__':
	#testMailLogin()
	test126MailAddContacts()
	print(u"登陆126邮箱成功")		