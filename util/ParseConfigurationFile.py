#encoding=utf-8
from configparser import ConfigParser 
import sys
sys.path.append('..')
from config.VarConfig import pageElementLocatorPath

class ParseConfigFile(object):
	"""docstring for ParseConfigFile"""
	def __init__(self):
		self.cf = ConfigParser()
		self.cf.read(pageElementLocatorPath, encoding="utf-8")

	def getItemsSection(self, sectionName):
		optionsDict = dict(self.cf.items(sectionName))
		return optionsDict

	def getOptionValue(self, sectionName, optionName):
		value = self.cf.get(sectionName, optionName)
		return value

if __name__ == '__main__':
	pc = ParseConfigFile()
	print(pc.getItemsSection("126mail_login"))
	print(pc.getOptionValue("126mail_login", "loginPage.frame"))		
		