import numpy as np

# Angle	Average

# -40	61

# -30	116

# -20	177.3333333

# -10	246

# 0	296.3333333

# 10	539.6666667

# 20	680.3333333

# 30	733.6666667

# 40	651

# 50	652

# 60	534.6666667

# 70	303.6666667

# 80	24.66666667

# 90	0
#the angels that are being put in
x = [-40, -20, 0, 20, 40, 60, 80]
y = [61, 177, 296, 680, 651, 534.67, 24.67]

# Get Polynomial Regression
#ths is what the result of the equation will be found at
result = np.polyfit(x, y, 2)

print(result)
#this would be the person entering their angle
myNumber = raw_input("Input an angle")
# Get the equation
eq = np.poly1d(result)

print(eq)

print(eq(2))

print("My answer is: " + str(eq(int(myNumber))))

x2 = np.arange(-40, 90)

yfit = np.polyval(result, x2)
x2 = np.arange(-40, 90)
#the graph function is not working with the program/computer