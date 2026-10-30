# Trabalho de Teste de Software - Exercício do Triângulo

Implementação em Python utilizando o framework **pytest** para Calculadora de Salários por Cargo, acompanhada de uma suíte completa de testes unitários baseada em técnicas de TDD e análise de valores limite/partição de equivalência.

## Pré-requisitos e Instalação

1. Clone o repositório e acesse a pasta do projeto.
2. Crie e ative um ambiente virtual (`venv`):
   ```bash
   python -m venv venv
   # No Windows (CMD): venv\Scripts\activate.bat
   # No Linux/Mac: source venv/bin/activate

3. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt

4. Execução dos Testes
Para executar a suíte de testes unitários, utilize o comando:
    ```bash
    pytest

5. Para verificar a cobertura de código utilizando o pytest-cov, execute o comando abaixo:
    ```bash
    pytest --cov=salary_calculator --cov-report=term-missing