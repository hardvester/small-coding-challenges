test_array = [1,2,3,4]

def test_func(test_array, counter = 0):
    if counter == len(test_array):
        return
    print(test_array[counter])
    counter += 1
    test_func(test_array, counter)

test_func(test_array)

