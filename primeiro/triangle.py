class TriangleClassifier:
    @staticmethod
    def classify(a: int, b: int, c: int) -> str:
        """Classifica um triângulo com base nos lados inteiros a, b e c."""
        # Verifica se algum lado é menor ou igual a zero
        if a <= 0 or b <= 0 or c <= 0:
            return "Inválido"
        
        # Verifica a condição de existência do triângulo (desigualdade triangular)
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return "Inválido"
        
        # Classificação do triângulo
        if a == b == c:
            return "Equilátero"
        elif a == b or b == c or a == c:
            return "Isósceles"
        else:
            return "Escaleno"