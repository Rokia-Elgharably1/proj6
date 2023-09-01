import statistics
import math


################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None  #val = None: Initializes a variable val with the value None.  NULL has no value at all

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None

  return val

################ Main Program ################
# Initialize user input variable for menu option
option = ""

# Initialize dictionary for student list
studentList = {}

# Display menu to prompt user
print()
displayMenu()

# Function for Option 1: Adding student
def addStudent(studentList):
  
  student = input("Input student name to add: ")

  #The student's name is used as the key, and an empty list [] is assigned as the value. This is a common way to initialize a list that will store additional information about the student.
  studentList[student] = []
  
  print()
  print(f"{student} has been successfully added.")

# Function for Option 2: Deleting student 
def deleteStudent(studentList):
  
  student = input("Input student name to delete: ")

  # check if student is in studentList and remove 
  if student in studentList:
    removedStudent = studentList.pop(student)
    print()
    print(f"{removedStudent} has been deleted.\n")

  else:
    print("Student not found.\n")
    student = input("Input student name to delete: ")


  # Function for Option 3: Adding student grade to list
def addStudentGrade(studentList):
  
  student = input("Input student name: ")

  if student in studentList:
    grade = getNumberGradeFromUser()
    studentList[student].append(grade)
    print("Grade successfully added.")

# Function for Option 4: Listing student grades
def listStudentGrade(studentList):
  
  student = input("Input student name: ")

  # If student is in student list: print key / value pairs
  if student in studentList:
    grades = studentList[student]
    print(f"{student}: {grades}")
    
  else: 
    print("No student grades available")



# Function for Option 5: Getting student letter grade
def getStudentLetterGrade(studentList):
  
  student = input("Input student name: ")

  # Check if student is in list and get values from pair
  if student in studentList:
    grades = studentList[student]

    # Average values with statistics
    averageGrade = statistics.mean(grades)

    # return letter grades
    if (averageGrade >= 90):
      return "A"
    elif (averageGrade >= 80):
      return "B"
    elif (averageGrade >= 70):
      return "C"
    elif (averageGrade >= 60):
      return "D"
    else:
      return "F"
      
  else: 
    return "Student not found."

# Application Loop
while(option.lower() != "exit"):
  option = input("Please select an option: ")
  print()

# Option 1: Add student
  if (option == "1"):
    addStudent(studentList)
    print()
  
  # Option 2: Remove a student
  elif (option == "2"):
    deleteStudent(studentList)
    print()
  
  # Option 3: Add quiz grade for student
  elif (option == "3"):
    addStudentGrade(studentList)
    print()
  
  # Option 4: List student's quiz grades
  elif (option == "4"):
    listStudentGrade(studentList)
    print()
  
  # Option 5: Get student's letter grade
  elif (option == "5"):
    letterGrade = getStudentLetterGrade(studentList)
    print(f"\nLetter grade: {letterGrade}")

  # Option 6: Quit
  elif (option == "6"):
    print("Goodbye.")
    print()
    break

  print()
  displayMenu()