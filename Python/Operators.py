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
