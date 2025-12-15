def greet(name,message ="good morning "):
    print (message,name)

#function call
greet("alice")
greet("bob","hello")
def student_info(name,age,course):
    print("name",name)
    print("age",age)
    print("course",course)

#calling using keywords arguments
student_info(course="python",name="amar",age=20)
def add(a,b):
    return a+b

def operate(func,x,y):
    return func (x,y)

#passing add function to operate
result = operate(add,10,5)
print("result:",result)
