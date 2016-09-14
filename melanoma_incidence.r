m<-read.table('/home/louic/Desktop/thesis/figures/melanoma_incidence.csv', sep= '\t', row.names= 1, header = FALSE, check.names = FALSE)
m<-as.data.frame(t(m))
library(ggplot2)
graph <-ggplot(m, aes(x = Year, y = Male, colour = 'Male', size = 1.5)) + 
  geom_line() + 
  geom_line(data = m, aes(x = Year, y = Female, colour = 'Female', size = 1.5)) +
  labs(y = "Rate per 100,000", x = "Year of Diagnosis") +
  theme(axis.title.y= element_text(size = rel(1.4))) +
  theme(axis.title.x= element_text(size = rel(1.4))) +
  theme(axis.text.x= element_text(size = rel(1.4))) + 
  theme(axis.text.y= element_text(size = rel(1.4)))+
  theme(text = element_text(size =16))


graph
