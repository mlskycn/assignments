
left_hand = list("qwertasdfgzxcvb")
right_hand = list("yuiophjklnm")


word = input("Enter a word: ")


left_used = False
right_used = False


for letter in word:
    if letter in left_hand:
        left_used = True
    elif letter in right_hand:
        right_used = True

    
    if left_used and right_used:
        break


is_comfortable = left_used and right_used
print(is_comfortable) 