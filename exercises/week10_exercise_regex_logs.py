'''
Monday Morning Exercise:

Below are two lines of text from web log files:

line1 = '204.249.225.59 - - [28/Aug/1995:00:00:34 -0400] "GET /pub/rmharris/catalogs/dawsocat/intro.html HTTP/1.0" 200 3542\n'

line2 = 'access9.accsyst.com - - [28/Aug/1995:00:00:35 -0400] "GET /pub/robert/past99.gif HTTP/1.0" 200 4993\n'

Question: What regex pattern would you use to extract the following parts:
- url/host
- date and time
- action/method (i.e. 'GET')
- uri
- status
- data

Example output:
[('cssu24.cs.ust.hk', '28/Aug/1995:00:00:39', 'GET', '/pub/job/vk/view18.jpg HTTP/1.0', '200', '6578\n')]
'''

#hints
# s+ == white spaces
# capture items between []
#([^ ]+) capture single character not present in the list
# https://regex101.com/


# Thanks Chris
# Does not separate method  
print(re.findall('([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+)' "(.*\n)", line1))
print(re.findall('([a-zA-Z0-9\.\-\_]+) - - \[(.*?)\] "(.*?)" (\d+)' "(.*\n)", line2))


#Thanks Paul
#non regex method
def cleaner(line):
    final = []
    tmp = line.split()
    tmp2 = tmp[6] + ' ' + tmp[7][:-1]
    final.append((tmp[0],tmp[3][1:], tmp[5][1:], tmp2, tmp[8], tmp[9]))
    print final


#Solution 1 - Total
import re

my_regex = '^([^ ]+)\\s+-\\s+-\\s+\\[([^\\]]+)\s+-0400\\]\\s+\\"([^ ]+)?\\s+([^\\"]+)\\s*.*?\\"\\s+([^ ]+)\\s+([^ ]+)'
re.findall(my_regex, line1)

#Solution 1a - parse the url/host

pattern = '^([^ ]+)\\s+-\\s+-\\s+'
assert(re.findall(pattern, line1) == ['204.249.225.59'])
assert(re.findall(pattern, line2) == ['access9.accsyst.com'])


#Solution 1b - parse the date and time
pattern = '\\[([^\\]]+)\s+-0400\\]'
assert(re.findall(pattern, line1) == ['28/Aug/1995:00:00:34'])
assert(re.findall(pattern, line2) == ['28/Aug/1995:00:00:35'])



