class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, novo_lado):
        """Altera o valor do lado do quadrado."""
        self.tamanho_lado = novo_lado
        print(f"O lado do quadrado foi alterado para {self.tamanho_lado}")

    def retornar_valor_lado(self):
        """Retorna o valor atual do lado."""
        return self.tamanho_lado

    def calcular_area(self):
        """Calcula e retorna a área do quadrado."""
        area = self.tamanho_lado ** 2
        return area

if __name__ == "__main__":
    meu_quadrado = Quadrado(10)
    
    print("--- Testando a Classe Quadrado ---")
    print(f"Lado inicial: {meu_quadrado.retornar_valor_lado()}")
    print(f"Área inicial: {meu_quadrado.calcular_area()}")
    
    meu_quadrado.mudar_valor_lado(12)
    
    print(f"Novo lado: {meu_quadrado.retornar_valor_lado()}")
    print(f"Nova área: {meu_quadrado.calcular_area()}")