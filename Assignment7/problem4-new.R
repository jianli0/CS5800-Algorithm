lprec <- make.lp(0, 6)
set.objfn(lprec, c(0, 4.9, 0.7, 1.7, 0, 7.1),)

add.constraint(lprec, c(3.6, 0.6, 5.9, 4.5, 0.4, 0.0), "<=",7.4)
add.constraint(lprec, c(0.0, 4.5, 0.0, 1.8, 0.0, 0.5), "<=", 4.3)
add.constraint(lprec, c(8.1, 3.3, 0.0, 7.5, 0.0, 0.0), "<=", 0.9)
add.constraint(lprec, c(5.8, 5.6, 0.0, 0.0, 0.0, 4.8), "<=", 2)
add.constraint(lprec, c(1.5, 0.0, 0.9, 0.0, 1.8, 8.6), "<=",2.6)
add.constraint(lprec, c(3.1, 5.3, 0.0, 1.1, 8.0, 0.0), "<=", 8.1)
add.constraint(lprec, c(0.0, 9.9, 0.0, 5.1, 0.0, 7.9), ">=", -3)
add.constraint(lprec, c(0.0, 0.5, 5.3, 0.2, 8.6, 5.1), ">=", -8.5)
lp.control(lprec,sense='max')


#set.bounds(lprec, lower = c(28.6, 18), columns = c(1, 4))
#set.bounds(lprec, upper = 48.98, columns = 4)

RowNames <- c("const1", "const2", "const3",  "const4",  "const5",  "const6",  "const7",  "const8")
ColNames <- c("x1",  "x2",  "x3",  "x4",  "x5",  "x6")
dimnames(lprec) <- list(RowNames, ColNames)

lprec
solve(lprec)
get.objective(lprec)
round(get.objective(lprec),2)
get.variables(lprec)
round(get.variables(lprec),2)
round(get.constraints(lprec),2)
