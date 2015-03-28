lprec <- make.lp(0, 8)
set.objfn(lprec, c(1, -1, 2, -2, 3, -3 , 4 ,-4),)

add.constraint(lprec, c(2,-2, 0, 0, 4, -4, 0, 0), ">=",-10)
add.constraint(lprec, c(0, 0, 5, -5, 3,-3, 0, 0), ">=", -12)
add.constraint(lprec, c(8,-8, 2, -2, 0, 0, 0, 0), "<=", 5)
add.constraint(lprec, c(1,-1, 0,  0, 0, 0, 6, -6), "<=", 2)
add.constraint(lprec, c(0, 0, 1, -1, 7,-7, 0, 0), "<=", 1)
add.constraint(lprec, c(0, 0, 3, -3, 0, 0, 5, -5), "<=", 8)
#set.bounds(lprec, lower = c(-Inf,-Inf,-Inf,-Inf,-Inf,-Inf), columns = c(1,2,3,4,5,6))

lp.control(lprec,sense='max')


#set.bounds(lprec, lower = c(28.6, 18), columns = c(1, 4))
#set.bounds(lprec, upper = 48.98, columns = 4)

RowNames <- c("const1", "const2", "const3",  "const4",  "const5",  "const6")
ColNames <- c("x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8")

dimnames(lprec) <- list(RowNames, ColNames)

lprec
solve(lprec)
get.objective(lprec)
round(get.objective(lprec),2)
get.variables(lprec)
round(get.variables(lprec),2)
round(get.constraints(lprec),2)

