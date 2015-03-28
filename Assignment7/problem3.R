library(lpSolve)
eg.lp <- lp(objective.in=c(1, 2, 3, 4),
            const.mat=matrix(c(2, 0, 4, 0,
                               0, 5, 3, 0,
                               8, 2, 0, 0,
                               1, 0, 0, 6,
                               0, 1, 7, 0,
                               0, 3, 0, 5), nrow=6),
            const.rhs=c(-10, -12, 5, 2, 1, 8),
            const.dir=c(">=",">=","<=","<=","<=","<="), direction="max")

eg.lp$solution
