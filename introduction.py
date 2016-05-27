from bs4 import BeautifulSoup
soup = BeautifulSoup(open("sample.html"))

print soup.prettify()
#gives the html document in prettified manner

print(soup.get_text())
#prints text of the page

print type(soup)
#<class 'bs4.BeautifulSoup'>

print soup.title
# <title>The Dormouse's story</title>

print soup.title.name
# u'title'

print soup.title.string
# u'The Dormouse's story'

print soup.title.parent.name
# u'head'

print soup.p  #gives first p tag
# <p class="title"><b>The Dormouse's story</b></p>

print soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print soup.p['class']
# u'title'

#Not done till yet :

print soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
