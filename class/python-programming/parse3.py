import fileinput, sys

def get_ingredients(paths):
    out = []
    for line in fileinput.input(paths):
        if line.startswith('#'):
            continue
        out.append( line.rstrip() )        # zap trailing newline
    return out

def main(paths):
    for ing in get_ingredients(paths):
        key,value = ing.split('=')
        key = key.strip()
        value = value.strip()
        if key == 'title':
            print '*'*5, value, '*'*5
        words = value.split()
        print '{:<8}\t{}'.format( ' '.join(words[:-1]), words[-1] )

if __name__=='__main__':
    main(sys.argv[1:])
