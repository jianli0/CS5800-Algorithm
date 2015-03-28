lprec <- make.lp(0, 6)
set.objfn(lprec, c(-5, 3, 5, -3, -4, -9))

add.constraint(lprec, c(-6, 3, 5, 2, 5, 6), "<=",1)
add.constraint(lprec, c(0, 10, 5, 5, -5, 8), "<=", 4)
add.constraint(lprec, c(8, -4, 7, 4, -5, 3), "<=", 10)
add.constraint(lprec, c(-4, -3, -5, -2, 9, -5), ">=", -8)
add.constraint(lprec, c(3, 8, 4, -1, -4, 2), ">=", -4)

#lp.control(lprec,sense='max')


#set.bounds(lprec, lower = c(28.6, 18), columns = c(1, 4))
#set.bounds(lprec, upper = 48.98, columns = 4)

RowNames <- c("const1", "const2", "const3",  "const4",  "const5")
ColNames <- c("a","b", "c", "d", "e", "f")
dimnames(lprec) <- list(RowNames, ColNames)

lprec
solve(lprec)
get.objective(lprec)
round(get.objective(lprec),2)
get.variables(lprec)
round(get.variables(lprec),2)
round(get.constraints(lprec),2)
get.dual.solution(lprec)
