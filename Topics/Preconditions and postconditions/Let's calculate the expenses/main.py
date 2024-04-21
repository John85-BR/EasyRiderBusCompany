import re

string = input()
template = '(\d+)?( [a-z\s]+ )?\$(\d{1,})'
l = [int(k)   if i != ''  else int(k) for i, j, k in re.findall(template, string)]
print(f"This week you have spent: {sum(l)} dollars")
