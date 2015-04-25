library(rootSolve)

model <- function(x){
  f1 <- x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] -1
  f2 <- -0.1*x[1] + 0.1*x[2] + 0.12*x[8]
  f3 <- 0.1*x[1] - 0.2*x[2]
  f4 <- 0.1*x[2] - 0.1*x[3] + 0.01*x[4]
  f5 <- 0.1*x[3] - 0.05*x[4]
  f6 <- 0.04*x[4] - 0.1*x[5] + 0.02*x[6]
  f7 <- 0.1*x[5] - 1/15*x[6]
  f8 <- 7/150*x[6] - 0.2*x[7] + 0.08*x[8]
  #f9 <- 0.2*x[7] - 0.2*x[8]
  c(f1=f1,f2=f2,f3=f3,f4=f4,f5=f5,f6=f6,f7=f7,f8=f8)
}
solution <- multiroot(f = model, start = c(1, 1, 1, 1, 1, 1, 1, 1))
print (solution)