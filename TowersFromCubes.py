import numpy as np

def CalculateSurface(ListOfIntegers):

# If ListOfIntegers contains negative number or zero or type of list elements are not integers 
# then this function returns with -1 as the whole surface of the created objectum is invalid in these cases.
# Otherwise it returns calculated surface.

    Surface = 0
    LastPartialSurface = 0;

    # Iterate over towers
    for i in range(len(ListOfIntegers)-1):
            # Chechk wheter type of elements are int and positive.
            if (isinstance(ListOfIntegers[i], int) == False or isinstance(ListOfIntegers[i+1], int) == False or ListOfIntegers[i] < 0 or ListOfIntegers[i+1] < 0):
                Surface = -1
                break
            else:
                # Partial surfaces of towers
                PartialSurface = 4*ListOfIntegers[i]+2-2*min(ListOfIntegers[i],ListOfIntegers[i+1])
                
                # Surface of last tower
                if(i == len(ListOfIntegers)-2):
                     LastPartialSurface = 4*ListOfIntegers[i+1]+2
                    
                Surface += PartialSurface + LastPartialSurface
               
    return Surface

ListOfIntegers = [4,25.56,1]
Surface = CalculateSurface(ListOfIntegers)


