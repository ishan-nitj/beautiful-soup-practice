#There are four kinds of objects in BS:Tag, NavigableString, BeautifulSoup, and Comment
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("sample.html"))

#1)Tag
title_tag=soup.title
print type(title_tag)
#<class 'bs4.element.Tag'>
print title_tag.name
#title 
print title_tag['class']
print title_tag['id']

#Note:We can change name class and id of a tag and it will be refelcted back in html generated by BS but not in original document.
#We can also del class and id .

#2)NavigableString
#A string corresponds to a bit of text within a tag.
print title_tag.string
print type(title_tag.string)
# <class 'bs4.element.NavigableString'>
title_tag.string.replace_with("Hi")
#To replace the string

#3)Beautiful Soup
print type(soup)
#<class 'bs4.BeautifulSoup'>

#4)Comment
#The Comment object is just a special type of NavigableString:
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
print type(comment)
# <class 'bs4.element.Comment'>

