class Retangulo:
    def __init__(self, base, altura):
        self.base = abs(base)
        self.altura = abs(altura)

    def mudar_lados(self, nova_base, nova_altura):
        """Altera os valores da base e altura."""
        self.base = abs(nova_base)
        self.altura = abs(nova_altura)
        print(f"Valores alterados: Base = {self.base}, Altura = {self.altura}")

    def retornar_lados(self):
        """Retorna uma tupla com os valores da base e altura."""
        return (self.base, self.altura)

    def calcular_area(self):
        """Calcula e retorna a área do retângulo (Base * Altura)."""
        return self.base * self.altura

    def calcular_perimetro(self):
        """Calcula e retorna o perímetro do retângulo (2*Base + 2*Altura)."""
        return (2 * self.base) + (2 * self.altura)