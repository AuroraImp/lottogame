name =input("Your Name: ")
cash= 1000
print ("Hello %s. Welcome to Lotto Game. Your Current Cash is $%d" %(name,cash))


while cash>0:
    
    

    while True:
        try:
            bet = int(input('Your Bet: '))
            if bet > cash:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("You have not enough cash. Your cash is $%d" %cash)

    cash=cash-bet

    while True:
        try:
            luckynum = int(input('Enter Lucky Number: '))
            if luckynum < 1 or luckynum > 40:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("Invalid Number. The number must be in the range of 1-40.")



    while True:
        try:
            num1 = int(input('Enter First Number: '))
            if num1 == luckynum:
                raise ValueError

            if num1 < 1 or num1 > 40:
                raise ValueError
            break
        except ValueError:
            print("Invalid Number. Number must be 1-40 and Do not enter same numbers.")
       
    while True:
        try:
            num2 = int(input('Enter Second Number: '))
            if num2 == luckynum or num2 == num1:
                raise ValueError

            if num2 < 1 or num2 > 40:
                raise ValueError
            break
        except ValueError:
            print("Invalid Number. Number must be 1-40 and Do not enter same numbers.")
       

    while True:
        try:
            num3 = int(input('Enter Third Number: '))
            if num3 == luckynum or num3 == num1 or num3 == num2:
                raise ValueError

            if num3 < 1 or num3 > 40:
                raise ValueError
            break
        except ValueError:
            print("Invalid Number. Number must be 1-40 and Do not enter same numbers.")

    while True:
        try:
            num4 = int(input('Enter Fourth Number: '))
            if num4 == luckynum or num4 == num1 or num4 == num2 or num4 == num3:
                raise ValueError

            if num4 < 1 or num4 > 40:
                raise ValueError
            break
        except ValueError:
            print("Invalid Number. Number must be 1-40 and Do not enter same numbers.")

    while True:
        try:
            num5 = int(input('Enter Fifth Number: '))
            if num5 == luckynum or num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
                raise ValueError

            if num5 < 1 or num5 > 40:
                raise ValueError
            break
        except ValueError:
            print("Invalid Number. Number must be 1-40 and Do not enter same numbers.")


    print("You bet %d. Lucky Number: %d and Others Number: %d, %d, %d, %d, %d" %(bet,luckynum,num1,num2,num3,num4,num5))
    print("Lotto starts draw now")

    import random
    v1,v2,v3,v4,v5,v6 = random.sample(range(1,21),6)
    print ("Lucky Number: %s,Others Number%s,%s,%s,%s, %s." %(v1,v2,v3,v4,v5,v6))

    list1 = [v1,v2,v3,v4,v5,v6]
    list2 = [num1,num2,num3,num4,num5]
    list3 = [luckynum]
     
    s1 = set(list1)&set(list3)
    s2 = set(list1)&set(list2)

    if len(s1)+len(s2) == 6:
         win=(bet*10000)
         cash=win+cash
         print ("You have won jackpot $%d. Your current cash is now %d" % (win,cash))

    if len(s2)==5:
         win=(bet*2000)
         cash=win+cash
         print ("Five number match without lucky number. You have won $%d. Your current cash is now %d" % (win,cash))

    if len(s1)+len(s2) == 5:
         win=(bet*1000)
         cash=win+cash
         print ("Five number match with lucky number. You have won $%d.  Your current cash is now %d" % (win,cash))

    if len(s1)+len(s2) == 4:
         win=(bet*100)
         cash=win+cash
         print ("Four number match. You have won $%d.  Your current cash is now %d" % (win,cash))

    if len(s1)+len(s2) == 3:
         win=(bet*2)
         cash=win+cash
         print ("Three number match. You have won $%d.  Your current cash is now %d" % (win,cash))

    if len(s1)+len(s2) == 2:
         win=(bet*.5)
         cash=win+cash
         print ("Two number match. You have won $%d.  Your current cash is now %d" % (win,cash))

    if len(s1)+len(s2) == 1 or len(s1)+len(s2) == 0:
         win=(bet*0)
         cash=win+cash
         print ("One number match. You have won $%d.  Your current cash is now %d" % (win,cash))

    if cash<1:
            print("You have not any cash. Go study")
