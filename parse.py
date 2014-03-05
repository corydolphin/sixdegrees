import gzip, os, re



MAGIC_START_STRING = '----\t\t\t------'

actor_reg = re.compile('([^\t]*)\t*(.*)', re.UNICODE) # Regex to match actorname and movie information, from Allen Downey
title_reg = '([^\(]*)' # Match a title eg. The Last of the Mohicans
date_reg = '\(([^\)]*)\)' # Match a date, eg. (1992)
role_reg = '\[?([^\]]*)?\]?' # Optional, match a role eg. [Himself]
info_reg = re.compile(title_reg + '\s*' + date_reg + '[^\[]*' + role_reg, re.UNICODE) # Regex to match movie info, adopted from Allen Downey
video = re.compile('\(T?V|VG\)', re.UNICODE)


def parseFile(filename):
    with gzip.open(filename, 'rb') as infile:
        line = infile.readline()
        while not MAGIC_START_STRING in line.strip():
            line = infile.readline()

        current_actor = None
        movies = []

        for line in infile:
            line = line.rstrip()
            actor_match = actor_reg.match(line)
            if actor_match:
                actor_name, info = actor_match.groups()
                if actor_name == 'Aguila, Robert':
                    print info
                    print movies
                # skip television shows (titles in quotation marks) 
                if info.startswith('"') or  video.search(info):
                    continue

                if actor_name and actor_name != current_actor:
                    yield current_actor, movies
                    movies = []
                    current_actor = actor_name

                info_match = info_reg.match(info)
                if info_match:
                    title, date, role = info_match.groups()
                    if date == None:
                        continue
                    movies.append((title,date,role))



def download(name):
    actors = urlopen('ftp://ftp.fu-berlin.de/pub/misc/movies/database/%s' % name)
    with open(name, 'wb') as fp:
        shutil.copyfileobj(actors, fp)

def main():
    for filename in 'actors.list.gz', 'actresses.list.gz':
        if not os.path.exists(filename):
            download(filename)

        for actor, movies in parseFile(filename):
            print actor, movies




if __name__ =='__main__':
  main()