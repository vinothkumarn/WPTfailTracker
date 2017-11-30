import os
import xlsxwriter

rootDir = 'testing/web-platform/meta/'
count = 0
row = 0
col = 0
temp = ""
tempmult = ""
requiredSubdirList = ['content-security-policy','mixed-content','subresource-integrity','cors','x-frame-options','referrer-policy','webauthn','feature-policy','credential-management']
file = open('testing/web-platform/meta/failing_wpt_tests.txt','w+')
workbook = xlsxwriter.Workbook('testing/web-platform/meta/failing_wpt_tests.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
for dirName, subdirList, fileList in os.walk(rootDir):
	if any(x in dirName for x in requiredSubdirList):
		for fname in fileList:
			if '.ini' in fname:
				if dirName != temp:
					print('\t%s\n' % (dirName.replace('testing/web-platform/meta/','')))
					tempdir = dirName.replace('testing/web-platform/meta/','')
					try:
						if(tempdir.index('/')):
							tempdir = tempdir[:tempdir.index('/')]
					except:
						pass
					if tempmult != tempdir:
						file.write('\t%s\n' % (tempdir))
						worksheet.write(row,col,tempdir,bold)
					row+=1
					temp = dirName
					tempmult = tempdir
				count+=1
				print('\t%s/%s' % (dirName,fname))
				file.write('%s,%s/%s\n' % (fname,dirName,fname))
				worksheet.write(row,col,dirName+'/'+fname)
				row+=1
workbook.close()
file.close()
print('\n%s' % count)