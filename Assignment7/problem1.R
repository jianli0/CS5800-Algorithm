library(lpSolve)
eg.lp <- lp(objective.in=c(5, 8),
            const.mat=matrix(c(1, 1, 1, 2), nrow=2),
            const.rhs=c(2, 3),
            const.dir=c("<=", "="), direction="max")
print (eg.lp$solution)

