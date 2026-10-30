import pytest
from models import Person, Email
from person_dao import PersonDAO

@pytest.fixture
def dao():
    return PersonDAO()

def test_valid_person(dao):
    # Cenário totalmente válido
    email = Email(1, "teste@exemplo.com")
    person = Person(1, "João Silva", 25, [email])
    
    errors = dao.isValidToInclude(person)
    assert len(errors) == 0

def test_name_less_than_two_parts(dao):
    # Nome com apenas uma parte
    email = Email(1, "teste@exemplo.com")
    person = Person(1, "João", 25, [email])
    
    errors = dao.isValidToInclude(person)
    assert any("2 partes" in err for err in errors)

def test_name_with_numbers_or_symbols(dao):
    # Nome contendo números ou caracteres inválidos
    email = Email(1, "teste@exemplo.com")
    person = Person(1, "João Silv@1", 25, [email])
    
    errors = dao.isValidToInclude(person)
    assert any("apenas de letras" in err for err in errors)

@pytest.mark.parametrize("invalid_age", [0, -5, 201])
def test_invalid_age_range(dao, invalid_age):
    # Idade fora do intervalo [1, 200]
    email = Email(1, "teste@exemplo.com")
    person = Person(1, "João Silva", invalid_age, [email])
    
    errors = dao.isValidToInclude(person)
    assert any("idade" in err.lower() for err in errors)

def test_person_without_emails(dao):
    # Pessoa sem nenhum objeto email associado
    person = Person(1, "João Silva", 25, [])
    
    errors = dao.isValidToInclude(person)
    assert any("pelo menos um email" in err for err in errors)

@pytest.mark.parametrize("invalid_email_str", [
    "joao@com",       # Falta o ponto da extensão
    "joao.com",       # Falta o @
    "@exemplo.com",   # Falta a parte antes do @
    "joao@.com",      # Falta o nome do domínio
    "joao@exemplo"    # Falta o domínio final (.com)
])
def test_invalid_email_format(dao, invalid_email_str):
    # Email fora do padrão "_____@____._____"
    email = Email(1, invalid_email_str)
    person = Person(1, "João Silva", 25, [email])
    
    errors = dao.isValidToInclude(person)
    assert any("formato inválido" in err for err in errors)