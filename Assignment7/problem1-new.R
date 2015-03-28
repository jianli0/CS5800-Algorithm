lprec <- make.lp(0, 15)
set.objfn(lprec, c(3,4,2,5,4,4,5,2,1,2,1,3,6,5,2),)

add.constraint(lprec, c(500,400,350,100,50,1000,1500,500,200,80,200,400,500,100,300), "<=",5000)
add.constraint(lprec, c(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0), "<=",3)
add.constraint(lprec, c(0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0), "<=",3)
add.constraint(lprec, c(0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0), "<=",3)
add.constraint(lprec, c(0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0), "<=",4)
add.constraint(lprec, c(0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1), "<=",4)

set.bounds(lprec, upper = c(1,1,1,2,1,2,2,1,1,2,2,1,2,3,4), 
           columns = c(1, 2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

lp.control(lprec,sense='max')


#set.bounds(lprec, lower = c(28.6, 18), columns = c(1, 4))
#set.bounds(lprec, upper = 48.98, columns = 4)

RowNames <- c("const1", "const2", "const3",  "const4",  "const5",  "const6")
ColNames <- c("x11", "x12", "x13", "x14", "x15", "x21", "x22", "x23", "x24", "x25", "x31", "x32", "x33", "x34", "x35")
dimnames(lprec) <- list(RowNames, ColNames)

lprec
print (lprec)
solve(lprec)
get.objective(lprec)
get.variables(lprec)
get.constraints(lprec)
