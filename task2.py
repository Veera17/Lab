# -*- coding: utf-8 -*-
"""
 a temporary script file.
"""
import string
lst=[]
fin=open('/content/mybook1.txt')
for line in fin:
  line=line.split()
  for word in line:
    word=word.strip(string.punctuation + string.whitespace).lower()
    lst.append(word)
print(lst)
print(len(lst))
