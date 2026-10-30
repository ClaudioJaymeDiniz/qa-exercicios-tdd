import pytest
from salary_calculator import Employee, Role, SalaryCalculator

# 1. Testes para DESENVOLVEDOR
def test_developer_high_salary():
    # Salário >= 3000.00 (desconto de 20%) -> 4000.00 - 20% = 3200.00
    emp = Employee("Alice", "alice@dev.com", 4000.00, Role.DESENVOLVEDOR)
    assert SalaryCalculator.calculate_net_salary(emp) == 3200.00

def test_developer_low_salary():
    # Salário < 3000.00 (desconto de 10%) -> 2500.00 - 10% = 2250.00
    emp = Employee("Bob", "bob@dev.com", 2500.00, Role.DESENVOLVEDOR)
    assert SalaryCalculator.calculate_net_salary(emp) == 2250.00

# 2. Testes para DBA
def test_dba_high_salary():
    # Salário >= 2000.00 (desconto de 25%) -> 3000.00 - 25% = 2250.00
    emp = Employee("Carlos", "carlos@dba.com", 3000.00, Role.DBA)
    assert SalaryCalculator.calculate_net_salary(emp) == 2250.00

def test_dba_low_salary():
    # Salário < 2000.00 (desconto de 15%) -> 1500.00 - 15% = 1275.00
    emp = Employee("Diana", "diana@dba.com", 1500.00, Role.DBA)
    assert SalaryCalculator.calculate_net_salary(emp) == 1275.00

# 3. Testes para TESTADOR
def test_tester_high_salary():
    # Salário >= 2000.00 (desconto de 25%) -> 2500.00 - 25% = 1875.00
    emp = Employee("Eva", "eva@test.com", 2500.00, Role.TESTADOR)
    assert SalaryCalculator.calculate_net_salary(emp) == 1875.00

def test_tester_low_salary():
    # Salário < 2000.00 (desconto de 15%) -> 1800.00 - 15% = 1530.00
    emp = Employee("Frank", "frank@test.com", 1800.00, Role.TESTADOR)
    assert SalaryCalculator.calculate_net_salary(emp) == 1530.00

# 4. Testes para GERENTE
def test_manager_high_salary():
    # Salário >= 5000.00 (desconto de 30%) -> 6000.00 - 30% = 4200.00
    emp = Employee("Grace", "grace@manager.com", 6000.00, Role.GERENTE)
    assert SalaryCalculator.calculate_net_salary(emp) == 4200.00

def test_manager_low_salary():
    # Salário < 5000.00 (desconto de 20%) -> 4000.00 - 20% = 3200.00
    emp = Employee("Heitor", "heitor@manager.com", 4000.00, Role.GERENTE)
    assert SalaryCalculator.calculate_net_salary(emp) == 3200.00