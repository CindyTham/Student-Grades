#Student Portal - Percentage converted to grade

print('Welcome to the Student Portal, here, we can calculate and convert your target percentage mark into a grade. Firstly let me get your name?')
name = input('')
print('OK ' + name)
targetpercentage = input("Enter your target percentage (numerical value only)")
targetpercentage = int (targetpercentage)
actualpercentage = input("Enter your actual percentage (numerical value only)") 
actualpercentage = int (actualpercentage)

#Grade Calculations

if actualpercentage <= 59:
    print('Unfortunately ' + name)
    print ('This is a Grade F')

#Meet Target?
    if targetpercentage < actualpercentage:
      print("You have met your target, however this classification is a Fail.")
    if actualpercentage == targetpercentage:
      print("You have achieved your target grade, however this classification is a Fail. ")
    if targetpercentage > actualpercentage:
      print("I am sorry, you did not meet your target grade and this classification is a Fail.")
      
if 60 <= actualpercentage <= 69:
    print('Your grades have been calculated '+ name)
    print ('This is a Grade D')

#Meet Target?
    if targetpercentage < actualpercentage:
      print("You met your target grade and performed better than predicted.")
    if actualpercentage == targetpercentage:
      print("You have achieved your target grade.")
    if targetpercentage > actualpercentage:
      print("I am sorry, you did not meet your target grade")
      
if 70 <= actualpercentage <= 79:
    print( 'Your grades have been calculated '+ name)
    print ('This is a Grade C')
    
#Meet Target?
    if targetpercentage < actualpercentage:
      print("Well done, you met your target grade.")
    if actualpercentage == targetpercentage:
      print("You have achieved your target grade.")
    if targetpercentage > actualpercentage:
      print("I am sorry, you did not meet your target grade")
      
if 80 <= actualpercentage <= 89:
    print( 'Your grades have been calculated '+ name)
    print ('This is a Grade B')

#Meet Target?
    if targetpercentage < actualpercentage:
      print("Well done you met your target grade.")
    if actualpercentage == targetpercentage:
      print("You have achieved your target grade.")
    if targetpercentage > actualpercentage:
      print("I am sorry, you did not meet your target grade")
      
if 90 <= actualpercentage <= 100:
    print('WELL DONE! ' + name)
    print ('This is a Grade A')

#Meet Target?
    if targetpercentage < actualpercentage:
      print("Excellent, you met your target grade.")
    if actualpercentage == targetpercentage:
      print("Good Job, You have achieved your target grade.")
    if targetpercentage > actualpercentage:
      print("I am sorry, you did not meet your target grade")

