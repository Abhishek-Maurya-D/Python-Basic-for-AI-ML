a = 5
b = 10
sum = a + b


# Normal formatting
print("language is {}".format("Python"))
print("Sum of {} & {} is {}".format(a, b, sum))

# Index Based formatting
print("Sum of {1} & {0} is {2}".format(a, b, sum))

#value based formatting
print("{a} values of vars {a} & {b}".format(a=4, b=5))