import unittest
import employee_management


class UnitTestEmployeeManagement(unittest.TestCase):
    def test_employee_class(self):
        emp1=employee_management.Employee("James",20,39,"HR")
        self.assertTrue(emp1.id>0)
        self.assertTrue(emp1.age>0)
        self.assertIsInstance(emp1.name,str)
        self.assertIsInstance(emp1.dep,str)
    
    def test_add_employee(self):
        org=employee_management.EmployeeManagement()
        emp1=employee_management.Employee("James",20,39,"HR")
        org.add_employee(emp1)
        emp1test=[{'name':'James','id':20,'age':39,'departement':'HR'}]
        self.assertTrue(all(x in org.employees for x in emp1test)) #I found this on the internet and have little clue on how it works
        
        
        
