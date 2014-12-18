###### ------ CPI AND INFLATION SCRIPT ------ ######


###---Ordering by date to get the cpi calculation in the correct order---###

#Load infrastructure file first so you have storage2

###---CPI Weights---#
#We only have "Food, Tob, Bev", "Clothing and footwear", and "Misc"
#Creating weights for the 3 categories we have

weights<-function(w,N,E) {
  return(w*(1+(E/N)))
}

E<-0.0977+0.0949
N<-1-E
w_ftb<-weights(0.4971,N,E) #0.61568
w_cf<-weights(0.0473,N,E) #0.05858311
w_misc<-weights(0.2912,N,E) #0.3606639

#sanity check
w_ftb+w_cf+w_misc #close enough to 1 - a little off but that's because the input
#weights from the Indian Buerau didn't quite add to 1 either

weight_df<-data.frame(unique(buckets),c(w_ftb,w_misc,w_cf))
colnames(weight_df)<-c("bucket","weight")

weightings<-c()
for (k in 1:length(storage2$bucket)) {
  weightings[k]<-weight_df$weight[is.element(weight_df$bucket,storage2$buckets[k])]
}

  
storage2$weightings<-weightings


###---Now we can actually go through and calculate the cpi---###
#but first we need to define a base period - we take this to be 11/23/2014

#computing the weighted cpi
weighted_basket<-c()
for (k in 1:length(unique(bpp_current1$date))) {
  weighted_basket[k]<-sum(storage2$weightings*storage2[,k+1])
}

cpi<-c()
for (k in 1:length(weighted_basket)-1) {
  cpi[k]<-(weighted_basket[k+1]/weighted_basket[1])*100
}

cpi


#computing inflation

inflation_calculation<-function(x) {
  #x is a a numeric vector (takes in cpi values)
  inflations<-c()
  for (k in 1:(length(x)-1)) {
    inflations[k]<-((x[k+1]-x[k])/x[k])*100
  }
  return(inflations)
}

inflations<-inflation_calculation(cpi)


#Note - when calculating daily inflation it is much more volatile than the monthly numbers we see
