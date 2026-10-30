import re
from typing import List
from models import Person

class PersonDAO:
    def save(self, p: Person) -> None:
        """Simula a persistência se o objeto for válido."""
        errors = self.isValidToInclude(p)
        if errors:
            raise ValueError(f"Person inválida: {errors}")
        # Lógica de salvamento real viria aqui

    def isValidToInclude(self, p: Person) -> List[str]:
        errors = []

        # 1. Validação do Nome: ao menos 2 partes e composto apenas de letras
        if not p.name:
            errors.append("O nome não pode estar vazio.")
        else:
            parts = p.name.strip().split()
            if len(parts) < 2:
                errors.append("O nome deve ser composto por ao menos 2 partes.")
            
            # Verifica se cada parte é composta exclusivamente por letras (sem números ou caracteres especiais)
            for part in parts:
                if not part.isalpha():
                    errors.append("O nome deve ser composto apenas de letras.")
                    break

        # 2. Validação da Idade: intervalo [1, 200]
        if not (1 <= p.age <= 200):
            errors.append("A idade deve estar no intervalo entre 1 e 200.")

        # 3. Validação de Emails: pelo menos um objeto Email associado
        if not p.emails or len(p.emails) == 0:
            errors.append("A pessoa deve ter pelo menos um email associado.")
        else:
            # 4. Formato do Email: "_____@____._____", cada parte com ao menos um caractere
            # Expressão regular para garantir formato parte@parte.parte (com subpartes opcionais no domínio)
            email_regex = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
            for email in p.emails:
                if not re.match(email_regex, email.name):
                    errors.append(f"O email '{email.name}' está em um formato inválido.")
                    break

        return errors