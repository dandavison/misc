cf1 <- curve(sqrt(x), from=0, to=1)
cf2 <- curve(sqrt(1 + 8 * x) - x - 1, from=0, to=1)

plot(cf1, col="red", type="l", lty=2, xlab="Prevalence", ylab="Carrier frequency")
lines(cf2, col="blue", lty=2)
legend("bottomright",
       legend=c(expression(sqrt(beta)),
                expression(sqrt(1 + 8*beta) - beta -1)),
       col=c("red", "blue"), lty=2, bty="n")
