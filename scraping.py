import urllib2,os,url
import  validators
from BeautifulSoup import BeautifulSoup

"""
	# About
	Creator : Dion Ajie
	Location : Bandung, Indonesia
	Mail : mail@dionajie.com


	# Depedencies
	pip install urllib2
	pip install validators
	pip install BeautifulSoup
	pip install url


	# Bug (Update Soon!)
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
	print 'downloading %s/%s' %(path,filename)
	if not os.path.exists(pathfolder+path):
	    os.makedirs(pathfolder+path)

	try: 
		print str(url)+str(content)
		res = urllib2.urlopen(str(url)+str(content))
		print "download ",content
		with open(pathfolder+path+'/'+filename, "wb" ) as file:
			file.write(res.read())
	except urllib2.HTTPError, e:
		print e
	
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

	# get content page
	soup = BeautifulSoup(webContent)

	#get css
	print "\ncss------"
	for css in soup.findAll("link"):
		if "stylesheet" in css.get("rel", []):
			if css["href"][-4:] == '.css' and not validators.url(css["href"]):
				download(css['href'])
		# exceot stylesheet
		elif(css.get("rel", [])):
			download(css['href'])

	#get js
	print "\njs------"
	for js in soup.findAll("script"):
		if js["src"][-3:] == '.js' and not validators.url(js["src"]):
			download(js["src"])

	#get images URL
	print "\nimages------"
	for image in soup.findAll("img"):
		download(image["src"])

	# check font-awesome/fonts
	if os.path.exists(pathfolder+'font-awesome/'):
		print "\nFont Awesome------"
		if not os.path.exists(pathfolder+'font-awesome/fonts'):
			os.makedirs(pathfolder+'font-awesome/fonts/')
		FAfiles = ['FontAwesome.otf', 'fontawesome-webfont.eot', 'fontawesome-webfont.svg', 'fontawesome-webfont.ttf', 'fontawesome-webfont.woff', 'fontawesome-webfont.woff2' ]
		url = 'https://github.com/FortAwesome/Font-Awesome/blob/master/fonts/'
		for content in FAfiles:
			res = urllib2.urlopen(str(url)+str(content)+'?raw=true')
			print "download ",content
			with open(pathfolder+'font-awesome/fonts/'+content, "wb" ) as file:
				file.write(res.read())

	print "\nComplete"


if __name__ == '__main__':
	url = 'http://blackrockdigital.github.io/startbootstrap-creative/' #URL Page
	filenamePage = 'index'	# HTML File name
	pathfolder = 'startbootstrap/'	# Folder to save files
	scrapPage(url,filenamePage,pathfolder)