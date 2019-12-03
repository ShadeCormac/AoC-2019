def get_input():
    with open('2-input.txt', 'r') as file:
        return list(map(int,file.readline().split(',')))

def compute(array, pos):
    if int(array[pos]) == 99:
        return 0
    else:
        result = 0
        result_2 = 0
        if array[pos] == 1:
            result_2 = array[array[pos + 1]] + array[array[pos + 2]]
            result = 100*array[array[pos + 1]] + array[array[pos + 2]]
        else: 
            result_2 = array[array[pos + 1]] * array[array[pos + 2]]
            result = 100*array[array[pos + 1]] * array[array[pos + 2]]
        array[array[pos + 3]] = result_2
        print(result)
        if result == 19690720:
            print('noun: ' + str(array[array[pos + 1]]))
            print('verb: ' + str(array[array[pos + 2]]))
        return 4

input_list = get_input()
pos = 0
while pos <= input_list.__len__():
    result = compute(input_list, pos)
    if result == 0:
        break
    else: 
        pos += result
        input_list = get_input()

