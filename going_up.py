from bs4 import BeautifulSoup
soup = BeautifulSoup(open("sample.html"))
title_tag=soup.title

print title_tag.parent
# <head><title>The Dormouse's story</title></head>

link=soup.a
for parent in link.parents:
    print parent.name
#Here link.parents is a generator

