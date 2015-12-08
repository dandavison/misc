svg("curve.svg")
cf1 = curve((x), from=0, to=1)
cf2 = curve((3 - sqrt(9 - 8 * x)) / 2, from=0, to=1)
plot(cf1, col="red", type="l", lty=2, xlab="Prevalence", ylab="Allele frequency")
lines(cf2, col="blue", lty=2)
legend("bottomright",
       legend=c(expression(alpha),
                expression((3 - sqrt(9 - 8 * alpha)) / 2)),
       col=c("red", "blue"), lty=2, bty="n")
dev.off()
