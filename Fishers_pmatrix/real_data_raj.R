########### code for Raj's data on 02/13/2018 by JX########


################# set up environment #################
rm(list  =ls())
workdir ="M:/BIMO/"
outdir =paste0(workdir,"output/")
datadir =paste0(workdir,"data/market_raj/")

setwd(workdir)

getwd()


#################### input original file ##################
infile = "p_matrix"

raw = read.csv(file = paste0(datadir,infile, ".csv"))


tmp0 = seq(from =3, to = 114, by =4)
varlist =colnames(raw)[tmp0]
######## 28 variables to analyze independently ##########


lme.dersi=function(j){
  (var = varlist[j])
  d.0 = raw[,c(tmp0[j], tmp0[j]+1, tmp0[j]+2)]
  
  na.row0 =unique(which(is.na(d.0),arr.ind=TRUE)[1])

  if (!is.na(na.row0)){
    
    d.1 = na.omit(d.0)
    ni = raw$Response[-c(na.row0)]
    market.name = raw[-c(na.row0),1]
  }else{
    d.1 = d.0
    ni = raw$Response
    market.name = raw[,1]
  }
 

  
  
  ########simple estiamte of standard deviation of market i#######
  si= (d.1[,2] - d.1[,3])/4
  
  yidot  = d.1[,1]
  
  ######################################

  
  
  I =length(yidot)
  ydotdot = sum(ni*yidot)/sum(ni)
  
  
  ########################################################################################
  mse = sum((ni-1)*si^2)/sum(ni-1)
  msb = sum(ni*(yidot - ydotdot)^2)/(I-1)
  

  
  ###################### method 2) DerSimonian approach to estimate tau2, sigma2, and muh ###############
  ######### if min = max, use smallest si ###############
  si[si == 0] = min(si[si!=0])
  wi = 1/si^2
  

  c0 = sum(wi) - sum(wi^2)/sum(wi)
  df = I -1
  
  ydotdots = sum(wi*yidot)/sum(wi)
  
  q0 =sum(wi*(yidot - ydotdots)^2)
  
  tau2 = ifelse(q0>df,(q0 - df)/c0,0)
  
  sigma2 = mse
  
  wis = 1/(si^2 + tau2)
  muh = sum(wis*yidot)/sum(wis)
  
  
  ############################# method 1 ) anova approach to estimate tau2, sigma2, and muh, if dersimonian has tau2=0 use anova #####################
  
  if (tau2 == 0){
    n0 = ((sum(ni))^2 -sum(ni^2))/((I-1)*sum(ni))
    tau2 = (msb - mse)/n0
    sigma2 = mse
    muh = ydotdot
  }

  
  
  ###################### values required to calcualte p-values are : yidot, tau2, sigma2, ni, muh#########
  
  #####################################  calculate the p-values #########
  
  sig2 = tau2 + sigma2/ni
  
  z.score= (yidot - muh)/sqrt(sig2 )
  ##################### two-sided p-value ##############
  pv  = 2*pnorm(q = abs(z.score),lower.tail = F)
  
  ############ p-value adjustment ###################
  # pv.adj = p.adjust(pv, method = "BH")
  
  ########################################################
  
  ################### merge to the market name ###########
  

  
  
  dd = data.frame(market.name,pv)
  market.name.all = raw[1]
  res = merge(market.name.all,dd, by.x = "Market",by.y="market.name", all = T)
  
  ############ sorted ################
  res  = res[order(res$Market),]
  return(res)
  # sum(pv<0.05)
  # sum(pv.adj<0.05)
 }



################### start analysis ####################
market.name.all = sort(raw$Market)

out = NULL
for (i in 1:length(tmp0)){
  
  print(i)
  res = lme.dersi(j = i)
  out = cbind(out,res$pv)
}

out0 = cbind(levels(market.name.all), out)
colnames(out0) = c("Market", varlist)

################## write the result to the file #############

file0 = "Market_pv_lme_unadjusted"
(fn =paste0(outdir, file0,Sys.Date(),".csv"))
write.csv(out0, file= fn, row.names = F)




#Fisher's takes pij (uniform - distribution); when transform - 2 log(pij); 2dfs of freedom (you get p-value) 
#when you combine chi-square you can add df's - get tail area of this chi square 
#tests not only one value if significant, but you compare all rows 
#assume all rows have similar risk (RR); in my case you assume homogenous RRi's are same 
#RR - tail probabilities under chi square  - based on p-value of chi square

#Max-Min / SD -> within market variability

#Bootstrap -> you have rri for each row; under null hypothesis -> rri's are the same
#testing at least 1 rri is different than the rest
#Max of RRI's = Test statistic
#Distribution of RRi's , you bootstrap - with replacement, everytime you can calculate maximum rri 
#(same value can get placed in sample)

#RR value with the maximum threshold (upper 95%tile of distribution) "Called Threshold Value"
#Now look at data Value RR, and see which ones are greater than the threshold value - essentially are the ones you care about
#Null hypothesis ; if largest is greater than threshold then you reject the null hypothesis
#This gives you all the sites that are signals

##You want to test if all rri's are equal##

#Fishers Controls type 1 error to be 2.5 for all sites; globally 


#LRT converts all pij to 0 and 1 , if they are signficant they are 1
#It takes how many 1's you have, assumes poisson model, then apply LRT method to 0 and 1 counts

#leave the first si, and sum all other rows
#si  observed values   
#smi calc pvalue   
#  chi squared greater than si 
#  chi squared greater than smi  
#  pi    
#  pmi   
#  pi/pmi    
#  pi / 1- pmi   
#  pmi/pi    
