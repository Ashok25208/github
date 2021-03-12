# basic string print in python 3
firstProgram = 'Arun'
age = 34
print(firstProgram +" age is "+ str(age));
# basic if condition
if firstProgram == 'Arun':
 print('Ashok');
 print("This is " + firstProgram + "'s age.");
else:
 print('---Arun----');
#nested if-else condition
if firstProgram == 'Ashok':
 print('Ashok');
 print("This is ashok's age.");
elif age > 35:
 print('Arun');
else:
 print('******Aashu******');
#basic for loop
import json
dic_data = {
            "name" : "Jenny",
            "age" : 25,
            "profession" : "developer",
            "skill set" : ("C" ,"CPP", "JAVA", "PYTHON"),
            "previous experience" : None,
            "academic details" : [
                                  {"qualification" : "UG" , "score" : 7.5 },
                                  {"qualification" : "HSC" , "score" : 90}
                                  ]
            }
json_data = json.dumps(dic_data)
print(json_data)
print(json.dumps(dic_data, indent=2))
print(json.dumps(dic_data, indent=4))
print(json.dumps(dic_data, indent=6))
