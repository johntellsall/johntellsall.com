http://stackoverflow.com/questions/24878174/how-to-count-digits-letters-spaces-for-a-string-in-python/24878232#24878232


To make it fast, consider using itertools.imap() like this: 

numbers = sum(imap(str.isdigit, s))

After the initial calls, that will run at C-speed with no pure python
steps and no method lookups. – Raymond Hettinger

vs

s = 'some string'
numbers = sum(c.isdigit() for c in s)
words   = sum(c.isalpha() for c in s)
spaces  = sum(c.isspace() for c in s)
others  = len(s) - numbers - words - spaces
