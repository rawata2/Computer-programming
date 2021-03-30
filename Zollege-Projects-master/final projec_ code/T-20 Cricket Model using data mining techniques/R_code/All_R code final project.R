#******************************************************************************************************************************************************
#                                     Start of the code
#Author: kuldeep Rawat
#******************************************************************************************************************************************************

#set working directory
setwd("C:/Users/kuldeep/Desktop/Software Project/New Rcode")

#Read this file all the time
mydataN <- read.csv("Final_cric.csv")

#Installing Libraries 
install.packages("fitdistrplus")
install.packages("e1071")
install.packages("mice")
install.packages("ggplot2")
install.packages("ggthemes")
install.packages("scales")

#loading library
library("fitdistrplus")
library(e1071)
library(ggplot2)
library(ggthemes)
library(scales)
library(Hmisc)

#******************************************************************************************************************************************************
#                       Data Explore
#******************************************************************************************************************************************************

#Read the merged file. 
#mydata <- read.csv("MergedN.csv") #first time use only

head(mydata)

##column names
colnames(mydata)

# clean.
summary(mydata)
str(mydata)
any(is.na(mydata))

# Pattern of missing values
library(mice)
md.pattern(mydataN)  # pattern or missing values in data.

# remove unwanted columns
rem <- mydata[ , -(c(1,11,12,15,17,23,24,27,28,41))]

#checking the removed coulmns 
colnames(rem)

write.csv(rem, file="Final_cric.csv", row.names = F, na = " ")


#mydataN <- read.csv("Final_cric.csv") # read this

#checking colnames again
colnames(mydataN)

#plot to see data of coulmn, matches played
polygon(density(mydataN$Team_Matches_Played), col="blue")
polygon(density(mydataN$Matches_Won), col="blue")

#Cullen and Frey graph
descdist(mydataN$Matches_Won)
plot(as.numeric(mydataN$Team_Matches_Played))

#plot rating, points and Matches won
plot(density(mydataN$Points))
plot(density(mydataN$Rating))
plot(density(mydataN$Matches_won))

#scatter plot
scatter.smooth(x=mydataN$Team_Matches_Played, y=mydataN$Matches_Won,z= mydataN$Country,xlab="Matches Played", ylab = "Matches won", main="Matches won ~ Matches Played")

# help to eliminate outliers
impute(mydataN$Rating, mean)  # replace with mean
impute(mydataN$Rating, median)  # median

# ggplots to see macth winner and opposition
ggplot(mydataN, aes(x = Country, fill = factor(Opposition))) +
  geom_bar(stat = 'count', position = 'dodge') +
  labs(x = 'Country') +labs(y= '')
  theme_few()

ggplot(mydataN, aes(x = Country, fill = factor(Win_outcome))) +
  geom_bar(stat = 'count', position = 'dodge') +
  labs(x = 'Country') +labs(y= 'Matches')
  theme_few()


#******************************************************************************************************************************************************
#                       Multi Linear Regression
#******************************************************************************************************************************************************
#read data 
#check names
names(mydataN)

#check correlation between attributes
cor(mydataN[c("Country_N", "Matches_Won", "Points","Rating")]) 
pairs(mydataN[c("Country_N", "Matches_Won", "Points","Rating" )]) 

# create the model
MLR <- lm(Country_N ~ Matches_Won + Points + Rating+ Target + Ground, data=mydataN)

#display the result
MLR

# Check residuals
mydataN.stdRes = rstandard(MLR)
plot( mydataN.stdRes, col="blue")
abline(0,0)

#normality
qqnorm(mydataN.stdRes,ylab="Standardized Residuals",xlab="Normal Scores", main="Normality Plot", col="green")
qqline(mydataN.stdRes)

summary(MLR)

#******************************************************************************************************************************************************
#                       Decision Tree
#******************************************************************************************************************************************************


# Decision Tree Code
install.packages("rpart")
install.packages("rpart.plot")
install.packages("party")
library(party)
require(rpart)
require(rpart.plot)

# lets look at it structuer of the data
str(mydataN)

normalize <- function(x) { return((x - min(x)) / (max(x)-min(x)))}
normalize(c(1,2,3,4,5))
normalize(c(10,20,30,40,50))

barplot(prop.table(table(mydataN$Win_outcome)),
        col = rainbow(2),
        ylim = c(0, 0.7),
        main = "Class Distribution")

library(e1071)
smodel <-svm(mydataN$Win_outcome)
summary(smodel)
table(mydataN$Win_outcome)

# randomize first
set.seed(1234) # sync the randomization / allows reproducibility
pd <- sample(2, nrow(mydataN),replace = TRUE, prob = c(0.8,0.2))
train <- mydataN[pd==1,] 
test <-mydataN[pd==2,] 

# install and load the C5.0 library
install.packages("C50")
library("C50")

#Converting it into factor
mydataN$Win_outcome<-as.factor(mydataN$Win_outcome)
str(mydataN$Win_outcome)

# train the model
colnames(mydataN)
cmodel <-C5.0(train[6], train$Win_outcome)
summary(cmodel)

modelc = rpart(Win_outcome ~ Country, data=mydataN[1:8000,], method="class")
modelc

# Decision with rpat
modelc <- rpart(Win_outcome ~ Country + Rating + Points + Team_Matches_Played, data=mydataN)

library(rpart.plot)
rpart.plot(modelc,extra = 5)

# test the model
nmodel = as.factor(predict(cmodel, test) ) 
nmodel
# evaluation
install.packages("gmodels")
library("gmodels")

# CrossTable with all details
CrossTable(test$Win_outcome, nmodel) 


# CrossTable that is a lot clearer
CrossTable(test$Win_outcome, nmodel, prop.chisq = FALSE, prop.c 
           = FALSE, prop.r = FALSE, dnn =c('actual', 'predicted'))

########################################
    #Performing again for improvement
########################################

# train another model, but this time a series of models
trainm = C5.0(train[6], train$Win_outcome, trials = 15)
trainm

# test the models
testm = predict(trainm, test) 

# evaluate this now
CrossTable(test$Win_outcome, testm, prop.chisq = FALSE, prop.c = 
             FALSE, prop.r = FALSE, dnn =c('actual', 'predicted'))


#******************************************************************************************************************************************************
#                      Code Refrences 
#******************************************************************************************************************************************************
