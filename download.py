from urllib2 import urlopen
import shutil



actors = urlopen('ftp://ftp.fu-berlin.de/pub/misc/movies/database/actors.list.gz')


with open('actors.list.gz', 'wb') as fp:
    shutil.copyfileobj(actors, fp)


actresses = urlopen('ftp://ftp.fu-berlin.de/pub/misc/movies/database/actresses.list.gz') 

with open('actresses.list.gz', 'wb') as fp:
    shutil.copyfileobj(actresses, fp)
