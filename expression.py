import re
tem = "The rain in Spain"
x = re.search("^The.*Spain$", tem)
print(x)