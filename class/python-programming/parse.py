lines = open('oldfashioned.dat').readlines()

for line in lines:
    if line.startswith('#'):
        continue
    line = line.rstrip()        # zap trailing newline
    key,value = line.split('=')
    if key == 'title':
        print '*'*5, value, '*'*5
        continue
    print value
