class Pessoa:
    def __init__(self, nome, idade, peso, altura_cm):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura_cm  

    def envelhecer(self, anos=1):
        """Aumenta a idade da pessoa e ajusta a altura se for menor de 21."""
        idade_anterior = self.idade
        self.idade += anos
        print(f"{self.nome} envelheceu {anos} ano(s). Idade atual: {self.idade}")
        
        for i in range(anos):
            if (idade_anterior + i) < 21:
                self.crescer(0.5)

    def engordar(self, quilos):
        """Aumenta o peso da pessoa."""
        self.peso += quilos
        print(f"{self.nome} engordou {quilos}kg. Peso atual: {self.peso}kg")

    def emagrecer(self, quilos):
        """Diminui o peso da pessoa."""
        self.peso -= quilos
        print(f"{self.nome} emagreceu {quilos}kg. Peso atual: {self.peso}kg")

    def crescer(self, cm):
        """Aumenta a altura da pessoa em centímetros."""
        self.altura += cm
        print(f"{self.nome} cresceu {cm}cm. Altura atual: {self.altura}cm")

    def mostrar_dados(self):
        """Mostra um resumo dos dados da pessoa."""
        print(f"--- Dados de {self.nome} ---")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} cm")


if __name__ == "__main__":
    print("--- Testando a Classe Pessoa ---")
    joao = Pessoa("João", 18, 70, 175)
    joao.mostrar_dados()
    
    print("\n--- Ações ---")
    joao.envelhecer(2) 
    joao.engordar(5)
    joao.mostrar_dados()
    
    print("\n--- Envelhecendo mais (passando dos 21) ---")
    joao.envelhecer(3) 
    joao.emagrecer(2)
    joao.mostrar_dados()