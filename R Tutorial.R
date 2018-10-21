#Zachary Lyons
#Info 3401
#Friday Problem Set Answers
#Worked with Steven Rothaus, Harold Chang, Lucas Bouchard, and Justin Klemperer

setwd('/Users/Zach/Documents/GitHub/problem-set-7-zjlyons')

titanic_data <- read.csv(file = 'titanic.csv', head=TRUE, sep = ",")

summary(titanic_data)

#Problem 6 
titanic_data$Name
names(titanic_data)
table(titanic_data$Sex)

#Problem 7
names(titanic_data)

table((titanic_data$PassengerId), titanic_data$Survived)

table(titanic_data$Sex)

gender_table <- table(titanic_data$Sex)
gender_proportion <- prop.table(gender_table)

gender_proportion

survived_table <- table(titanic_data$Survived)
survived_proportion <- prop.table(survived_table)

survived_proportion

sex_v_survived_table <- table(titanic_data$Sex, titanic_data$Survived)

prop.table(sex_v_survived_table)

#Problem 8

prop.table(table(titanic_data$Sex, titanic_data$Survived))

prop.table(table(titanic_data$Sex, titanic_data$Survived), 1)

prop.table(table(titanic_data$Sex, titanic_data$Survived), 2)