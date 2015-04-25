# library(rootSolve)
# model <- function(x){
# f1 <- x[1]+x[2] -4
# f2 <- 2*x[1] + 3*x[2] -11
# c(f1=f1,f2=f2)
# }
# solution <- multiroot(f = model, start = c(1, 1))
# print (solution)

library(rootSolve)
model <- function(x){
  f1 <- -0.7*x[1] + 0.1*x[2] + 0.4*x[3] + 0.2*x[4]
  f2 <- 0.2*x[1] + 0.6*x[2] - 0.9*x[3] + 0.5*x[4]
  f3 <- 0.4*x[1] + 0 * x[2] + 0.1*x[3] -0.9*x[4]
  f4 <- x[1] + x[2] + x[3] + x[4] -1 
  c(f1=f1,f2=f2,f3=f3,f4=f4)
}
solution <- multiroot(f = model, start = c(1, 1, 1, 1))
print (solution)