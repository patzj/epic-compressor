import os
import sys
import magic
from PIL import Image

ACCEPTED = ['image/jpg', 'image/jpeg']
MIME = magic.Magic(mime=True)

def main():
    try:
        print 'starting compression'
        path = os.path.abspath(sys.argv[1])
        traverse(path)
    except Exception as e:
        sys.stderr.write(e)
        sys.exit(e.errno)
    else:
        print 'done'

def traverse(path):
    listdir = os.listdir(path)
    for i in listdir:
        current = os.path.abspath(os.path.join(path, i))
        if os.path.isdir(current):
            traverse(current)
        else:
            if os.path.exists(current) and \
                os.path.isfile(current) and \
                MIME.from_file(current) in ACCEPTED:

                print 'compressing ' + i
                im = Image.open(current)
                im.save(current, optimize=True, quality=75)

if __name__ == '__main__':
    main()
