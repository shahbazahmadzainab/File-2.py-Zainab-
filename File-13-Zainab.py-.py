# Create a file named data.txt, write 3 lines of text in it using write mode, then close the file.
file = open("data.txt", "w")
file.write("Hello, world!\n")
file.write("My name is Alice.\n")
file.write("Allah Hafiz, World!\n")
file.close()
# Open data.txt in read mode, read all lines, and print each line one by one.
file = open("data.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()
# Use readlines() to read all lines and print each line with it's line number.
file = open("data.txt", "r")
lines = file.readlines()
i = 0
for line in lines:
    print(f"{i} : {line}")
    i += 1
file.close()
# Open data.txt in append mode, add a new line, then read and print the updated content.
file = open("data.txt", "a")
file.write("This is the new appended line.\n")
file.close()
file = open("data.txt", "r")
updated_lines = file.readlines()
for line in updated_lines:
    print(line.strip())
file.close()
# Use with open() statement to open file in read mode, and use a loop to print each line with numbers.
with open("data.txt", "r") as file:
    content = file.readlines()
for i, line in enumerate(content, start=1):
    print(f"{i} : {line.strip()}")
# Create numbers.txt, write numbers 1 to 10 (one per line), read file and print the sum of all numbers.
with open("numbers.txt", "w") as file:
    for num in range(1, 11):
        file.write(f"{num}\n")
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print("sum of numbers:", total)
# Create even_numbers.txt and write all even numbers from 1 to 50 using a loop.
file = open("even_number.txt", "w")
for i in range(2, 50, 2):
    file.write(str(i) + "\n")
file.close()
with open("even_number.txt", "r") as file:
    even_numbers = file.readlines()
    for i, number in enumerate(even_numbers, start=1):
        print(f"{i} ; {number.strip()}")
# Create students.txt and write names of students. Read file, print names with character count using len().
file = open("student.txt", "w")
names = ["Ayesha \n", "Zainab \n", "Seerat \n", "Farwa \n", "Shumaiza \n"]
file.writelines(names)
file.close()
file = open("student.txt", "r")
data = file.readlines()
print("Student Names :")
for i, line in enumerate(data, start=1):
    print(f"{i} : {line} and the lenght of the name is {len(line.strip())}\n")
# Read info.txt, check if "Python" exists. If true, print "Python found", else print "Not found".
with open("info.txt", "r") as file:
    content = file.read()
    if "Python" in content:
        print("Python found")
    else:
        print("Not found")
# Read a file, convert all text to uppercase, write to output.txt.
with open("data.txt", "r") as file:
    content = file.read()
with open("output.txt", "w") as file:
    file.write(content.upper())
print("Uppercase text:")
print(content.upper())