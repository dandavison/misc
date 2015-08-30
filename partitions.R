C <- function(n) {
    if(n < 2) return(0)
    i <- 1:(n-1)
    sum((n - i) * n^(i - 1))
}
