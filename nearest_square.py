def nearest_square(limit):
    result = 0
    computed = 0
    i = 0
    while(computed < limit):
        result = computed 
        i+=1
        computed = i**2
    return result
        
test_1 = nearest_square(40)

print('expected result: 36, actual result: {}'.format(test_1))