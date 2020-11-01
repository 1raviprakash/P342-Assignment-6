# Library
import My_lib


# Function
def fun(x):
    return (x/(1 + x))


# Limits
a = 1
b = 3

for N in [5, 10, 25]:
    print("For N = ", N)
    print("Itegral(Midpoint) = ", My_lib.midpoint(a, b, fun, N))
    print("Itegral(Trapezoidal) = ", My_lib.traphezoidal(a, b, fun, N))
    print("Itegral(Simpson) = ", My_lib.simpson(a, b, fun, N))


# Output:
# For N =  5
# Itegral(Midpoint) =  1.308092114284065
# Itegral(Trapezoidal) =  1.3043650793650796
# Due to odd no. issue with simpson method, we take N=(N+1) i.e N = 6
# Itegral(Simpson) =  1.306830206830207
# For N =  10
# Itegral(Midpoint) =  1.3071646395900398
# Itegral(Trapezoidal) =  1.3062285968245722
# Itegral(Simpson) =  1.3068497693110697
# For N =  25
# Itegral(Midpoint) =  1.3069028019555275
# Itegral(Trapezoidal) =  1.3067528394240817
# Due to odd no. issue with simpson method, we take N=(N+1) i.e N = 26
# Itegral(Simpson) =  1.3068527513069683

'''
Comparison of  the result (in tabular format) with the actual analytical result:

_______________________________________________________________________________________________________________________                
      N      |       METHOD                |          RESULT                   |        Actual Analytical Result
             |                             |                                   |
             |   Itegral(Midpoint)         |        1.308092114284065          |
      5      |   Itegral(Trapezoidal)      |        1.3043650793650796         |
             |   Itegral(Simpson)          |        1.306830206830207          |
             |                             |                                   |
             |   Itegral(Midpoint)         |        1.3071646395900398         |
      10     |   Itegral(Trapezoidal)      |        1.3062285968245722         |           1.306852819440055    
             |   Itegral(Simpson)          |        1.3068497693110697         |
             |                             |                                   |
             |   Itegral(Midpoint)         |        1.3069028019555275         |
     20      |   Itegral(Trapezoidal)      |        1.3067528394240817         |
             |    Itegral(Simpson)         |        1.3068527513069683         |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          


'''
