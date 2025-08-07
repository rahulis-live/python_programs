#student based grade management system

class Student:
   
        def set_student_details(self):
            name = input("Enter the student name: ")
            self.__name = name
            rollno = int(input("Enter student roll no: "))
            self.__rollno = rollno
            marks = {}
            x = int(input("Enter the mark for maths "))
            marks["maths"] = x
            y = int(input("Enter the mark for science "))
            marks["science"] = y
            z = int(input("Enter the mark for englich "))
            marks["english"] = z
            
            self.__marks = marks
        def get_student_details(self):
            print(f"Name of student is {self.__name} and rollno is {self.__rollno}")
            print(self.__marks)
        def calculate_average(self):
            self.add = sum(self.__marks.values())
            self.length = len(self.__marks)
            self.avg = self.add/self.length
            print(f"Average mark is {self.avg}")
                
        def display_grade(self):
            if self.avg >= 90:
                print("Grade A")
            elif self.avg >= 80 and self.avg <=89:
                print("Grade B")    
            elif self.avg >=70 and self.avg <=79:
                print("Grade C")
            else:
                print("F")        
                
s1 = Student()
s1.set_student_details()     
s1.get_student_details()       
s1.calculate_average()  
s1.display_grade() 