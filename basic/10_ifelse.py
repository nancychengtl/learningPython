#布林值判斷
bool_one = 3 < 5 #會print True

bool_two = True and True #and, or 是布林運算，直接打文字

#or只要其一為True就是True

bool_five = not not False #not為補集

#判斷順序：not -> and -> or
#if 判斷
def using_control_once():
    if 1+1 == 2: #回傳True則往下執行
        return "Success #1"

def using_control_again():
    if 1+3 == 4:
        return "Success #2"

print using_control_once()
print using_control_again()

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:
        return  False      # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False    # Make sure this returns False
#if else if
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4) #output: 1
print greater_less_equal_5(5) #output: 0
print greater_less_equal_5(6) #output: -1
#字串+判斷
original = raw_input('Enter a word:') #將使用者輸入的字串存在original


if len(original) > 0 and original.isalpha(): #判斷是否為字母且長度>0
    word = original.lower()
    first = word[0]
    new_word = word + first
    new_word = new_word[1: len(new_word)] #取字串從1到new_word長度的字串
    print new_word
else:
    print 'empty'

#綜合判斷
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()