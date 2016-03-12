# pyScrapPage
Scraping HTML Website Template (include css, js, images) and restructurize folders like original one

### Installation
Download this repository  ``` git clone https://github.com/dionajie/pyScrapPage.git ```

install package using pip
```  sh
pip install urllib2
pip install validators
pip install BeautifulSoup
pip install url

```

### How to
open scraping.py and set variables 

``` sh
url = 'path/to/url'
filenamePage = 'your page filename'
pathfolder = 'path/to/your/folder'
````
Example:
``` sh
url = 'http://blackrockdigital.github.io/startbootstrap-creative/' 
filenamePage = 'index'	
pathfolder = 'startbootstrap/'
```

Then go to your folder path and run this command in terminal
``` sh
python -u scraping.py
```

### TO DO
* download image in inline style

### Warning
Use this app wisely. 
It is your responsibility to use this app
