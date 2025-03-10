from sentence_Smash import smash
from rock_paper_scissors import rps
from opposite_number import opposite
from calculate_average import find_average
from abbreviate_a_two_word_name import abbrev_name


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
