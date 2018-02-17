num1=3.1425467389
num2=10.2903948

# previous
print('num1 is : ', num1, "and num2 is : ", num2)

#new
#format method
print('num1 is {0} and num 2 is {1}'.format(num1, num2))

#only 3 precision
print('num1 is {0:.3} and num 2 is {1:.4}'.format(num1, num2))

#3 decimal points
print('num1 is {0:.3f} and num 2 is {1:.4f}'.format(num1, num2))

#using F-Strings
print(f'num1 is {num1:.4f} and num2 is {num2:.4f}')
