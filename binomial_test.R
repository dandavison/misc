#!/usr/bin/env Rscript
# Test null hypothesis that both samples drawn from the same binomial distribution
my.prop.test <- function (x, n, p = NULL, alternative = c("two.sided", "less", 
    "greater"), conf.level = 0.95, correct = TRUE) 
{
    DNAME <- deparse(substitute(x))
    if (is.table(x) && length(dim(x)) == 1L) {
        if (dim(x) != 2L) 
            stop("table 'x' should have 2 entries")
        l <- 1
        n <- sum(x)
        x <- x[1L]
    }
    else if (is.matrix(x)) {
        if (ncol(x) != 2L) 
            stop("'x' must have 2 columns")
        l <- nrow(x)
        n <- rowSums(x)
        x <- x[, 1L]
    }
    else {
        DNAME <- paste(DNAME, "out of", deparse(substitute(n)))
        if ((l <- length(x)) != length(n)) 
            stop("'x' and 'n' must have the same length")
    }
    OK <- complete.cases(x, n)
    x <- x[OK]
    n <- n[OK]
    if ((k <- length(x)) < 1L) 
        stop("not enough data")
    if (any(n <= 0)) 
        stop("elements of 'n' must be positive")
    if (any(x < 0)) 
        stop("elements of 'x' must be nonnegative")
    if (any(x > n)) 
        stop("elements of 'x' must not be greater than those of 'n'")
    if (is.null(p) && (k == 1)) 
        p <- 0.5
    if (!is.null(p)) {
        DNAME <- paste(DNAME, ", null ", ifelse(k == 1, "probability ", 
            "probabilities "), deparse(substitute(p)), sep = "")
        if (length(p) != l) 
            stop("'p' must have the same length as 'x' and 'n'")
        p <- p[OK]
        if (any((p <= 0) | (p >= 1))) 
            stop("elements of 'p' must be in (0,1)")
    }
    alternative <- match.arg(alternative)
    if (k > 2 || (k == 2) && !is.null(p)) 
        alternative <- "two.sided"
    if ((length(conf.level) != 1L) || is.na(conf.level) || (conf.level <= 
        0) || (conf.level >= 1)) 
        stop("'conf.level' must be a single number between 0 and 1")
    correct <- as.logical(correct)
    ESTIMATE <- x/n
    names(ESTIMATE) <- if (k == 1) 
        "p"
    else paste("prop", 1L:l)[OK]
    NVAL <- p
    CINT <- NULL
    YATES <- ifelse(correct && (k <= 2), 0.5, 0)
    if (k == 1) {
        z <- ifelse(alternative == "two.sided", qnorm((1 + conf.level)/2), 
            qnorm(conf.level))
        YATES <- min(YATES, abs(x - n * p))
        z22n <- z^2/(2 * n)
        p.c <- ESTIMATE + YATES/n
        p.u <- if (p.c >= 1) 
            1
        else (p.c + z22n + z * sqrt(p.c * (1 - p.c)/n + z22n/(2 * 
            n)))/(1 + 2 * z22n)
        p.c <- ESTIMATE - YATES/n
        p.l <- if (p.c <= 0) 
            0
        else (p.c + z22n - z * sqrt(p.c * (1 - p.c)/n + z22n/(2 * 
            n)))/(1 + 2 * z22n)
        CINT <- switch(alternative, two.sided = c(max(p.l, 0), 
            min(p.u, 1)), greater = c(max(p.l, 0), 1), less = c(0, 
            min(p.u, 1)))
    }
    else if ((k == 2) & is.null(p)) {
        DELTA <- ESTIMATE[1L] - ESTIMATE[2L]
        YATES <- min(YATES, abs(DELTA)/sum(1/n))
        WIDTH <- (switch(alternative,
                         two.sided = qnorm((1 + conf.level)/2),
                         qnorm(conf.level))
                  * sqrt(sum(ESTIMATE * (1 - ESTIMATE)/n)) + YATES * sum(1/n))
        CINT <- switch(alternative,
                       two.sided = c(max(DELTA - WIDTH, -1),
                                     min(DELTA + WIDTH, 1)),
                       greater = c(max(DELTA - WIDTH, -1), 1),
                       less = c(-1, min(DELTA + WIDTH, 1)))
    }
    if (!is.null(CINT)) 
        attr(CINT, "conf.level") <- conf.level
    METHOD <- paste(ifelse(k == 1, "1-sample proportions test", 
        paste(k, "-sample test for ", ifelse(is.null(p), "equality of", 
            "given"), " proportions", sep = "")), ifelse(YATES, 
        "with", "without"), "continuity correction")
    if (is.null(p)) {
        p <- sum(x)/sum(n)
        PARAMETER <- k - 1
    }
    else {
        PARAMETER <- k
        names(NVAL) <- names(ESTIMATE)
    }
    names(PARAMETER) <- "df"
    x <- cbind(x, n - x)
    E <- cbind(n * p, n * (1 - p))
    if (any(E < 5)) 
        warning("Chi-squared approximation may be incorrect")
    STATISTIC <- sum((abs(x - E) - YATES)^2/E)

    print(YATES)
    print(DELTA)
    print(WIDTH)

    names(STATISTIC) <- "X-squared"
    if (alternative == "two.sided") 
        PVAL <- pchisq(STATISTIC, PARAMETER, lower.tail = FALSE)
    else {
        if (k == 1) 
            z <- sign(ESTIMATE - p) * sqrt(STATISTIC)
        else z <- sign(DELTA) * sqrt(STATISTIC)
        PVAL <- pnorm(z, lower.tail = (alternative == "less"))
    }
    RVAL <- list(statistic = STATISTIC, parameter = PARAMETER, 
        p.value = as.numeric(PVAL), estimate = ESTIMATE, null.value = NVAL, 
        conf.int = CINT, alternative = alternative, method = METHOD, 
        data.name = DNAME)
    class(RVAL) <- "htest"
    return(RVAL)
}

argv <- commandArgs(trailing=TRUE)
stopifnot(length(argv) == 4)
argv <- sapply(argv, as.integer)

x1 <- argv[1]
n1 <- argv[2]
x2 <- argv[3]
n2 <- argv[4]






test <- my.prop.test(x=c(x1, x2), n=c(n1, n2))




print(test$p.value)
print(test$conf.int)
