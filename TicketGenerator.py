import random

Row1 = []
Row2 = []
Row3 = []

Row1_Delay = False
Row2_Delay = True
Row3_Delay = False


for x in range(9):
    if Row1_Delay == True :
        Row1.append("--")
        Row1_Delay = False
    elif Row1_Delay == False :
        Row1.append(str(random.randrange(0, 100)))
        Row1_Delay = True
    
    if Row2_Delay == True :
        Row2.append("--")
        Row2_Delay = False
    elif Row2_Delay == False :
        Row2.append(str(random.randrange(0, 100)))
        Row2_Delay = True
    
    if Row3_Delay == True :
        Row3.append("--")
        Row3_Delay = False
    elif Row3_Delay == False :
        Row3.append(str(random.randrange(0, 100)))
        Row3_Delay = True

print(Row1)
print(Row2)
print(Row3)