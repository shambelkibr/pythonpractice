# Creating and writing to a file
with open('frist.text', 'w') as file:
    file.write('Hello, world!\n')
    file.write('This is a file handling example.\n')

# Reading from a file
with open('frist.text', 'r') as file:
    content = file.read()
    print(content)

# Appending to a file
with open('frist.text', 'a') as file:
    file.write('Appending a new line.\n')

# Reading the updated file
with open('frist.text', 'r') as file:
    updated_content = file.read()
    print(updated_content)
