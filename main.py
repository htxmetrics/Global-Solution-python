# ========== INGESTÃO DE DADOS ==========

asteroides_detectados = [
    {"asteroide": "AST-001", "minerio": "Platina", "pureza": 85, "distancia": 1.2},
    {"asteroide": "AST-002", "minerio": "Ferro", "pureza": 40, "distancia": 0.5},
    {"asteroide": "AST-003", "minerio": "Ouro", "pureza": 15, "distancia": 5.0},
    {"asteroide": "AST-004", "minerio": "Platina", "pureza": 92, "distancia": 8.5}
]

# ========== ANÁLISE LÓGICA ==========

def analisar_asteroide():
    print("\n--- RELATÓRIO DE ANÁLISE DE ASTEROIDES ---\n")

    for item in asteroides_detectados:
        asteroide = item["asteroide"]
        minerio = item["minerio"]
        pureza = item["pureza"]
        distancia = item["distancia"]

        if pureza > 80 and distancia < 3.0:
            decisao = "ALVO PRIORITÁRIO (Alta pureza e perto)"

        elif distancia > 6.0 and pureza < 40:
            decisao = "MINERAÇÃO INVIÁVEL (Muito longe e pouca pureza)"

        elif pureza > 80:
            decisao = "ALVO VALIOSO DISTANTE (Alta pureza, mas longe)"

        else:
            decisao = "MISSÃO PADRÃO (Análise normal)"

# ========== EXIBIÇÃO DE RESULTADOS ==========

        print(
            f"Asteroide: {asteroide} | Minério: {minerio} | Pureza: {pureza}% | Distância: {distancia} UA | Decisão: {decisao}")

  # ========== PROGRAMA PRINCIPAL ==========

while True:
    print("\n" + "=" * 40)
    print("CENTRO DE CONTROLE DE MINERAÇÃO")
    print("=" * 40)
    print("[1] Gerar Relatório de Asteroides")
    print("[2] Sair do Sistema")

    opcao = input("Escolha uma opção (1 ou 2): ")

    if opcao == "1":
        analisar_asteroide()

    elif opcao == "2":
        print("\nDesconectando do Centro de Controle... Até logo, Capitão!")
        break

    else:
        print("\n[ERRO] Opção inválida! Digite apenas 1 ou 2.\n")