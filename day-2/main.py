def get_input():
    with open('2-input.txt', 'r') as file:
        return file.readline().split(',')

def compute(array, pos):
    print(pos)
    if array[pos] == 99:
        return 1
    else:
        array[pos + 3] = array[pos + 1] + array[pos + 2]
        return 4

input = get_input()
pos = 0
while pos <= input.__len__():
    pos += compute(input, pos)

print(input[0])