
install.packages("readr")
library(readr)

##### to use association rules we need package "arules" foe apriori algorithm

install.packages("arules")
library("arules")

book <- read.csv(file.choose())
View(book)

## inspect(book) # showing only top 10 transactions

class(book) 

summary(book)

##### using apriori algorithm

arules <- apriori(book, parameter = list(support = 0.002, confidence = 0.75, minlen = 2))
arules

##### Viewing rules based on lift value

inspect(head(sort(arules, by = "lift"))) # to view we use inspect 

##### Overal quality 

head(quality(arules))

##### for visualizing rules

install.packages("arulesViz")
library("arulesViz") 

###### Different Ways of Visualizing Rules

plot(arules)

windows()
plot(arules, method = "grouped")

###### for good visualization try plotting only 10 rowls

plot(arules[1:10], method = "graph") 

write(arules, file = "book.csv", sep = ",")

getwd()
