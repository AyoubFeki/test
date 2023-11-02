import unittest
import employee_management
class IntegTestEmployeeManagement(unittest.TestCase):
    def fire_employee_test(self):
        org=employee_management.EmployeeManagement()
        emp1=employee_management.Employee("James",20,39,"HR")
        emp2=employee_management.Employee("Jack",20,50,"IT")
        emp1test=[{'name':'James','id':20,'age':39,'departement':'HR'}]
        self.assertTrue(all(x in org.employees for x in emp1test)) 
        org.add_employee(emp1)
        org.add_employee(emp2)
        org.fire_employee(emp1)
        self.assertFalse(all(x in org.employees for x in emp1test)) 
    def find_employee(self):
        org=employee_management.EmployeeManagement()
        emp1=employee_management.Employee("James",20,39,"HR")
        emp2=employee_management.Employee("Jack",20,50,"IT")
        emp1test=[{'name':'James','id':20,'age':39,'departement':'HR'}]
        org.add_employee(emp1)
        org.add_employee(emp2)
        self.assertTrue(emp1test==org.find_employee(20))
