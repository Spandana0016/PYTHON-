

def funct1(): 
    print("Normal Func()")

def funct2(course,name,id):
    print("My name is",name,"my Id is", id,"My Courseis",course)    
    print(f"I Have an ID :{id} and My name is {name} I Have Selected Course {course}") 

funct1()
# Key Word Argument
funct2(course="python",name="sweety",id=1)    
# Positioned Arguments
funct2("Python","sweety",1)

def funct3(*ards):
    print(f"This is My Third No {args[2]}")

funct3(1,2,3,4,5)



def keyfunc3(**args):
    print(f"Hello {args["name"]} and my age is {args["age"]}")

keyfunc3(name="sweety", age=18) 

def functiPosit(name,/):
    print(f" Hello {name}")

functiPosit("sweety")    
# functiPosit(name="sweety")

def funckey(*,ui):
    print(f" This is my design {ui}")

funckey(ui="Developer")    


def funckey1(*,a,b,**ui):
    print(f"This is my design: {ui}")
    print(f"Required parameters: a = {a}, b = {b}")

funckey1(a=1, b=2, c="test", d=4)    

