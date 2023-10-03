number_of_hundreds = 546.34 // 100
hundreds_change = 546.34 % 100
print(round(hundreds_change, 2))

number_of_fifties = hundreds_change // 50
fifties_change = hundreds_change % 50
print(round(number_of_fifties, 2))

number_of_tens = fifties_change // 10
tens_change = fifties_change % 10
print(round(number_of_tens, 2))

number_of_fives = tens_change // 5
fives_change = tens_change % 5
print(round(number_of_fives, 2))

number_of_ones = fives_change // 1
ones_change = fives_change % 1
print(round(number_of_ones, 2))
'''
variable = 65.73 // 5
variable_change = 65.73 % 5
print(variable)
print(round(variable_change,2))
'''