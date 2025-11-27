class TV:
    def __init__(self, canal_inicial=1, volume_inicial=10):
        self.canal = canal_inicial
        self.volume = volume_inicial
        self.canal_min = 1
        self.canal_max = 99
        self.volume_min = 0
        self.volume_max = 100
        self.ligada = True 

    def mudar_canal(self, novo_canal):
        """Altera o canal para um número específico, dentro da faixa válida."""
        if self.canal_min <= novo_canal <= self.canal_max:
            self.canal = novo_canal
            print(f"Canal alterado para: {self.canal}")
        else:
            print(f"Erro: Canal {novo_canal} está fora da faixa válida ({self.canal_min}-{self.canal_max}).")

    def aumentar_volume(self):
        """Aumenta o volume em 1, até o máximo."""
        if self.volume < self.volume_max:
            self.volume += 1
            print(f"Volume: {self.volume}")
        else:
            print("Volume MÁXIMO.")

    def diminuir_volume(self):
        """Diminui o volume em 1, até o mínimo."""
        if self.volume > self.volume_min:
            self.volume -= 1
            print(f"Volume: {self.volume}")
        else:
            print("Volume MÍNIMO.")

    def mostrar_status(self):
        print(f"--- Status da TV ---\nCanal: {self.canal}\nVolume: {self.volume}")

if __name__ == "__main__":
    minha_tv = TV(canal_inicial=5, volume_inicial=20)
    
    print("--- Testando a Classe TV ---")
    minha_tv.mostrar_status()

    print("\n--- Mudando Canal ---")
    minha_tv.mudar_canal(10)
    minha_tv.mudar_canal(150) 
    minha_tv.mudar_canal(1)

    print("\n--- Ajustando Volume ---")
    minha_tv.aumentar_volume()
    minha_tv.aumentar_volume()
    minha_tv.diminuir_volume()
 
    print("\n--- Testando Limites de Volume ---")
    minha_tv.volume = 99
    minha_tv.aumentar_volume()
    minha_tv.aumentar_volume() 
    
    minha_tv.volume = 1 
    minha_tv.diminuir_volume()
    minha_tv.diminuir_volume()
    
    print("\n--- Status Final ---")
    minha_tv.mostrar_status()