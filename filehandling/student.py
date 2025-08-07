def demo():
    n = int(input("Enter the number of students: "))
    
    for i in range(n):
        
        f = open("demo.txt","a")
        name= input("Enter the student name: ")
        age = int(input("Enter the students age: "))
        place = input("Enter the place")
       
        f.write(f"\nStudent name is {name} \nPlace is {place} \nAge is {age}")
        f.close
      
    
demo()

