import pytest
from triangle import TriangleClassifier

# 1. Triângulo escaleno válido
def test_scalene_valid():
    assert TriangleClassifier.classify(3, 4, 5) == "Escaleno"

# 2. Triângulo isósceles válido
def test_isosceles_valid():
    assert TriangleClassifier.classify(5, 5, 3) == "Isósceles"

# 3. Triângulo equilátero válido
def test_equilateral_valid():
    assert TriangleClassifier.classify(4, 4, 4) == "Equilátero"

# 4. Pelo menos 3 CTs para isósceles válido contendo a permutação dos mesmos valores
@pytest.mark.parametrize("a, b, c", [
    (5, 5, 3),
    (5, 3, 5),
    (3, 5, 5)
])
def test_isosceles_permutations(a, b, c):
    assert TriangleClassifier.classify(a, b, c) == "Isósceles"

# 5. Um valor zero
def test_one_zero_value():
    assert TriangleClassifier.classify(0, 4, 5) == "Inválido"

# 6. Um valor negativo
def test_one_negative_value():
    assert TriangleClassifier.classify(-1, 4, 5) == "Inválido"

# 7 e 8. A soma de 2 lados é igual ao terceiro lado (e suas permutações)
@pytest.mark.parametrize("a, b, c", [
    (2, 2, 4),
    (2, 4, 2),
    (4, 2, 2)
])
def test_sum_equals_third_side_permutations(a, b, c):
    assert TriangleClassifier.classify(a, b, c) == "Inválido"

# 9 e 10. A soma de 2 lados é menor que o terceiro lado (e suas permutações)
@pytest.mark.parametrize("a, b, c", [
    (1, 2, 4),
    (1, 4, 2),
    (4, 1, 2)
])
def test_sum_less_than_third_side_permutations(a, b, c):
    assert TriangleClassifier.classify(a, b, c) == "Inválido"

# 11. Um CT para os três valores iguais a zero
def test_all_zeros():
    assert TriangleClassifier.classify(0, 0, 0) == "Inválido"