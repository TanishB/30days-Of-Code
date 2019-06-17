class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        minElement = self.__elements[0]
        maxElement = self.__elements[0]
        for element in self.__elements:
            if element<minElement:
                minElement = element
            elif element>maxElement:
                maxElement=element
        
        self.maximumDifference = abs(maxElement - minElement)


# End of Difference class