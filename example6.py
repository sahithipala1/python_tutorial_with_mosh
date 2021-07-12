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
    
    
z=[1,2,3,4,5,6]
z.append(6)
z.insert(0,-1)
z.remove(6)
print(z)
print( 1 in z)
print(len(z))

k = [1,2,3,4,5,6]

for item in k :
    print(item)
    
    
    
j= 0 
while j < len(z):
    print(z[j])
    j = j + 1    