rm(list=ls())

# Assumes 4-taxon balanced tree with equal branch lengths

brl <- 0.07
numSites <- 20
root <- vector(mode="character",length=numSites)
leftAnc <- vector(mode="character",length=numSites)
rightAnc <- vector(mode="character",length=numSites)
llTerm <- vector(mode="character",length=numSites)
lrTerm <- vector(mode="character",length=numSites)
rlTerm <- vector(mode="character",length=numSites)
rrTerm <- vector(mode="character",length=numSites)

probChange <- 1 - ((1/4) + ((3/4)*exp(-4*(brl/3))))

bases <- c("red","green","blue","yellow")

for (i in 1:numSites){
	root[i] <- sample(bases,1)
	
	# Draw left daughter of root
	leftAnc[i] <- root[i]
	if (runif(1) < probChange){
		while (root[i] == leftAnc[i]){
			leftAnc[i] <- sample(bases,1)
		}
	}
	
	# Draw right daughter of root
	rightAnc[i] <- root[i]
	if (runif(1) < probChange){
		while (root[i] == rightAnc[i]){
			rightAnc[i] <- sample(bases,1)
		}
	}
	
	# Draw left most terminal
	llTerm[i] <- leftAnc[i]
	if (runif(1) < probChange){
		while (llTerm[i] == leftAnc[i]){
			llTerm[i] <- sample(bases,1)
		}
	}
	
	lrTerm[i] <- leftAnc[i]
	if (runif(1) < probChange){
		while (lrTerm[i] == leftAnc[i]){
			lrTerm[i] <- sample(bases,1)
		}
	}
	
	rlTerm[i] <- rightAnc[i]
	if (runif(1) < probChange){
		while (rlTerm[i] == rightAnc[i]){
			rlTerm[i] <- sample(bases,1)
		}
	}
	
	rrTerm[i] <- rightAnc[i]
	if (runif(1) < probChange){
		while (rrTerm[i] == rightAnc[i]){
			rrTerm[i] <- sample(bases,1)
		}
	}
}

scale <- 0.15
quartz(width=numSites*scale,height=4*scale)
par(mai=c(0,0,0,0))
plot(c(),c(),main="",xaxt="n",yaxt="n",xlab="",ylab="",bty="n",
	 xlim=c(0,numSites*scale),ylim=c(0,(numSites/4)*scale))

for (i in 1:numSites){
	rect(numSites*scale*((i-1)/numSites),
		(numSites/4)*scale*(3/4),
		numSites*scale*(i/numSites),
		(numSites/4)*scale,
		col=llTerm[i])
	rect(numSites*scale*((i-1)/numSites),
		(numSites/4)*scale*(1/2),
		numSites*scale*(i/numSites),
		(numSites/4)*scale*(3/4),
		col=lrTerm[i])
	rect(numSites*scale*((i-1)/numSites),
		(numSites/4)*scale*(1/4),
		numSites*scale*(i/numSites),
		(numSites/4)*scale*(1/2),
		col=rlTerm[i])
	rect(numSites*scale*((i-1)/numSites),
		0,
		numSites*scale*(i/numSites),
		(numSites/4)*scale*(1/4),
		col=llTerm[i])
}

