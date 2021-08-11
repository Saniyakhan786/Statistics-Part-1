#airquality = read.csv('path/airquality.csv', header= TRUE, sep=",")
#for inbuild r dataset
airquality <- datasets::airquality

#####Top 10 rows and Last 10 rows
head (airquality)    #by default 6 rows are displayed
tail(airquality)     #by default 6 rows are displayed
head(airquality,4)   #for specific no of rows and columns
tail(airquality,8)   #for specific no of rows and columns

#Columns

airquality[,c(1,2)]   #all rows and columns 1&2
airquality$Solar.R    #for a particular

df<- airquality[,6]   #excluding column no 6
df                    #to check the dataset

#Descriptive Statistics

summary(airquality[,3])      #D.S for column
summary(airquality$Solar.R)  #D.S for specific column name
summary(airquality)          #D.S for all columns

#Visualisation Technique
#1. Scatter Plot

plot(airquality$Solar.R)                               #plot for specific column
plot(airquality$Temp,airquality$Solar.R,type = "p")    #relation between temp & wind
plot(airquality$Ozone,type = "1")                      #plot a line
plot(airquality)
plot(airquality$Solar.R,type = "b")                    #points and lines
plot(airquality$Solar.R,xlab = 'No of instances', ylab = 'solar.R Concentartion', main = 'solar.R', col='blue', type = "p")  #naming the labels on the graph

#2. Horizontal Bar Plot

barplot(airquality$Solar.R)                #plot for specific column
barplot(airquality$Solar.R,horiz = "F")
barplot(airquality$Solar.R,main = 'Solar.R No of instances', ylab = 'solar.R', col='blue', horiz= "F")  #naming the labels on the graph

#3. Histogram

hist(airquality$Solar.R)                               #plot for specific colum
hist(airquality$Solar.R,main = 'Solar.R No of instances', xlab = 'solar Radiation', col='blue') 

#4. Single Box Plot

boxplot(airquality$Solar.R,main ="Box Plot", xlab = 'Solar radaition')
summary(airquality$Solar.R)             #to check summary
boxplot.stats(airquality$Solar.R)$out   #to check outliers

#5. Multiple Box Plot

boxplot(airquality[,1:4],main = 'Multiple')    #to get multiple box plot at once


#margin of the grid (mar)
#no of rows and columns (mfrow)
#whether a border is to be included (bty)
#and positions to the labels
#labels (las:1 for horizontal, las:0 for vertical)
#bty- box around the plot (0=yes box needed, n=no)


par(mfrow = c(3,3),mar = c(2,5,2,1),las=0, bty = "0")
plot(airquality$Solar.R)
plot(airquality$Ozone,airquality$Solar.R)
plot(airquality$Wind,type = "1")

