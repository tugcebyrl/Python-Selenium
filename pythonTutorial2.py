# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:29:57 2023

@author: TUGCE
"""

print("*****--Student Registration System--*****")

students=[]


def findNumberOfStudents():
    global numberOfStudents
    numberOfStudents=input("How many students do you want to add?: ")
    if not numberOfStudents.isdigit():
            print("Please enter a valid number.")
    else:
        numberOfStudents = int(numberOfStudents)
        print(numberOfStudents)
        addNewStudent()
        
def addNewStudent():
    for i in range(0,numberOfStudents):
        studentName=str(input("Enter the name and surname of the student: "))
        students.append(studentName)
    print(students)
    removeStudent()
    
def removeStudent():
    removedStudent=str(input("Write the name and surname of the student to be deleted "))
    students.remove(removedStudent)
    listStudent()
    
def listStudent():
    for i in range(len(students)):
        print(students[i])
    findStudentNo()

def findStudentNo():
    studentNo=str(input("Enter the name of the student whose student number you want to know "))
    for i in range(len(students)):
        if(studentNo==students[i]):
            print("Student No: "+str(i))
            break
    removeMultipleStudents()
    
def removeMultipleStudents():
    k=0
    removedStudentsNumber = int(input("How many students do you want to remove?: "))
    while(k<removedStudentsNumber):
        k=k+1
        removedStudentNo = int(input("Enter the Student numbers to be deleted: "))
        students.remove(students[removedStudentNo])
    print(students)
    
    
    
findNumberOfStudents()

