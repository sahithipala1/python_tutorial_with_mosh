x= int(input("Weight :"))
unit = input("(k)gs or (L)bs : ")
if unit.upper() == "k":
    converted = x/0.45
    print("Weight in lbs:" + str(converted))
else: 
    converted = x * 0.45
    print("Weight in kgs:" + str(converted))  
    
    
i = 1
while i<= 20:
    print(i * '*')
    i = i + 2