#string宣告
nancy = "hello world"

#跳脫字元
nancy = "it/'s"

#MONTY字元的[4]
fifth_letter = "MONTY"[4]

#計算string 長度
len(nancy) #長度, nancy是一個字串變數名, 如果直接是字串, 則要改成"Nancy"

#String轉為小寫
print nancy.lower()
print nancy.upper() #大寫

#將非字串的轉為字串
pi = 3.14
print str(pi)

#字串的組合
M = "Spam "+"and "+"eggs"
print "The value of pi is around " + str(3.14)

#判斷是不是字串
if M.isalpha() == True:
    print M

#input and output string
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Your name is %s, your quest is %s, " \
"and your favorite color is %s." %(name, quest, color)