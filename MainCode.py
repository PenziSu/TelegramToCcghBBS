import urllib2
from bs4 import BeautifulSoup
import json
import shlex
url="https://api.telegram.org/bot239286896:AAHslOboDCVFX0NARtR_qyeBsbN9OmWtg8M/getMe"
page = urllib2.urlopen(url)

resp = page.read()

#contant = json.dumps(contant, sort_keys=True, indent=4, separators=(',',':'))
#print (contant)

#print dict(token.split(':') for token in shlex.split(resp))
