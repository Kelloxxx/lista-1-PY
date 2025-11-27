class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        """Altera a cor da bola."""
        self.cor = nova_cor
        print(f"A cor da bola agora é {self.cor}")

    def mostraCor(self):
        """Exibe a cor atual da bola."""
        print(f"A cor atual da bola é: {self.cor}")
        return self.cor

if __name__ == "__main__":
    minha_bola = Bola("Azul", 20, "Couro")
    
    print("--- Testando a Classe Bola ---")
    minha_bola.mostraCor()
    
    minha_bola.trocaCor("Vermelha")
    minha_bola.mostraCor()
    
    print(f"Circunferência: {minha_bola.circunferencia}")
    print(f"Material: {minha_bola.material}")