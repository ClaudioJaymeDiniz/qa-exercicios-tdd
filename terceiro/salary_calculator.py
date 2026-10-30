from enum import Enum

class Role(Enum):
    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"

class Employee:
    def __init__(self, name: str, email: str, base_salary: float, role: Role):
        self.name = name
        self.email = email
        self.base_salary = base_salary
        self.role = role

class SalaryCalculator:
    @staticmethod
    def calculate_net_salary(employee: Employee) -> float:
        salary = employee.base_salary
        role = employee.role
        discount = 0.0

        if role == Role.DESENVOLVEDOR:
            if salary >= 3000.00:
                discount = 0.20
            else:
                discount = 0.10
        elif role in (Role.DBA, Role.TESTADOR):
            if salary >= 2000.00:
                discount = 0.25
            else:
                discount = 0.15
        elif role == Role.GERENTE:
            if salary >= 5000.00:
                discount = 0.30
            else:
                discount = 0.20
        
        net_salary = salary * (1 - discount)
        return round(net_salary, 2)