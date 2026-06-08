# 🚀 Centro de Controle de Mineração de Asteroides

Este é um sistema em Python projetado para simular o monitoramento, ingestão de dados e análise lógica de asteroides
detectados para fins de mineração espacial. O programa avalia a viabilidade de missões com base na pureza dos minérios e
na distância dos asteroides em Unidades Astronômicas (UA).

## integrantes

Heitor Anacleto Araújo - rm573599

Isaac Israel Rosa Coimbra - rm570072

Matheus Henrique Pedersen Guerra - rm571197

## 📊 Como Funciona o Sistema

O script processa uma lista de asteroides integrando três etapas principais:

1. **Ingestão de Dados:** Uma base de dados simulada contendo informações como identificação do asteroide, tipo de
   minério (Platina, Ferro, Ouro), porcentagem de pureza e distância.
2. **Análise Lógica:** Uma função que aplica regras de negócio espaciais para classificar os asteroides.
3. **Interface de Linha de Comando (CLI):** Um menu interativo para o usuário gerar relatórios ou encerrar o sistema.

### 🧠 Regras de Decisão (Algoritmo)

O sistema classifica cada asteroide em uma das quatro categorias abaixo:

---

| Condição                              | Classificação             | Descrição                                          |
|:--------------------------------------|:--------------------------|:---------------------------------------------------|
| Pureza > 80% **e** Distância < 3.0 UA | **ALVO PRIORITÁRIO**      | Alta pureza e perto, ideal para extração imediata. |
| Pureza > 80% (mas longe)              | **ALVO VALIOSO DISTANTE** | Alta pureza, mas exige mais combustível/tempo.     |
| Distância > 6.0 UA **e** Pureza < 40% | **MINERAÇÃO INVIÁVEL**    | Muito longe e com baixo retorno financeiro.        |
| Outras combinações                    | **MISSÃO PADRÃO**         | Análise normal de rotina.                          |

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Conceitos aplicados:** Estruturas de repetição (`while`, `for`), estruturas condicionais compostas (`if`, `elif`,
  `else`), dicionários e listas, e funções.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

Você precisa ter o **Python 3** instalado em sua máquina.

### Passo a Passo

1. ***Clone o repositório ou baixe o arquivo:**

```bash
git clone https://github.com/htxmetrics/Global-Solution-python.git
```
