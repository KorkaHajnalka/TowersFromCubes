import numpy as np

def CalculateSurface(ListOfIntegers):

# If ListOfIntegers contains negative number or zero then this function returns with -1 as the surface of a single tower 
# is invalid in these cases.

    SumOfPartialSurface = 0
    Surface = -1

    for i in range(len(ListOfIntegers)):
        
        if (ListOfIntegers[i] > 0):
            if(i < len(ListOfIntegers)-1):
                PartialSurface = 4*ListOfIntegers[i]+2-2*min(ListOfIntegers[i],ListOfIntegers[i+1])
            else:
                PartialSurface = 4*ListOfIntegers[i]+2

            SumOfPartialSurface = SumOfPartialSurface + PartialSurface
        Surface = SumOfPartialSurface
        else:
            break

    
    return Surface

ListOfIntegers = [4,-3,1]
Surface = CalculateSurface(ListOfIntegers)


