import os
import xlsxwriter
from os.path import expanduser

def findFailingTests(rootDir ,worksheet):
	count = 0
	row = 2
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
requiredSubdirList = [
	'cookies',
	'clear-site-data',
	'content-security-policy',
	'cors',
	'credential-management'
	'feature-policy',
	'fetch',
	'mixed-content',
	'mimesniff',
	'referrer-policy',
	'subresource-integrity',
	'webauthn',
	'x-frame-options',
]

workbook = xlsxwriter.Workbook('failing_wpt_tests.xlsx')
bold = workbook.add_format({'bold': True})
overviewsheet = workbook.add_worksheet('Overview')
overviewsheet.write(0, 0, 'Testname', bold)
overviewsheet.write(0, 1, 'Tests', bold)
overviewsheet.write(0, 2, 'Failures', bold)
overviewsheet.write(0, 3, 'Percentage', bold)
row = 0
for dirName, subdirList, fileList in os.walk(rootDir,workbook):
	testdir = dirName.replace(rootDir, '')
	testcount = 0
	failcount = 0
	if testdir in requiredSubdirList:
		row += 1
		testcount = findCountofTests(dirName)
		worksheet = workbook.add_worksheet(testdir.replace(rootDir,''))
		failcount = findFailingTests(dirName, worksheet)
		worksheet.write(0, 0, 'Testname', bold)
		worksheet.write(0, 1, 'Tests', bold)
		worksheet.write(0, 2, 'Failures', bold)
		worksheet.write(1, 0, testdir)
		worksheet.write(1, 1, testcount)
		worksheet.write(1, 2, failcount)
		overviewsheet.write(row, 0, testdir)
		overviewsheet.write(row, 1, testcount)
		overviewsheet.write(row, 2, failcount)
		print testdir, testcount, failcount
workbook.close()






