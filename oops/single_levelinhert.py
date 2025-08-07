####single level inheritance

class College:
    def open(self):
        return 'college open'
    
    
class Student(College):
    def msg(self):
        return 'class started'
    
obj = Student()
print(obj.msg())
print(obj.open())        