#load survival data and turn headers to lowercase
surv <- read.csv('/home/louic/Desktop/Bioinformatics/survival_analysis/tcga_glut_surv.csv', header=TRUE)
names(surv)<-tolower(names(surv))

### make sure that the data you are uploading is already made into medians or quartiles for survivial analysis
#creating survival curve data
rock2.surv<- survfit(Surv(surv10y, vital10y)~rock2,data = surv)
#plot curve with ggsurv
pl2<-ggsurv(rock2.surv)
pl2 <- pl2 + guides(linetype = F)
#    scale_colour_discrete(name = 'Expression', breaks = c(0,1), labels=c('Low', 'High'))
    
#find median survival times 
med.surv <- data.frame(time = c(270,270, 426,426), quant = c(.5,0,.5,0),
                       sex = c('M', 'M', 'F', 'F'))
#add median survival lines (50%)
> pl2+geom_line(data = med.surv, aes(time, quant, group =group), col = 'darkblue', linetype = 3)+
  + geom_point(data=med.surv, aes(time, quant, group=group), col = 'darkblue')
##generalized function to check library
Surv_analysis <- function(survival, status, gene) {

  values <- c(0,0,0)
  names(values)<- c("median low", "median high", "p.value")
  values<-data.frame(values)
  for(i in 1:length(gene)){ 
    fit <- survfit(Surv(survival, status)~gene[[i]])
    diff<- survdiff(Surv(survival, status == 1) ~ gene[[i]])  
    p.value <- 1 - pchisq(diff$chisq, 1)
    med<-unname(summary(fit)$table[,'median'])
    stuff<- c(med, p.value)
    lab <- names(gene)[[i]]
    print(lab)
    values[lab]<-stuff
    }
  return(values)
}

#plot all the survival curves with p.values in ggplot

tkplt<- ggplot(k_surv, aes(med.diff, -log(p.value)))
tkplt+geom_point(aes(colour = k_surv$med.diff, size = 3))+
geom_text(aes(label=ifelse(k_surv$p.value<0.05, 
              as.character(k_surv$gene),'')),hjust=0, yjust=0)


survdiff(Surv(survival, status == 1) ~ gene[[i]]) 
survdiff(Surv(survival, vital_status ==1) ~ genes[[3]])