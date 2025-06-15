import sys
import numpy
list = [1,2,3,4,5,6]
convert = numpy.array(list)
print(type(convert))
print("After convertion of list to array memory size:",sys.getsizeof(convert))