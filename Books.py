# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 14:31:26 2021

@author: User
"""

pip install mlxtend
import matplotlib.pylab as plt
import pandas as pd

from mlxtend.frequent_patterns import apriori, association_rules

books= [] 
with open("F:/Association Rules/Assignment/book.csv") as f:
    books = f.read()
    
books =  books.split("\n")

books_list = []
for i in books:
    books_list.append(i.split(","))
    
allbooks_list = [i for item in books_list for i in item]

from collections import Counter

itemsFrequencies  = Counter(allbooks_list)

itemsFrequencies = sorted(itemsFrequencies.items(), key = lambda x:x[1])

frequenciesbook =list(reversed([i[1] for i in itemsFrequencies]))
itembook = list(reversed([i[1] for i in itemsFrequencies]))

plt.bar(height = frequenciesbook[0:11], x = list(range(0, 11)), color = 'rgbkymc')
plt.xticks(list(range(0, 11), ), itembook[0:11])
plt.xlabel("items")
plt.ylabel("Count")
plt.show()

# Creating Data Frame for the transactions data
books_series = pd.DataFrame(pd.Series(books_list))
books_series = books_series.iloc[:9835, :] # removing the last empty transaction

books_series.columns = ["collections"]

# creating a dummy columns for the each item in each transactions ... Using column names as item name
X = books_series['collections'].str.join(sep = '*').str.get_dummies(sep = '*')

frequent_booksets = apriori(X, min_support = 0.0075, max_len = 4, use_colnames = True)

frequent_booksets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 3)), height = frequent_booksets.support[0:3], color ='rgmyk')
plt.xticks(list(range(0, 3)), frequent_booksets.itemsets[0:3], rotation=20)
plt.xlabel('book-sets')
plt.ylabel('support')
plt.show()


rules = association_rules(frequent_booksets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

