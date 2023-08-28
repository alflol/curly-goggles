import re
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# TODO: replace None with appropriate code
# split verse into list of words
verse_list = verse.split(" ")
verse_list2 = re.split(r'\s+', verse)

# TODO: replace None with appropriate code
# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# TODO: replace None with appropriate code
# find the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = 'breathe' in verse_dict.keys()
print(contains_breathe)

sorted_keys = sorted(list(verse_dict.keys()))
print(sorted_keys)
print(sorted_keys[-1])

with open('actors_list.txt') as f:
    #file_data = f.read()
    for line in f:
        print(line.split(',')[0])

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            cast_list.append(line.split(',')[0])
    return cast_list

cast_list = create_cast_list('actors_list.txt')
print(cast_list)