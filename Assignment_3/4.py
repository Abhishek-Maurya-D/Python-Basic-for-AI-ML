tup = (1,7,5,9,5,6,7,2)

tup_even = ()
for i in tup:
    if i % 2 == 0:
        tup_even += (i,)

tup_odd = ()
for i in tup:
    if i % 2 != 0:
        tup_odd += (i,)

print("Tuple is : ", tup)
print("Tuple with Even Numbers : ", tup_even)
print("Tuple with Odd Numbers: ", tup_odd)