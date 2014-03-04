import gzip


def parseFile(filename):
    with gzip.open(filename, 'rb') as infile:
        line = infile.readline()
        while not "THE ACTORS LIST" in line:
            line = infile.readline()        
        while line:
            line = infile.readline()
            print line

def main():
    parseFile('actors.list.gz')
    # parseFile('actors.list.gz')



if __name__ =='__main__':
  main()