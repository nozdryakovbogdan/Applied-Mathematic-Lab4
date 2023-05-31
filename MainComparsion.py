import numpy

from SLAE import SLAE
from MathematicalOperations import MathOper

matrixMain = numpy.random.randint(-10, 10, size=(10, 10))

matrixFree = numpy.random.randint(-10, 10, size=(10))

slae = SLAE(10, 10, matrixMain, matrixFree)

vector = slae.GaussMethod()

#print("Gauss method:")

#print("Number of iterations:", str(vector["Number of iterations"]) + ";","Convergence time:", vector["Convergence time"])

print("Gauss method:", vector)

print()

theorVec = numpy.linalg.inv(matrixMain).dot(matrixFree)

print("Theoretical values", theorVec)

print()

math = MathOper()

meanDev = math.meanDeviationGauss(vector, theorVec)

print("Main deviation:", meanDev)

print()

vector = slae.relaxationMethod(0.01, 0.5)

#print("Relaxation method:")

#print("Number of iterations:", str(vector["Number of iterations"]) + ";", "Convergence time:", vector["Convergence time"])

print("Relaxation method:", vector)

print()

meanDev = math.meanDeviation(vector, theorVec)

print("Main deviation:", meanDev)