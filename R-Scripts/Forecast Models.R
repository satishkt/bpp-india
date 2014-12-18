#####-----Forecast Models for BPP------#####
#we first start off by just doing the prices from the consecutive days

#Need to load infrastructure script first so we can access storage2

#-----Time Series Setup-----#
library(forecast)
library(xts)

################# Using 11-23 till Dec 7 to predict Dec 8 til 16 ######################### 

#------------Misc------------#
misc_train<-as.numeric((storage2[storage2$buckets=="Misc",][2:(length(storage2[storage2$buckets=="Misc",])-9)]))

misc_train_ts<-ts(misc_train,start=c(2014, 11,23), frequency=7)
plot(misc_train_ts)

#-----Training Stage-----#

fit_misc<-auto.arima(misc_train_ts, ic="aic") 

forecast(fit_misc,8)
plot(forecast(fit_misc,8))

#-----Testing Stage-----#
#the most recent weeks values
misc_test<-as.numeric((storage2[storage2$buckets=="Misc",][(length(storage2[storage2$buckets=="Misc",])-8):(length(storage2[storage2$buckets=="Misc",])-1)]))
prediction_misc<-as.vector(unlist(forecast(fit_misc,8)[4]))

mse_misc<-mean((misc_test-prediction_misc)^2)
#815312816425

#------------Food,Tobacco,Berverages------------#
ftb_train<-as.numeric((storage2[storage2$buckets=="Food, Tobacco, Beverages",][2:(length(storage2[storage2$buckets=="Food, Tobacco, Beverages",])-9)]))

ftb_train_ts<-ts(ftb_train,start=c(2014, 11,23), frequency=7)
plot(ftb_train_ts)

#-----Training Stage-----#

fit_ftb<-auto.arima(ftb_train_ts, ic="aic") 
forecast(fit_ftb,8)
plot(forecast(fit_ftb,8))

#-----Testing Stage-----#
#the most recent weeks values
ftb_test<-as.numeric((storage2[storage2$buckets=="Food, Tobacco, Beverages",][(length(storage2[storage2$buckets=="Food, Tobacco, Beverages",])-8):(length(storage2[storage2$buckets=="Food, Tobacco, Beverages",])-1)]))
prediction_ftb<-as.vector(unlist(forecast(fit_ftb,8)[4]))

mse_ftb<-mean((ftb_test-prediction_ftb)^2)
#1401565
