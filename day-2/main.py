def get_input():
    with open('2-input.txt', 'r') as file:
        return file.readline().split(',')

def compute(array, pos):
    if array[pos] == str(99):
        return 0
    else:
        array[pos + 3] = int(array[pos + 1]) + int(array[pos + 2])
        print(array[pos +3])
        return 4

list = get_input()

pos = 0
while pos <= list.__len__():
    result = compute(list, pos)
    if result == 0:
        break
    else: pos += result

print(list[0])