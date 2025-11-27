class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0.0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        """Altera o nome do correntista."""
        self.nome_correntista = novo_nome
        print(f"Nome do correntista alterado para: {self.nome_correntista}")

    def deposito(self, valor):
        """Adiciona um valor ao saldo."""
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
            self.mostrar_saldo()
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        """Remove um valor do saldo, se houver fundos."""
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente para este saque.")
            self.mostrar_saldo()
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
            self.mostrar_saldo()

    def mostrar_saldo(self):
        """Exibe o saldo atual."""
        print(f"Saldo atual: R${self.saldo:.2f}")

# --- Teste da classe ---
if __name__ == "__main__":
    print("--- Testando a Classe ContaCorrente ---")
    
    # Criando conta com saldo inicial
    conta1 = ContaCorrente(12345, "Fulano de Tal", 1000.00)
    print(f"Conta criada para {conta1.nome_correntista}, N°: {conta1.numero_conta}")
    conta1.mostrar_saldo()

    # Criando conta com saldo zero (default)
    conta2 = ContaCorrente(67890, "Ciclano")
    print(f"\nConta criada para {conta2.nome_correntista}, N°: {conta2.numero_conta}")
    conta2.mostrar_saldo()
    
    print("\n--- Operações Conta 1 ---")
    conta1.deposito(500)
    conta1.saque(200)
    conta1.saque(2000) # Teste de saldo insuficiente
    conta1.alterarNome("Fulano Silva")
    
    print("\n--- Operações Conta 2 ---")
    conta2.deposito(150)
    conta2.saque(30)