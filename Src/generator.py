import random
# generate function will select a random character for either num, letter, or symbol
def generate(num,list):
    list_of_char = []
    for number in range(0,num):
        # random.randint will select a random char bases on index
        random_index = random.randint(0,(len(list) -1))
        list_of_char.append(list[random_index])
    return list_of_char



