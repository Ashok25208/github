#Datatyoes and Operators
name = 'ashok'
print(type(name)==str)
print(len(name)==4)
print(isinstance(name,str))
print(name)
#casting
age = int("20")
print(age)
float_value = 0.6575
intFractiontoInt = int(float_value)
print(float_value)
print(intFractiontoInt)
#Operators
##assignment Operators
score = 200
print(score)
##Arithematic Operators
score = 200
score += 50
print("After adding "+ str(score))
score -= 150
print("After subtracting "+ str(score))
score *= 2
print(score)
score /= 2
print(score)
score %= 6
print(score)
score **= 2
print(int(score))
score //=3
print(score)
###Comparison Operators
Tamil = 75
English = 85
Maths = 80
Science = 85
Social_science = 90
print(Science==English)
print(Social_science >= Science)
print(English > Tamil)
print(Science < Social_science )
print(Science <= Maths )
print(Tamil != English)
### Boolean Operators
## not, or & and
status = False
Character = True
print(not status)
print("before or operation")
print(status or Character)
print("OR will always check the first operand not to be false \n and returns the other operand")
print(Character or status)
print("before and operation")
print(Character and status)
print("AND will always check the first operand to be True \n and returns other operand if condition satisfied")
print(status and Character)
##Ternary Operators
print("Ternary operator")
a = 10
b = 21
print(a) if a > b else print(b)
##String Built in Methods
name = "AshokPandianSomasundaram"
alphanumeric_name = "Ashok20"
age = "32423"
lower_name = "ashokpandiansomasundaram"
upper_name = "ASHOK"
attitude = "My thoughts are genuine"
print(name.isalpha())
print(alphanumeric_name.isalnum())
print(age.isdecimal())
print(name.lower())
print(lower_name.islower())
print(upper_name.isupper())
print(lower_name.upper())
print(name.title())
print(name.startswith("Ashok"))
print(name.endswith("ram"))
print(len(name))
print(name[0])
print(upper_name[-1])
print(attitude.strip())
print(attitude.find("are"))
print(attitude.join("* "))
print(attitude.split("t"))
print(attitude.split())
print("are" in attitude)
print("Ash\"ok")
print("Ashok\tPandian")
print("Ashok\nPandian")
print("Ashok\\Pandian")
print(lower_name[0:2])
print(lower_name[2:])
print(lower_name[1:8])
