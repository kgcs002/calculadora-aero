import math
import matplotlib.pyplot as plt

# Função para calcular a força de sustentação
def calcular_forca_sustentacao(ρ, V, S, Cl):
    return 0.5 * ρ * V**2 * S * Cl

# Função para calcular a força de arrasto
def calcular_forca_arrasto(ρ, V, S, Cd):
    return 0.5 * ρ * V**2 * S * Cd

# Função para simular a trajetória de voo
def simular_trajetoria(V_inicial, angulo_subida, tempo_voo):
    g = 9.81  # Aceleração da gravidade (m/s²)
    angulo_rad = math.radians(angulo_subida)
    V_vertical = V_inicial * math.sin(angulo_rad)
    
    t = []
    h = []
    
    for t_curr in range(tempo_voo + 1):
        altura = V_vertical * t_curr - 0.5 * g * t_curr**2
        h.append(max(0, altura))
        t.append(t_curr)
    
    # Plotar gráfico da trajetória
    plt.plot(t, h)
    plt.xlabel('Tempo (s)')
    plt.ylabel('Altura (m)')
    plt.title('Trajetória de Voo')
    plt.grid(True)
    plt.show()

    return max(h)  # Altura máxima

# Função para calcular o momento de arfagem (pitch)
def calcular_momento_arfagem(Cm, ρ, V, S, corda_media):
    return Cm * 0.5 * ρ * V**2 * S * corda_media

# Função principal para escolher a análise
def menu_principal():
    print("Escolha a análise que deseja realizar:")
    print("1. Cálculo de Performance de Voo")
    print("2. Análise Aerodinâmica")
    print("3. Simulação de Trajetória")
    print("4. Análise de Estabilidade e Controle")
    opcao = input("Digite o número da opção: ")

    if opcao == '1':
        calcular_performance()
    elif opcao == '2':
        calcular_aerodinamica()
    elif opcao == '3':
        simular_voo()
    elif opcao == '4':
        analisar_estabilidade()
    else:
        print("Opção inválida.")

# Função para calcular a performance de voo
def calcular_performance():
    V_inicial = float(input("Digite a velocidade inicial (m/s): "))
    tempo_voo = int(input("Digite o tempo de voo (s): "))
    angulo_subida = float(input("Digite o ângulo de subida (graus): "))
    altura_maxima = simular_trajetoria(V_inicial, angulo_subida, tempo_voo)
    print(f"Altura máxima alcançada: {altura_maxima:.2f} metros")

# Função para calcular a análise aerodinâmica
def calcular_aerodinamica():
    densidade_ar = float(input("Digite a densidade do ar (kg/m³): "))
    velocidade_voo = float(input("Digite a velocidade de voo (m/s): "))
    area_asa = float(input("Digite a área da asa (m²): "))
    coeficiente_sustentacao = float(input("Digite o coeficiente de sustentação (Cl): "))
    coeficiente_arrasto = float(input("Digite o coeficiente de arrasto (Cd): "))
    
    forca_sustentacao = calcular_forca_sustentacao(densidade_ar, velocidade_voo, area_asa, coeficiente_sustentacao)
    forca_arrasto = calcular_forca_arrasto(densidade_ar, velocidade_voo, area_asa, coeficiente_arrasto)
    
    print(f"Força de Sustentação (L): {forca_sustentacao:.2f} N")
    print(f"Força de Arrasto (D): {forca_arrasto:.2f} N")

    # Gráfico das forças em função da velocidade
    velocidades = [v for v in range(0, int(velocidade_voo*1.5), 10)]
    sustentacoes = [calcular_forca_sustentacao(densidade_ar, v, area_asa, coeficiente_sustentacao) for v in velocidades]
    arrastos = [calcular_forca_arrasto(densidade_ar, v, area_asa, coeficiente_arrasto) for v in velocidades]
    
    plt.plot(velocidades, sustentacoes, label="Sustentação (L)")
    plt.plot(velocidades, arrastos, label="Arrasto (D)")
    plt.xlabel('Velocidade (m/s)')
    plt.ylabel('Força (N)')
    plt.title('Forças Aerodinâmicas')
    plt.legend()
    plt.grid(True)
    plt.show()

# Função para simular a trajetória de voo
def simular_voo():
    V_inicial = float(input("Digite a velocidade inicial (m/s): "))
    angulo_subida = float(input("Digite o ângulo de subida (graus): "))
    tempo_voo = int(input("Digite o tempo de voo (s): "))
    altura_maxima = simular_trajetoria(V_inicial, angulo_subida, tempo_voo)
    print(f"Altura máxima alcançada: {altura_maxima:.2f} metros")

# Função para análise de estabilidade e controle
def analisar_estabilidade():
    densidade_ar = float(input("Digite a densidade do ar (kg/m³): "))
    velocidade_voo = float(input("Digite a velocidade de voo (m/s): "))
    area_asa = float(input("Digite a área da asa (m²): "))
    coeficiente_momento = float(input("Digite o coeficiente de momento (Cm): "))
    corda_media = float(input("Digite a corda média da asa (m): "))
    
    momento_arfagem = calcular_momento_arfagem(coeficiente_momento, densidade_ar, velocidade_voo, area_asa, corda_media)
    print(f"Momento de Arfagem: {momento_arfagem:.2f} Nm")
    
    # Gráfico do momento de arfagem em função da velocidade
    velocidades = [v for v in range(0, int(velocidade_voo*1.5), 10)]
    momentos = [calcular_momento_arfagem(coeficiente_momento, densidade_ar, v, area_asa, corda_media) for v in velocidades]
    
    plt.plot(velocidades, momentos)
    plt.xlabel('Velocidade (m/s)')
    plt.ylabel('Momento de Arfagem (Nm)')
    plt.title('Momento de Arfagem')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    menu_principal()
