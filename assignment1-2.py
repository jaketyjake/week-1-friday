#find the largest element in array
#array= [324523452352345,12, 123,1234,12345,123456,1234567]
#order = sorted(array)
#print(order[-1])

#rewrote without using any built in functions to sort
array = [324523452352345,12, 123,1234,12345,123456,1234567]
new_array =[]
while array:
    lowest = array[0]
    for number in array:
        if number < lowest:
            lowest = number
    new_array.append(lowest)
    array.remove(lowest)        
print(new_array[-1])



