import re
from pathlib import Path

file_path = Path('C:\\work\\python\\wenzzel\\python-master\\agmcs\\0004\\test.txt')
with open(file_path) as f:
 data = f.read()

result = re.split(r"[^a-zA-Z]",data)
print (len([x for x in result if x!= '']))
