class MathOper:

    def meanDeviationGauss(self, vectorExp, vectorTheor):

        meanDev, index = 0, 0

        for i in range(len(vectorExp) - 3, -1, -1):
            
            meanDev += abs(vectorTheor[index] - vectorExp["x" + str(i + 1)])
            
            index += 1
            
        meanDev /= len(vectorTheor)

        return meanDev
    

    def meanDeviation(self, vectorExp, vectorTheor):

        meanDev = 0
        
        for i in range(len(vectorExp) - 3):
            
            meanDev += abs(vectorTheor[i] - vectorExp["x" + str(i + 1)])
            
        meanDev /= len(vectorTheor)

        return meanDev

