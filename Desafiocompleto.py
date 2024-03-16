
#eSTRUTURA DE CONTROLE COM USO DE VARIAVEIS
while True:
    # Solicitar nome e experiência do herói
    NameHero = input("Qual é o seu nome?")
    exp = int(input("Qual é o seu nivel de experiência?"))
    

    #ESTRUTURAS DE CONDIÇÃO.
    if exp < 1000:
        nivel = "Ferro"
        print("Seu nome é ", NameHero, "E SEU NIVEL É:", nivel)
    elif 1001 <= exp <= 2000:
        nivel = "Bronze"
        print("Seu nome é ", NameHero, "E SEU NIVEL É:", nivel)
    elif 2001 <= exp <= 5000:
        nivel = "Prata"
        print("Seu nome é ", NameHero, "E SEU NIVEL É:", nivel)
    elif 5001 <= exp <= 7000:
        nivel = "Ouro"
        print("Seu nome é ", NameHero, "E SEU NIVEL É:", nivel)
    elif 7001 <= exp <= 8000:
        nivel = "Platina"
        print("Seu nome é ", NameHero, "E SEU NIVEL É:", nivel)
    elif 8001 <= exp <= 9000:
        nivel = "Ascendente"
        print("Seu nome é ", NameHero, "E SEU NIVEL É:", nivel)
    elif 9001 <= exp <= 10000:
        nivel = "Imortal"
        print("Seu nome é ", NameHero, "E SEU NIVEL É:", nivel)
    else:
        nivel = "Radiante"
        print("Seu nome é ", NameHero, "E SEU NIVEL É:", nivel)
        #sAIDA DO PROGRAMA.
        sair = input("Deseja sair do programa? (s/n)").lower()
    if sair == "s":
        print("Saindo do programa.")
        break




