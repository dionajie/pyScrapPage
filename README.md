# pyScrapPage
Scraping HTML Website Template (include css, js, images) and restructurize folders like original one.
PyScrapPage is one of apps on challenge list i made. You can read it on [my blog].

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


[my blog] : <https://blog.dionajie.com/python-apps-challenge-1bc71acbdc5f#.tgqxlbw31>