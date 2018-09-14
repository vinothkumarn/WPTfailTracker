import os
import xlsxwriter
from os.path import expanduser

def findFailingTests(rootDir ,worksheet):
	count = 0
	row = 1
	col = 0
	temp = ""
	tempmult = ""
	for dirName, subdirList, fileList in os.walk(rootDir):
		for fname in fileList:
			if '.ini' in fname and fname != '__dir__.ini':
				count+=1
				worksheet.write(row,col,count)
				worksheet.write(row,col+1,fname)
				#worksheet.write(row,col+2,dirName.strip(expanduser("~")))
				row+=1
	return count

def findCountofTests(rootDir):
	count = 0
	rootDir = rootDir.replace('/meta/','/tests/')
	for dirName, subdirList, fileList in os.walk(rootDir):
		for fname in fileList:
			if '.html' in fname or '.htm' in fname:
				count+=1
	return count
home = expanduser("~")
rootDir = home+'/src/mozilla-central/testing/web-platform/meta/'
requiredSubdirList = ['content-security-policy','mixed-content','subresource-integrity','cors','x-frame-options','referrer-policy','webauthn','feature-policy','credential-management']
workbook = xlsxwriter.Workbook('failing_wpt_tests.xlsx')
bold = workbook.add_format({'bold': True})
for dirName, subdirList, fileList in os.walk(rootDir,workbook):
	midtemp = dirName
	testcount = 0
	failcount = 0
	if midtemp.replace(rootDir,'') in requiredSubdirList:
		testcount = findCountofTests(dirName)
		worksheet = workbook.add_worksheet(midtemp.replace(rootDir,''))
		failcount = findFailingTests(dirName,worksheet)
		worksheet.write(0,0,midtemp.replace(rootDir,'')+'(failing '+str(failcount)+'/total '+str(testcount)+')',bold)
workbook.close()






