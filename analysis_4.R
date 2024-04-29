## STANDARDIZE ALL DATA
library(tidyverse)
library(skimr)
library(lubridate)
library(readr)
library("corrplot")
library("psych")
features <- read_csv("Analysis/Features-data-set_1_-_2_.csv")
features1 <- features %>% drop_na(CPI)
Temp <- c((features1$Temperature-mean(features1$Temperature))/sd(features1$Temperature))
CPI <- c((features1$CPI-mean(features1$CPI))/sd(features1$CPI))
fuel_price <- c((features1$Fuel_Price-mean(features1$Fuel_Price))/sd(features1$Fuel_Price))
z <- data.frame(fuel_price,CPI,Temp)
cor_matrix <- cor(z)
corrplot(cor_matrix, method = "color")
cor.test(z$Temp,z$CPI)
cor.test(z$fuel_price,z$CPI)
##print corresponding p-values as well..----done
## print graphs of Temp Vs CPI and Fuel Vs CPI