def sweety():
    print("Hello Sweety")

def sanju(name):
    print(f"Hello {name}")
def func(id,name,fee,course):
    print(f"ID: {id}, Name: {name}, Fee: {fee}, Course: {course}")       

def func1(*num):
    print("This is Number",num[2])


sweety()
sanju("sanju")
func(1,"pappy",34000,"python")
func1(1,2,3,4,5,6,7)     


def funckey(name):
    print(f"Hi {name}")


def funckey1(**keys):
    print("name:", keys["lname"])


funckey(name="Ramesh")
funckey1(fname="sweety",lname="Ramesh")    


def function1(name,/):
    print(f"Your name {name}")


def function2(name):
    print(f"Your name {name}")

function2("sweety")
function2(name="ramesh")        


function1("sweety")
# function1(name="ramesh")

print("Key Argument Based -----")
def keyfunct1(*,name):
    print(f"Hello {name}")


print("Normal Function")
function2("sweety")
function2(name="sweety")

keyfunct1(name="sweety")
# keyfunct1("sweety")

def combination(id,name,/,*,course):
    print(f"ID  {id} Name {name} course {course}")

combination(1,"sweety", course="python")    
# combination(id=1,name="sweety", course="python")