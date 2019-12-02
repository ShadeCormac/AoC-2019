import math

def calculate_fuel(mass):
    return math.trunc(mass/3) - 2

def get_total_fule(mass):
    temp = calculate_fuel(mass)
    total_mass = temp
    while(temp > 3):
        temp = calculate_fuel(temp)
        if(temp < 0):
            temp = 0
        total_mass += temp
    return total_mass

with open('1-input.txt', 'r') as input:
    sum = 0
    for line in input.readlines():
        sum += get_total_fule(int(line))
    print(sum)