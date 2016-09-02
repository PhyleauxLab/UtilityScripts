rm(list=ls())

drawBase <- function()
	{
		ranNum <- runif(1)
		if (ranNum <= 0.25) { return(rgb(1,0,0,alpha=1)) }
		else if (ranNum < 0.5) { return(rgb(0,1,0,alpha=1)) }
		else if (ranNum < 0.75) { return(rgb(0,0,1,alpha=1)) }
		else if (ranNum <= 1.0) { return(rgb(1,1,0,alpha=1)) }
	}

ntax <- 4
nsites <- 20

quartz(width=10,height=4)
plot(x=c(),y=c(),xlim=c(0,nsites),ylim=c(0,ntax),xlab="",ylab="",main="",xaxt="n",yaxt="n",bty="n")

for (i in 1:ntax){
	for (j in 1:nsites){
		polygon(x=c(j-1,j,j,j-1),y=c(i-1,i-1,i,i),col=drawBase())
	}
}
