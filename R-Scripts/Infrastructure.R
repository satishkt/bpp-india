######--------Infrastructure to handle the many categories and days-------------######
#we first start off by just doing the prices from the consecutive days

#------data setup------#

setwd("C:/Users/Nitin/Desktop")
bpp_current<-read.csv("bpp_just_scrapped.csv")

###---Ordering by date to get the cpi calculation in the correct order---###
bpp_current1<-bpp_current[order(as.Date(bpp_current$date, format="%d/%m/%Y")),]

#Unique categories
cats<-as.character(unique(bpp_current1$category))
write.csv(cats, "C:/Users/Nitin/Desktop/cats3.csv")

#too many categories to do in R - went to excel to make the mapping

#Loading in the cpi_mapping file to place categories in the proper buckets for analysis
cpi_mapping<-read.csv("cpi_mapping_3.csv")
cpi_mapping$cpi_bucket<-as.character(cpi_mapping$cpi_bucket)
cpi_mapping$category<-as.character(cpi_mapping$category)


#-----------------------#
#Next, we create a table that holds the averages of the items for each category over time

categories<-as.character(unique(bpp_current1$category))


storage<-data.frame(categories)
storage$categories<-as.character(storage$categories)

for (k in 1:length(unique(bpp_current1$date))) {
  for (j in 1:length(categories)) {
    storage[j,k+1]<-mean(as.numeric(as.character(bpp_current1$price_2[bpp_current1$category==categories[j] & bpp_current1$date==as.character(unique(bpp_current1$date)[k])])))
  }
}

#Note - this creates values with NaN - this is because not all goods may have been collected on a given day

#-----------------------#
#aggregate one more time to just get total values for the 3 buckets we have

storage$bucket<-cpi_mapping$cpi_bucket

buckets<-unique(cpi_mapping$cpi_bucket)
storage2<-data.frame(buckets)
storage2$buckets<-as.character(buckets)

for (k in 1:length(unique(bpp_current1$date))) {
  for (j in 1:length(buckets)) {
    storage2[j,k+1]<-sum(na.omit(storage[storage$bucket==storage2$buckets[j],k+1]))
  }
}

View(storage2)
