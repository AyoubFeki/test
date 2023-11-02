

class Employee:
    def __init__(self, name=None, id=None, age=None, dep=None):
        if not (name is None) and not (str(name).isdigit()):
            self.name=name
        else:
            raise Exception("The name cannot be a number")
        if not (id is None) and str(age).isdigit() and age>0:
            self.age=age
        else:
            raise Exception("The age must be a positive number")
        if not (age is None) and str(id).isdigit() and id>0:
            self.id=id
        else:
            raise Exception("The id must be a positive number")
        if not(dep is None) and not (str(dep).isdigit()):
            self.dep=dep
        else:
            raise Exception("The department name cannot be a number")

class EmployeeManagement:
    def __init__(self):
        self.employees= []
    
    def add_employee(self, employee):
        for i in self.employees:
            if i['id']==employee.id:
                raise Exception("This employee already exists")
                break
        self.employees.append({"name":employee.name, "id":employee.id, "age":employee.age, "departement":employee.dep})
    
    
    def find_employee(self, id):
        for i in self.employees:
            if i["id"]==id:
                return i
        return None
    def fire_employee(self, id):
        for i in range(len(self.employees)):
            if self.employees[i]['id']==id:
                del self.employees[i]
                return True
        return False





