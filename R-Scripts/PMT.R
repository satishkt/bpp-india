##### Proportional Mass Test Script #####

proportional_mass_test <- function(prices, a,b,c,boot_num) {
  
  #This function takes two inputs: 
  #prices is a numeric vector of the actual price of a given good over many days
  #boot_num is the number of times to replicate at the bootstrapping step
  
  
  #Function to compute price changes from the original prices
  price_diff <- function(prices) {
    y<-c()
    for (j in 1:(length(prices)-1)) {
      y[j]<-prices[j+1]-prices[j]
    }
    return(y)
  }
  
  #Function to find the empirical probability that the price change is within some number z per unit
  within_z <- function(price_diff,z) {
    return(sum(abs(price_diff)<z)/(length(price_diff)*2*z))
  }
  
  #Function to compute the proportional mass for value between 2 specified distances i and j
  pm_ij <- function(price_diff,i,j) {
    return(log(within_z(price_diff,i)/within_z(price_diff,j)))
  }
  
  #Function to compute the Proportional Mass Value for the given distances from 0 (called spread)
  pm<-function(price_diff) {
    #spread<-c(1,2.5,5)
    spread<-c(a,b,c)
    pm_values<-c()
    for (i in spread) {
      for (j in spread) {
        if (i<j) {
          pm_values<-c(pm_values,pm_ij(price_diff,i,j))
        }
      }
    }
    return(((length(pm_values))^-1)*sum(pm_values))
  }
  
  #Computes the p-value by calling all the above functions and bootstrapping with
  #at least 75 percent of the price_changes
  #Here the p-value is the share of pm's that are positive
  boot_sample_size<-ceiling(0.75*length(price_diff(prices)))
  values<-replicate(boot_num,pm(sample(price_diff(prices),boot_sample_size,replace=FALSE)))
  reject_the_null<-values<0
  p_value<-sum(na.omit(reject_the_null))/boot_num
  return(p_value)
  
}


#to pick the appropriate constants for a,b,c, we note that they were 1,2.5,5 when the project
#was done in US. But the dollar to rupee exchange rate is $1 to 50rp, so we let a=50 and keep b and c properly
#in propotion with a=50
misc<-as.numeric((storage2[storage2$buckets=="Misc",][2:(length(storage2[storage2$buckets=="Misc",])-1)]))

a<-50
b<-2.5*a
c<-5*a

proportional_mass_test(misc,a,b,c,1000)
#0

#####
ftb<-as.numeric((storage2[storage2$buckets=="Food, Tobacco, Beverages",][2:(length(storage2[storage2$buckets=="Food, Tobacco, Beverages",])-1)]))
#taking out 0's as before from the days that crawlers did not gather data
ftb<-ftb[ftb>0]

proportional_mass_test(ftb,a,b,c,1000)
#0.947