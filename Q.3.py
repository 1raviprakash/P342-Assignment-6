# Library
import My_lib
import math


# Function
def fun(x):
    return math.exp(-(x**2))


# Limits
a = 0
b = 1

# Max error as per Question
max_error = 0.001


# Lower peak point in (0,1)
sec_der_f_max = -2


# Upper peak point in (0,1)
four_der_f_max = 12


# Midpoint Method
print("Integral by Midpoint Method:-->")
N = (My_lib.max_error_midpoint(a, b, sec_der_f_max, max_error))
print("Calculated 'N' (Max. Error = 0.001) =", N)
print("Integral =", My_lib.midpoint(a, b, fun, N))


# Trapezoidal Method
print("Integral by Trapezoidal Method:-->")
N = (My_lib.max_error_trapezoidal(a, b, sec_der_f_max, max_error))
print("Calculated 'N' (Max. Error = 0.001) =", N)
print("Integral =", My_lib.traphezoidal(a, b, fun, N))


# Simpson Method
print("Integral by Simpson Method:-->")
N = (My_lib.max_error_simpson(a, b, four_der_f_max, max_error))
print("Calculated 'N' (Max. Error = 0.001) =", N)
print("Integral =", My_lib.simpson(a, b, fun, N))


# Output :
# Integral by Midpoint Method:-->
# Calculated 'N' (Max. Error = 0.001) = 10
# Integral = 0.7471308777479975
# Integral by Trapezoidal Method:-->
# Calculated 'N' (Max. Error = 0.001) = 13
# Integral = 0.7464612610366896
# Integral by Simpson Method:-->
# Calculated 'N' (Max. Error = 0.001) = 3
# Due to odd no. issue with simpson method, we take N=(N+1) i.e N = 4
# Integral = 0.7468553797909873
