# Library
import My_lib


# Function
def fun(x):
    return (4/(1 + (x**2)))


# Limits
a = 0
b = 1


# No. of random values taken
N = 100000


# Recalling function and saving value in "Q.4.txt" for graph plotting
print("Integration of the given function = ",  My_lib.monte_carlo(
    a, b, fun, N, open("Q.4.txt", "w+")))


# Output
# Integration of the given function =  3.1393821390003627
