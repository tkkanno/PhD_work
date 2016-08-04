get_median <-function(data, number)
  for (i in 1:number) {
    x <- median(data[[number]])
    y[i]<- x
  }
  return(y)


get_slopes <-function(x){
  value <- c(0,0,0)
  names(value)<- c("slope", "r.square", "p.value")
  values <-data.frame(value)
  gene <- as.integer(readline(prompt = "what gene number? ")) #this is the gene you're checking against
  #remember to adjust the loop number for the data you are
  #analysing! ideally should be fixed but i dont know how to
  size <- as.integer(readline(prompt ="how big (number of colums) is the dataset? "))
  for (i in 2:size){ #looping through the data
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
r1_corr <- read.csv('/home/louic/Desktop/Bioinformatics/glut_genes_data/correlations/ROCK1/ROCK1_correlations.csv', header = TRUE, sep = '\t')
names(r1_corr) <- tolower(names(r1_corr))

c_plot <- ggplot(data= rock2, aes(x= xu_slope, y= -log(xu_p.value), label = xu_gene))
c_plot <- c_plot +
  geom_point() +
  geom_text(aes(label=ifelse(((rock2$xu_slope < -0.5 | rock2$xu_slope > 0.4)&rock2$xu_p.value<0.01), 
                             as.character(rock2$xu_gene),'')),hjust=0, vjust=0) +xlim(-1.8,2.5)
c_plot
cor_plot<- function(data1, slope, p.value, gene){
  print(head(data1))
  print(data1[slope])
  print(data1[p.value])
  print(data1[gene])
  c_plot <- ggplot(data = data1, aes_string(x= data1[slope], y= -log(data1[p.value]), label = data1[gene]))
  c_plot <- c_plot +
  geom_point() +
  xlim(-1, 1) +
  geom_text(aes(label = ifelse(data1[p.value]<0.01 & data1[slope] >0.4), 
                               as.character(data1[gene]),''))
  c_plot
}