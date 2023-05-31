import numpy
import time

class SLAE:

    line, column, matrixMain, matrixFree = None, None, None, None

    def __init__(self, line, column, matrixMain, matrixFree):

        self.line = line
        self.column = column
        self.matrixMain = matrixMain
        self.matrixFree = matrixFree


    def GaussMethod(self):

        startTime = time.time()

        iteration = 0

        for i in range(len(self.matrixFree)):

            maxEl = abs(self.matrixMain[i][i])
            maxRow = i

            for j in range(i + 1, len(self.matrixFree)):

                if abs(self.matrixMain[j][i]) > maxEl:

                    maxEl = abs(self.matrixMain[j][i])
                    maxRow = j

            for j in range(i, len(self.matrixFree)):

                line = self.matrixMain[maxRow][j]
                self.matrixMain[maxRow][j] = self.matrixMain[i][j]
                self.matrixMain[i][j] = line

            line = self.matrixFree[maxRow]
            self.matrixFree[maxRow] = self.matrixFree[i]
            self.matrixFree[i] = line

            for k in range(i + 1, len(self.matrixFree)):

                value = -self.matrixMain[k][i] / self.matrixMain[i][i]

                for j in range(i, len(self.matrixFree)):

                    if i == j:

                        self.matrixMain[k][j] = 0

                    else:

                        self.matrixMain[k][j] += value * self.matrixMain[i][j]

                self.matrixFree[k] += value * self.matrixFree[i]

            iteration += 1

        x = {}
        
        for i in range(len(self.matrixFree) - 1, -1, -1):

            x.update({"x" + str(i + 1) : self.matrixFree[i]})

            for j in range(i + 1, len(self.matrixFree)):

                x["x" + str(i + 1)] -= self.matrixMain[i][j] * x["x" + str(j + 1)]

            x["x" + str(i + 1)] /= self.matrixMain[i][i]

            iteration += 1

        x.update({"Number of iterations" : iteration})

        endTime = time.time()

        x.update({"Convergence time" : endTime - startTime})

        return x
    

    def relaxationMethod(self, accuracy, relPar):

        startTime = time.time()

        exAccuracy, iteration = 1, 0

        vector = numpy.zeros((self.column, 3))

        vectorRes = {}

        while (accuracy <= exAccuracy):

            for i in range(self.column):

                vector[i][1] = self.matrixFree[i]
                
                for j in range(self.column):

                    if i == j:

                        continue
                    
                    vector[i][1] -= self.matrixMain[i][j] * vector[j][1]

                vector[i][1] /= self.matrixMain[i][i]


                memory = vector[i][1]

                vector[i][1] = relPar * vector[i][1] + (1 - relPar) * vector[i][0]

                vector[i][0] = memory

                vector[i][2] = abs(vector[i][1] - vector[i][0])
                    
                vectorRes.update({"x" + str(i + 1) : vector[i][1]})

            exAccuracy = vector[0][2]

            for i in range(1, self.column):

                if vector[i][2] > exAccuracy:

                    exAccuracy = vector[i][2]

            iteration += 1

        vectorRes.update({"Number of iterations" : iteration, "Experimental accuracy" : exAccuracy})

        endTime = time.time()

        vectorRes.update({"Convergence time" : endTime - startTime})

        return vectorRes
    
    
    def PrintMatrix(self):

        for i in range(self.column):

            for j in range(self.line):

                print(self.matrixMain[i][j], end=" ")

            print("|", self.matrixFree[i])    