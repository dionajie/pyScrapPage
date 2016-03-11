import urllib2,os,url,re,validators
from BeautifulSoup import BeautifulSoup


"""
	# About
	Creator : Dion Ajie
	Location : Bandung, Indonesia
	Mail : mail@dionajie.com


	# Package to install
	pip install urllib2
	pip install validators
	pip install BeautifulSoup
	pip install url


	# TO DO
	- download image in inline style
	- download images in css
	- download font in css or any files related

	# Warning
	Use this app wisely. 
	It is your responsibility to use this app

"""

def download(content):

	filename = content.rsplit('/', 1)[-1].encode('unicode-escape')
	path = content.rsplit('/', 1)[:-1][0].encode('unicode-escape')
	print 'Download %s' %(filename)
	if not os.path.exists(pathfolder+path):
	    os.makedirs(pathfolder+path)

	try: 
		print 'File from ', str(url)+str(content)
		res = urllib2.urlopen(str(url)+str(content))
		print "Download complete. Save to %s \n" %(content)
		with open(pathfolder+path+'/'+filename, "wb" ) as file:
			file.write(res.read())
	except urllib2.HTTPError, e:
		print e


	return pathfolder+path+'/'+filename

def getInsideCSS(path):
	print "\ninside css -------------"
	with open(path, "r") as f:
		content = f.read()

	path = path.split('/', -1)[:-1]
	path = '/'.join(path)
	path = path.split('/', 1)[1]
	print path

	match =  re.findall('url\((.*?)\)',content)
	for row in match:
		print row
		if '..' in row:
			rowAfter = row.split('/', 1)[-1]
			rowAfter = rowAfter.replace("'","")
		else:
			rowAfter = path+'/'+row
			rowAfter = rowAfter.replace("'","")
		rowAfter = rowAfter.split('?', 1)[0]
		print rowAfter
		download(rowAfter)


def getCSS(soup):
	# get css
	print "\n css------"
	for css in soup.findAll("link"):
		if "stylesheet" in css.get("rel", []):
			if css["href"][-4:] == '.css' and not validators.url(css["href"]):
				print css['href']
				result = download(css['href'])
				print result
				getInsideCSS(result)
		# exceot stylesheet
		elif(css.get("rel", [])):
			result = download(css['href'])
		
	print "end of css ----------"

def getJS(soup):
	#get js
	print "\njs------"
	for js in soup.findAll("script"):
		if js["src"][-3:] == '.js' and not validators.url(js["src"]):
			download(js["src"])
	print "end of js ----------"

def getImages(soup):
	#get images URL
	print "\nimages------"
	for image in soup.findAll("img"):
		print image["src"]
		download(image["src"])
	print "end of images ----------"

def getFontAwesome(pathfolder):
	# check font-awesome/fonts
	if os.path.exists(pathfolder+'font-awesome/'):
		print "\nFont Awesome------"
		if not os.path.exists(pathfolder+'font-awesome/fonts'):
			os.makedirs(pathfolder+'font-awesome/fonts/')
		FAfiles = ['FontAwesome.otf', 'fontawesome-webfont.eot', 'fontawesome-webfont.svg', 'fontawesome-webfont.ttf', 'fontawesome-webfont.woff', 'fontawesome-webfont.woff2' ]
		url = 'https://github.com/FortAwesome/Font-Awesome/blob/master/fonts/'
		for content in FAfiles:
			res = urllib2.urlopen(str(url)+str(content)+'?raw=true')
			print "\nDownload  %s" %(content)
			print "File from %s" %(str(url)+str(content))
			with open(pathfolder+'font-awesome/fonts/'+content, "wb" ) as file:
				file.write(res.read())
				print 'Download Complete. Save to %s/font-awesome/fonts/%s' %(pathfolder,content)
	print "end of font-awesome ----------"


def scrapPage(url,filenamePage,pathfolder):

	if not os.path.exists(pathfolder):
		os.makedirs(pathfolder)

	# request page
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)

	# get HTML content
	webContent = response.read()

	# save page
	f = open(pathfolder+filenamePage+'.html', 'w')
	f.write(webContent)
	f.close

	# create report 
	report = 'url : '+str(url)+'\n'
	f = open(pathfolder+'report.txt', 'w')
	f.write(report)
	f.close

	# get content page
	soup = BeautifulSoup(webContent)
	# getCSS(soup)
	getJS(soup)
	getImages(soup)
	getFontAwesome(pathfolder)

	# update report 
	with open(pathfolder+"report.txt", "r+") as f:
		old = f.read()
		f.seek(0) 
		f.write(old+"\nstatus : complete")

	print "\nComplete"


if __name__ == '__main__':
	url = 'http://premiumlayers.com/demos/vcard/' #URL Page
	filenamePage = 'index'	# HTML File name
	pathfolder = 'vcard/'	# Folder to save files
	scrapPage(url,filenamePage,pathfolder)