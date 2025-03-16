from kyu8.sentence_Smash import smash
from kyu8.opposite_number import opposite
from kyu8.rock_paper_scissors import rps
from kyu8.calculate_average import find_average
from kyu8.abbreviate_a_two_word_name import abbrev_name
from kuy7.sum_of_odd_numbers import row_sum_odd_numbers
from kuy7.reverse_words import reverse_words
from kuy7.ones_and_zeros import binary_array_to_number
from kuy7.number_of_people_in_the_bus import number
from kuy7.jaden_casing_strings import to_jaden_case

user_input = ('hello', 'world', 'this', 'is', 'great')
result = smash(user_input)
print(result)


user_input1 = ("scissors")
user_input2 =("paper")
result1 = rps(user_input1,user_input2)
print(result1)


user_input3 = (1)
result3 = opposite(user_input3)
print(result3)


user_input4 = [2, 5, 6]
result4 = find_average(user_input4)
print(result4)


user_input5 = ("Sam Harris")
result5 = abbrev_name(user_input5)
print(result5)


us_imp1 = 5
result = row_sum_odd_numbers(us_imp1)
print(result)


us_imp2 = ("This is an example!")
result2 = reverse_words(us_imp2)
print(result2)


us_imp3 = [0, 0, 1, 0]
result3 = binary_array_to_number(us_imp3)
print (result3)


us_imp4 = [[10,0],[3,5],[5,8]]
result4 = number(us_imp4)
print(result4)


us_imp5 = ("How can mirrors be real if our eyes aren't real")
result5 = to_jaden_case(us_imp5)
print(result5)
