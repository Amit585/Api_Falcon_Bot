import re

txt = "A1ere"
# x = re.search("^The.*Spain$", txt)
x=re.search("([A-Z][1-5])\w+",txt)
print(str(x))