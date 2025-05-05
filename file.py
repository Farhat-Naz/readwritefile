with open("demo.txt","w") as file:
    file.write("Hello world")
    file.write("\nHow are you")

with open("demo.txt","r") as file:
    print("content")
    print(file.read())    

    

with open("demo.txt","w") as file:
    file.write("this append a new word")    