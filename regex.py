import re
sum = 0
fname = 'regex_test.txt'
a = open(fname).read()
pri = re.findall('[0-9]+',a)
for num in pri:
    sum+=int(num)
print(sum)