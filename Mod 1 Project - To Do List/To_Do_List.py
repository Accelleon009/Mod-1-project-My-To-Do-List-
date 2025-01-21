# Overview

# In this project, you will build a functional To-Do List Application using Python from scratch. This assignment will help you strengthen your understanding of Python concepts such as syntax, data types, control structures, functions, and error handling, all while creating a practical, interactive command-line application.

## Project

# In VS Code, create a .py file and complete the following requirements:

##  User Interface (UI) and Storage Method
# Build a simple Command Line Interface (CLI) that welcomes users and displays a menu with options to add, view, delete tasks, or quit the application.
# The tasks should be stored in a Python list

# Core Features
# Add tasks
# View tasks
# Delete tasks
# Quit the application

## User Interaction
# Use input() to capture user selections and ensure proper input validation to handle invalid choices.
# Error Handling
# Implement error handling using try, except, else, and finally blocks to catch errors
# Alert the user if they provide invalid input
# Alert the user if there are no tasks to view
# Alert the user if they try to delete a task that doesn't exist
# Alert the user if they select an option on the main menu that doesn't exist

# #Code Organization
# Organize your code into functions to improve clarity and maintainability. 
# Use descriptive function names and add comments/docstrings where necessary.
# 
##Testing and Debugging
# Thoroughly test your application, considering edge cases such as empty lists and invalid input.
 
# #Submission Guidelines:
# Ensure the code is ready to run and that all functionality, such as loops, conditionals, and functions, works as expected when executed. The goal is to have fully tested and functional code.
# Create a GitHub repository to host your project. Add, commit, and push your code to it
# Create a README.md on the repository that gives information about your project and how to run/use it
# Submit the repository link in Google Classroom.

 

import sys  # Import sys to use sys.exit()

def main():
    """Main function to handle user input and loop through menu options."""
    tasks = []
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        try:
            choice = input("Choose an option (1-4): ").strip()
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                remove_task(tasks)
            elif choice == "4":
                quit_application()
            else:
                print("Error: Invalid choice! Please enter a number between 1 and 4.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

def add_task(tasks):
    """Function to add a task to the list."""
    try:
        task = input("Enter your task: ").strip()
        if task:
            tasks.append(task)
            print(f'Task "{task}" added successfully!\n')
        else:
            print("Error: Task cannot be empty!\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

def remove_task(tasks):
    """Function to remove a task from the list."""
    try:
        if not tasks:
            print("Error: No tasks available to delete!\n")
            return
        
        task = input("What task do you want to remove? ").strip()
        if task in tasks:
            tasks.remove(task)
            print(f'Task "{task}" removed successfully!\n')
        else:
            print("Error: Task not found in the list!\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

def view_tasks(tasks):
    """Function to display the list of tasks."""
    try:
        if not tasks:
            print("Error: No tasks available!\n")
            return
        
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1): # This allows the task to be viewed in a number sequence 
            print(f"{i}. {task}")
        print()
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

def quit_application():
    """Quits the application."""
    print("Exiting application. Goodbye!")
    sys.exit()  # Allows you  properly exit the program

if __name__ == "__main__":
    main()
  
    