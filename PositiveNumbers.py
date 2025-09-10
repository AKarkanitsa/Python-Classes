# compute average of positive numbers

numbers = [-3, 5, -2, 1, -8, -6, 90, -45]
count = 0
sum = 0
for value in numbers :
    if value > 0 :
        count = count + 1
        sum = sum + value

if (count == 0) :
    print("There are no positive numbers in the given collection")
else:
    print('Average of positive numbers is', sum/count)





