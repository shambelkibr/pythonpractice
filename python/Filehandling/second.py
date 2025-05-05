with open("second.text","w") as file:
    file.write("this file handling exercise")
    
with open("second.text","r")as file:
    content=file.read()
    print(content)
    
    