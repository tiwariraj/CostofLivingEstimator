############ fisher combination ##########



###################### perform the fisher combination to calcualte rri##########

# pv = p.matrix[,-1]
# lpv = -2*log(pv)


######## func.rri function , options, if opt =0 , only return rri, if opt =1, return the data frame####
func.rri= function(lpv =NULL, opt=0){
  lpv = data.frame(lpv)
  dim0= dim(lpv)
  si = rowSums(lpv, na.rm = T)
  smi = sum(si) - si
  
  ni = apply(lpv,1, function(x){sum(!is.na(x))})
  nmi = sum(ni) - ni
  
  pi = pchisq(q=si,df=2*(ni),lower.tail = F)
  pmi = pchisq(q=smi,df=2*(nmi),lower.tail = F)
  
  rri = (pmi/pi)
  
  if (opt == 0) return(rri)
  if (opt == 1) return(data.frame(si, smi, ni, nmi, pi,pmi, rri))
}

# rri = func.rri(lpv)
# tmp.0= data.frame(p.matrix, rri)
# rownames(tmp.0) =out.0$AE.0


########## bootstrp rri#############

fboot1= function(lpv =NULL){
  
  lpv = data.frame(lpv)
  dim0= dim(lpv)
  
  lpv0 =sapply(1:dim0[2],function(x){
                  ind = sample(length(lpv[,x]), rep=T) 
                  (lpv[ind,x])})
  
  rri.boot = max(func.rri(lpv =lpv0))
  return(rri.boot)
}

########### raw is a p-value matrix (fist column of raw is SITE_ID) ######
pvm.fisher.boot= function(n.boot= 1000, pmatrix=raw, epis = 1e-7){
  pmatrix = data.frame(pmatrix)
  ######## assgin very small value to p-value  = 0 ##########

  pv0 = pmatrix[-1]
  
  pv0[pv0 < epis] = epis
  data0 = -2*log(pv0)
  ###### number of tests for each site#
  ni = apply(pv0,1, function(x){sum(!is.na(x))})
  ######## number of test with pv <0.05##
  nsig = apply(pv0, 1, function(x)sum(x<0.05, na.rm = T))
  ## mean score for each site, similar to CP, high sibar, signal#############
  sibar = apply(data0,1, function(x){mean(x, na.rm = T)})
    
  ###### calcualte rri####
  rri0 = func.rri(lpv = data0, opt = 1)
  rri = rri0$rri
  # set.seed(1234567)
  # n.boot = 1000
  rri.sim = replicate(n.boot, fboot1(lpv = data0))
  # summary(rri.sim)
  (pv.fisher= sapply(rri,function(x){mean(as.numeric(rri.sim) >= x)}))
   res = data.frame(pmatrix[1],ni, nsig, sibar, n.boot,rri0,pv.fisher)
   colnames(res)[1:5] = c(colnames(pmatrix)[1],"#of tests","#of tests with pv<0.05","mean score(-2log(pv))", "#of bootstrap")
   ## order it by p-value 
  res = res[order(res$pv.fisher),]
  return(res)
}

pvm.lrt = function(pmatrix=raw, thred = 0.1,N.emp = 1000){
  # thred  =  0.1
  
  tmp0 = data.frame(ifelse(pmatrix[-1] < thred, 1, 0))
  # number of signals for each site
  nij= rowSums(tmp0,na.rm = T)
  
  ###### number of tests for each site
  nidot = apply(tmp0, 1, function(x){sum(!is.na(x))})
  
  d.0 = data.frame(SITE_ID = pmatrix[1], nij, nidot)

  # d = d[d$nij > 1,]
  pv.lrt =lrt.pois.all(d = d.0, N.emp=N.emp, alpha =0.05, sort1 = FALSE)
  
  res = cbind(pv.lrt,thred)
  res = res[order(res$pv.mlr),]
  return(res)

}
# alpha =0.05
# sig= ifelse(pv.0<alpha, TRUE, FALSE)

# tmp.1= cbind(tmp.0, pv.0,sig)


################## p-value matrix combination method from cluepoint, cp #########

############ if opt =0 , it only return sibar, if opt =1, it will return all the other variabels#######

#### when simplify1 is True, no qualify control , all tests are involved i nodis calculation ######
func.odis = function(pv = NULL, epis = 1e-10, sa = 0, opt = 0, simplify1 = TRUE){
  
  pv = data.frame(pv)
  
  if (simplify1 == TRUE){
    tt = rep(TRUE,ncol(pv))
  }else{
    tt = apply(pv, 2, function(x){if(
      (mean(x<0.05,na.rm = T) > 0.8) | (mean(is.na(x)) > 0.8) | 
      (length(unique(x)) == 1) | (min(x,na.rm = T) >= 10^(-sa))) return(FALSE) else return(TRUE)
    })}
    
  pv1 = pv[tt]



  ############ quality control finished ###########
  ######## assgin very small value 1e-10 to p-value < 1e-10##########
  pv1[pv1 < epis] = epis
  
  # for each site, de-noise the calcualtion of the ODIS by restricting the mean to the most significant tests 
  #   sij > salpha = 1.6 by default 
  
  data0 = -log10(pv1)
  sibar = apply(data0,1, function(x){mean(x[!is.na(x) & x >= sa])})
  
  ntest.odis = apply(data0, 1, function(x)sum(!is.na(x) & x >= sa, na.rm = T))
  
  
  if (opt == 0) return(sibar)
  if (opt == 1) return(data.frame(ncolumns.used = sum(tt),ntest.odis, odis = sibar))
}


## pv is the p-value matrix 
fboot.cp= function(pv =NULL){
  pv0 = matrix(data =(sample(unlist(pv), rep=T)),nrow = nrow(pv))
  cp.boot = (func.odis(pv =pv0,epis = epis, sa = sa,opt =0,simplify1 = TRUE))
  return(cp.boot)
}
pvm.cp = function(n.boot= 1000, pmatrix=raw, epis = 1e-10, sa = 0, simplify1 = TRUE){
  # thred  =  0.1
  ##############global variable ###############
  
  epis <<- epis
  sa <<- sa
  simplify1 <<- simplify1
  
  
  pmatrix = data.frame(pmatrix)
  pv0 = pmatrix[-1]
  


  ###### number of tests for each site#
  ni = apply(pv0,1, function(x){sum(!is.na(x))})
  ######## number of test with pv <0.05##
  nsig = apply(pv0, 1, function(x)sum(x<0.05, na.rm = T))


  
  odis0 = func.odis(pv = pv0, epis = epis, sa = sa, opt = 1,simplify1 = simplify1)
  odis = odis0$odis
  set.seed(1234567)
  # n.boot = 1000
  odis.sim = replicate(n.boot, fboot.cp(pv = pv0))

  pv.cp = sapply(1:length(odis), function(i){mean(odis.sim[i,] >= odis[i], na.rm = T)})
  
  res = data.frame(pmatrix[1],ni, nsig, n.boot,odis0,pv.cp, simplify1)
  colnames(res) = c(colnames(raw)[1],"#of tests","#of tests with pv<0.05", "#of bootstrap","#of columns left after quality control","#of test used for odis","odis(mean of -log10(pv))","pv.cp","simplified CP")
  ## order it by p-value 
  res1 = res[order(res$pv.cp),]
}
















