library(lpSolve)
eg.lp <- lp(objective.in=c(1.6, 1.7, 0.6, 9.3),
            const.mat=matrix(c(1.7, 4.7, -1.1, 2.7,
                               8.4, 5.9, -0.4, 0.0,
                              -1.4, 9.6,  0.0, 7.0,
                               5.0, 0.3,  8.9,-1.5,
                               0.0,-1.1,  0.0, 8.1
                               ), nrow=5),
            const.rhs=c(3.5, 5, 7.9, 9.9, 1.3),
            const.dir=c("<=","<=","<=","<=","<="), direction="max")
eg.lp
eg.lp$solution