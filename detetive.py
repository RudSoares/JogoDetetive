import random

# Definição das cartas
suspeitos = ["Sr. Black", "Dona White", "Coronel Mustard", "Sra. Peacock", "Prof. Plum", "Srta. Scarlet"]
armas = ["Revólver", "Faca", "Cano de Chumbo", "Corda", "Chave Inglesa", "Veneno"]
locais = ["Cozinha", "Salão", "Sala de Jantar", "Estúdio", "Biblioteca", "Salão de Jogos"]

# Escolher aleatoriamente o crime verdadeiro
crime = {
    "assassino": random.choice(suspeitos),
    "arma": random.choice(armas),
    "local": random.choice(locais)
}

# Criar as cartas para o jogador (todas menos as do crime)
cartas_disponiveis = [c for c in suspeitos + armas + locais if c not in crime.values()]
random.shuffle(cartas_disponiveis)

def verificar_suspeita(suspeita):
    """Verifica se a suspeita está correta."""
    for chave, valor in crime.items():
        if suspeita[chave] != valor:
            return False, f"{suspeita[chave]} não é o correto para {chave}!"
    return True, "Parabéns! Você solucionou o crime!"

# Jogo
print("Bem-vindo ao jogo Detetive!")
print("Você precisa descobrir quem cometeu o crime, com qual arma e em qual local.")
print(f"Cartas disponíveis para dedução: {', '.join(cartas_disponiveis)}")

while True:
    print("\nFaça sua suspeita!")
    suspeita = {
        "assassino": input(f"Escolha um suspeito ({', '.join(suspeitos)}): "),
        "arma": input(f"Escolha uma arma ({', '.join(armas)}): "),
        "local": input(f"Escolha um local ({', '.join(locais)}): ")
    }
    
    correta, mensagem = verificar_suspeita(suspeita)
    print(mensagem)
    
    if correta:
        break
    else:
        print("Tente novamente!")
