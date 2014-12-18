

#diptest package
library(diptest)
vec<-rnorm(200000, mean=0, sd=9)

#calculates the dip statistic
dip(vec,full.result = TRUE, min.is.0 = TRUE)

#to actually do the dip test
dip.test(vec, simulate.p.value=FALSE, B=1000)
#a p-value > 0.05 is suggestive of a unimodal dist

#let's make a crazy example
vec1<-c(rnorm(100, mean=0, sd=1), rnorm(100, mean=12, sd=3), rexp(100,0.1))
dip.test(vec1, simulate.p.value=FALSE, B=1000)

#another one
vec2<-c(rnorm(100,mean=0, sd=1),rnorm(100,mean=10, sd=1),rnorm(100,mean=5, sd=1))
hist(vec2)
dip.test(vec2, simulate.p.value=FALSE, B=1000)

#let's do something a bit more subtle
vec3<-c(rnorm(100,mean=0, sd=1/2),rnorm(170,mean=2, sd=1),rnorm(100,mean=4, sd=1/2),rnorm(100,mean=6, sd=1))
hist(vec3)
dip.test(vec3, simulate.p.value=FALSE, B=1000)


#Note - the dip test is extremeley sensitive to small modes that economists might just chalk up to noise
#ex: 

run_dip <- function( log, boot) {
  result<-0
  d<-dip.test(c(rnorm(100,mean=0, sd=1/2),rnorm(170,mean=2, sd=1),rnorm(100,mean=4, sd=1/2),rnorm(100,mean=6, sd=1)), simulate.p.value=log, B=boot)$p.value
  if (d<0.05) {
    result<-result+1
  } else {
    result<-result
  }
  return(result)
}

sum(replicate(10000,run_dip(FALSE, 1000)))/10000 #0.4481, so pretty sensitive to mild nodes

#this could be an issue for the time series data



