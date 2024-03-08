# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    count= 0
    letters_list= []
    for letter in sequence:
        try:
            if letter < sequence[count+1]:
                letters_list.append(letter)
                count+=1
            elif letter > sequence[count+1]:
                letters_list.append(letter)
                count+=1
            else:
                count+=1
        except:
            letters_list.append(letter)

    print(letters_list) 

# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable:
#         if char != prev:
#             result.append(char)
#             prev = char
#     print(result)







unique_in_order('AAAABBBCCDAABBB') #== ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         #== ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   #== [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   #== [1, 2, 3]