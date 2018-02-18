################# apply fisher or LRT to a p-value matrix #########

############ set up the working environment ##################
rm(list  =ls())
workdir ="~/R/Code/IRR Data Science Build/Shiny Apps/CostofLivingProject/real_data_raj_pmatrix"
outdir =paste0(workdir,"output/")
datadir =paste0(workdir,"data/")
codedir =paste0(workdir,"code/")
setwd(workdir)
getwd()

################# source 2 important files ##################
source("~/R/Code/IRR Data Science Build/Shiny Apps/CostofLivingProject/real_data_raj_pmatrix/LRTPois.R")
source("~/R/Code/IRR Data Science Build/Shiny Apps/CostofLivingProject/real_data_raj_pmatrix/pv_comb_funcs.R")

################# read in p-value matrix ########

#infile ="Market_pv_lme_unadjusted"
#raw = read.csv(file = paste0(outdir,infile, ".csv"))

raw = read.csv("Market_pv_lme_unadjusted.csv")

################ check the data ############
summary(raw)

pv.matrix = raw

apply(pv.matrix[-1], 1, function(x){sum(x<0.05)})



################ analyze the p-value matrix##########
####### 1 LRT with 0.1 
# 1 LRT method #######

(pv.lrt = pvm.lrt(pmatrix = data.frame(pv.matrix) , thred = 0.1,N.emp = 10000))

(pv.fisher = pvm.fisher.boot(n.boot= 1000, pmatrix= pv.matrix, epis = 1e-5))
############## write data to file############

#(file0 = "Market_LRT_")
#(fn =paste0(outdir, file0,Sys.Date(),".csv"))
#write.csv(pv.lrt, file= fn, row.names = F)
write.csv(pv.lrt,"Market_LRT.csv",row.names = F)


#(file0 = "Market_Fisher_")
#(fn =paste0(outdir, file0,Sys.Date(),".csv"))
#write.csv(pv.fisher, file= fn, row.names = F)
write.csv(pv.fisher,"Market_Fisher_.csv",row.names = F)




out = merge(pv.lrt,pv.fisher,by=c("Market"))
out1 = out[,c("Market","pv.mlr","pv.fisher")]

# out1= out1[order(out1$pv.fisher),]
write.csv(out1, "Final_P_Value_Test.csv", row.names = F)