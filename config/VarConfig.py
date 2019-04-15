#encoding=utf-8
import os
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pageElementLocatorPath = parentDirPath + u"\\config\\pageElementLocator.ini"

dataFilePath = parentDirPath + u"\\126邮箱联系人.xlsx"

account_username = 2
account_password = 3
account_dataBook = 4
account_isExecute = 5
account_testResult = 6

contacts_contactPersonName = 2
contacts_contactPersonEmail = 3
contacts_isStar = 4
contacts_contactPersonMobile = 5
contacts_contactPersonComment = 6
contacts_assertKeyWords = 7
contacts_isExecute = 8
contacts_runTime = 9
contacts_testResult = 10



