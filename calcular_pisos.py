
from retangulo import Retangulo

def main():
    print("--- Calculadora de Pisos e Rodapés ---")
    
    try:

        base_local = float(input("Informe a largura (base) do local (em metros): "))
        altura_local = float(input("Informe o comprimento (altura) do local (em metros): "))

        if base_local <= 0 or altura_local <= 0:
            print("As medidas devem ser valores positivos.")
            return

        local = Retangulo(base_local, altura_local)

        area_total = local.calcular_area()
        perimetro_total = local.calcular_perimetro()

        print("\n--- Resultado ---")
        print(f"Medidas do local: {local.base}m x {local.altura}m")
        

        print(f"Quantidade de piso necessária: {area_total:.2f} m²")
        
        print(f"Quantidade de rodapé necessária: {perimetro_total:.2f} metros lineares")

    except ValueError:
        print("Erro: Por favor, insira apenas números válidos para as medidas.")


if __name__ == "__main__":
    main()
    