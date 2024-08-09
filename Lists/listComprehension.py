# new_list = [new_item for item in list]
prev_list = [1,2,3]
new_list = [i * 2 for i in prev_list]
print(prev_list)
print(new_list)

language = 'Python'
new_list = [letter for letter in language]
print(new_list)

# Conditional List Comprehension
print('Conditional List Comprehension')
# new_list = [new_item for item in list if condition]
prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list = [number*number for number in prev_list if number < 0]
print(new_list)

sentence = 'My name is Zoltan'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
print(is_consonant('a'))

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

# we can also use functions
def get_number(number):
    return number if number > 0 else 'negative num'

prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
# if the number is > 0 then it will replace it wih 'negative num' otherwise it shows the number
new_list = [get_number(number) for number in prev_list]
print(new_list)

prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
# if the number is > 0 then it will replace it wih 'negative num' otherwise it shows the number
new_list = [number if number > 0 else 'negative num' for number in prev_list]
print(new_list)