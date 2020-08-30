import urllib

import xml.etree.ElementTree as ET
url = input('Enter-')
u = urllib.open(url)
data = u.read()
tree = ET.formstring(data)
results = tree.findall('comments/comment')
count = 0
sum = 0
for i in results:
    x = int(i.find('count').text)
    count = count+1
    sum += x
print(sum)