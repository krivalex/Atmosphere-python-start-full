toDoFile = open("todo.txt", "a")
print(toDoFile)

toDoItem = ""

while toDoItem != "esc":
    toDoItem = input("Enter the task: ")
    toDoFile.write(toDoItem + "\n")
toDoFile.close()
