######----------Dip Test-----------#######
#Loading necessary packages
library(diptest)

#Using the storage2 data frame, as this holds the average price changes for the buckets we are considering
#sadly,"Clothing and Footwear" don't have many date past the first few, so a unimodality test
#is useless on them
#also, the 
#Hence, we run the Dip Test (Hartigan) on the two remaing buckets

#First, a useful function to calculate price differences between consecutive days

price_diff <- function(prices) {
  y<-c()
  for (j in 1:(length(prices)-1)) {
    y[j]<-prices[j+1]-prices[j]
  }
  return(y)
}

#---Running the Dip Test for Misc---#
x<-as.numeric(storage2[storage2$buckets=="Misc",][2:(length(storage2[storage2$buckets=="Misc",])-1)])
x<-price_diff(x)

#with linear interpolation
dip.test(x, simulate.p.value=FALSE, B=1000)
#D = 0.0875, p-value = 0.1464
#alternative hypothesis: non-unimodal, i.e., at least bimodal

#with Monte Carlo Methods of simulate p-value
dip.test(x, simulate.p.value=TRUE, B=1000)
#D = 0.0875, p-value = 0.14
#alternative hypothesis: non-unimodal, i.e., at least bimodal

hist(x, xlab="Price differences", main="Distribution of price changes for Misc", breaks=20)

#---Running the Dip Test for Food, Tobacco, Beverages---#
#Note - upon inspection, there were two days that the crawlers were not able to pick up
#any data - so it is likely that this will be at least bimodal

#so we make the following assumption - we assume that if the crawler missed a day, jsut skip that day altogher
#that is, don't use the value of 0 in the computation
#this is necessary, as the with the Indian currecny of rupees it is not uncommon to see prices in the thousands

y<-as.numeric(storage2[storage2$buckets=="Food, Tobacco, Beverages",][2:(length(storage2[storage2$buckets=="Food, Tobacco, Beverages",])-1)])
#dropping the 0's for the reason above
y<-y[y>0]
y<-price_diff(y)

#with linear interpolation
dip.test(y, simulate.p.value=FALSE, B=1000)
#D = 0.0485, p-value = 0.9838
#alternative hypothesis: non-unimodal, i.e., at least bimodal

#with Monte Carlo Methods of simulate p-value
dip.test(y, simulate.p.value=TRUE, B=1000)
#D = 0.0485, p-value = 0.986
#alternative hypothesis: non-unimodal, i.e., at least bimodal

hist(y,xlab="Price differences", main="Distribution of price changes for Food, Tobacco, Beverages", breaks=20)
