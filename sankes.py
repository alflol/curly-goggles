names = input("Names please:").split(",")# get and process input for a list of names
assignments = input("assignments please:").split(",") # get and process input for a list of the number of assignments
grades = input("grades please:").split(",") # get and process input for a list of grades

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for index in range(len(names)):
    print(message.format(names[index],assignments[index],grades[index],int(assignments[index])*2+int(grades[index])))

def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("0 people in the hosue! cannot party!!")
    finally:
        return (num_each, leftovers)

try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))
   