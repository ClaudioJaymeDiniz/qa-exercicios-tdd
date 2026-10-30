# Trabalho de Teste de Software - FATEC SJC

Repositório contendo a implementação e os testes automatizados em Python utilizando **pytest** para os três exercícios solicitados na disciplina de Qualidade e Teste de Software.

## Estrutura do Projeto
- **Exercício 1:** Classificação de Triângulos (`triangle.py`)
- **Exercício 2:** Validação de Dados de Pessoas e Emails (`person_dao.py`, `models.py`)
- **Exercício 3:** Calculadora de Salários por Cargo (`salary_calculator.py`)

## Instalação e Configuração
1. Clone o repositório e acesse a pasta do projeto.

2. Crie e ative um ambiente virtual (`venv`):
   ```bash
   python -m venv venv
   # No Windows (CMD): venv\Scripts\activate.bat
   # No Linux/Mac: source venv/bin/activate

3. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt

4. Execução dos Testes e Cobertura
Para rodar todos os testes de uma vez e verificar as evidências de cobertura com o pytest-cov:
    ```bash
    pytest --cov=. --cov-report=term-missing