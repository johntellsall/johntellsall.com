for line in open('oldfashioned.dat'):
    if line.startswith('#'):
        continue
    line = line.rstrip()        # zap trailing newline
    key,value = line.split('=')
    key = key.strip()
    value = value.strip()
    if key == 'title':
        print '*'*5, value, '*'*5
        continue
    words = value.split()
    print '{:<8}\t{}'.format( ' '.join(words[:-1]), words[-1] )
