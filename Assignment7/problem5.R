library(lpSolve)
eg.lp <- lp(objective.in=c(-5, 3, 5, -3, -4, -9),
            const.mat=matrix(c(-6, 3, 5, 2, 5, 6,
                               0, 10, 5, 5, -5, 8,
                               8, -4, 7, 4, -5, 3,
                               -4, -3, -5, -2, 9, -5,
                               3, 8, 4, -1, -4, 2), nrow=5),
            const.rhs=c(1,4,10,-8,-4),
            const.dir=c("<=","<=","<=",">=",">="), direction="min")

eg.lp$solution