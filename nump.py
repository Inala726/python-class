import numpy
import matplotlib.pyplot as mp

arr = numpy.array([31, 28, 30912, 483, 5]) # Create a 1D array
print(arr) #sort the array
arr.transpose()
print(arr)

arr = numpy.array(45) #Create a 0D array
print(arr)

arr = numpy.array([[1, 2, 3], [4, 5, 6]])
print(arr) # Create a 2D array

arr = numpy.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
print(arr[0]) # Create a 3D array

print(numpy.random.rand(100, 10)) # Create an array of random numbers with shape (3, 2)

sales = numpy.array([
    [50, 30, 20],
    [60, 20, 30],
    [70, 40, 50],
    [80, 50, 60],
    [90, 62, 78]
])
print("Average eggs sold: ", sales[::, 2].mean()) # This calculates the mean of the first column (egg sales) across all rows

days = [1,2,3,4,5]
sales = [50,60,55,70,65]

mp.plot(days, sales, marker='*')
mp.title("Daily Sales(5)")
mp.xlabel("Days")
mp.ylabel("Unit sold")
mp.show()