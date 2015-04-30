newton<-read.table("newton_results.csv", header=T, sep=",")
nibun<-read.table("nibun_results.csv", header=T, sep=",")


newton$xn<-abs(newton$xn-8)
nibun$xn<-abs(nibun$xn-8)


#newton_smth <- nls( xn ~ a*n^b+c, data=newton, start=list(a=-1, b=2, c=0))
#pred_newton <- predict(newton_smth)

#nibun_smth <- nls( xn ~ a*n^b+c, data=nibun, start=list(a=-5, b=1, c=0))
#pred_nibun <- predict(nibun_smth)

nibun_smth <- lm(xn~n, data=nibun)


plot(	newton,  col="red", xlim=c(0,30),
		xlab="number of process",
		ylab=expression(paste({x[n]})))
#lines(pred_newton)


points(nibun, col="blue")
abline(nibun_smth, col="blue")

legend("topright", legend=c("newton","nibun"), pch=1, col=c("red","blue"))