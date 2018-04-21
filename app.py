import os
import sys
import json
import magic
from PIL import Image

cfg = {}
mime = None

def main():
    try:
        print 'starting compression'
        src = os.path.abspath(sys.argv[1])
        dest = os.path.abspath(sys.argv[2])

        if not os.path.exists(dest):
            os.mkdir(dest)
        traverse(src, dest)
    except Exception as e:
        sys.stderr.write(e)
        sys.exit(e.errno)
    else:
        print 'done'


def load_cfg():
    with open('config.json', 'r') as fin:
        return json.load(fin)


def traverse(src, dest):
    listdir = os.listdir(src)
    for i in listdir:
        curr_src = os.path.abspath(os.path.join(src, i))
        curr_dest = os.path.abspath(os.path.join(dest, i))
        if os.path.isdir(curr_src):
            if not os.path.exists(curr_dest):
                os.mkdir(curr_dest)
            traverse(curr_src, curr_dest)
        else:
            if os.path.exists(curr_src) and \
                os.path.isfile(curr_src) and \
                mime.from_file(curr_src) in cfg['accepted']:

                print 'compressing %s -> %s' % (curr_src, curr_dest)
                im = Image.open(curr_src)
                im.save(curr_dest, optimize=True, quality=cfg['quality'])

if __name__ == '__main__':
    cfg = load_cfg()
    mime = magic.Magic(mime=True)
    main()
