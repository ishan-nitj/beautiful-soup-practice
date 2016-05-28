from bs4 import BeautifulSoup
soup = BeautifulSoup(open("sample.html"))
#1)Using tag name
#Using a tag name as an attribute will give you only the first tag by that name:
print soup.body.b

#).contents :A tag’s children are available in a list called .contents:
print soup.body.contents
