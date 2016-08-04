get_median <-function(data, number)
  for (i in 1:number) {
    x <- median(data[[number]])
    y[i]<- x
  }
  return(y)


get_slopes <-function(x){
  values <- c(0,0,0)
  names(values)<- c("slope", "r.square", "p.value")
  values <-data.frame(values)
  gene <- 158
  #remember to adjust the loop number for the data you are
  #analysing! ideally should be fixed but i dont know how
  for (i in 2:71){
    fit<- lm(x[[i]]~x[[gene]])
    mycor <- cor.test(x[[gene]],x[[i]])$p.value
    myr <- summary(fit)$r.squared
    myslope <-fit$coefficients[[2]]
    stuff <-c(myslope,myr,mycor)
    lab <- names(x)[[i]]
    values[lab]<-stuff
}
  return(values)  
}
get_slopes_2D <-function(x){
  values <- matrix(,nrow = 80, ncol= 20)
  for (i in (156:159)){

    for(j in (2:71)){

      fit<- lm(x[[i]]~x[[j]])
      myslope <-fit$coefficients[[2]]
      m <- (j-154)
      n <-(i-1)
      values[n,m]<-myslope
  }
  }
  return(values)  
}

adjust_ps <- function(x) {
  p<-x
  holm <- p.adjust(x, "holm")
  hochberg <- p.adjust(x, "hochberg")
  hommel <- p.adjust(x, "hommel")
  bonferroni <- p.adjust(x, "bonferroni")
  bh <- p.adjust(x, "BH")
  by <- p.adjust(x, "BY")
  fdr <-p.adjust(x, "fdr")
  p.adj <- data.frame(p, holm, hochberg, hommel, bonferroni, bh, by, fdr)
  return(p.adj)
  
  }