#todos os exercícios num só arquivo

#%% [markdown]
# ## Exercício 1

VALOR_TRANSACAO = 100000
TIPO_TRANSACAO = "transferência"
CODIGO_CLIENTE = 10
ANO_2_DIGITOS = 99
var_auxiliar = 1000 * ANO_2_DIGITOS

print("\n\n=== EXERCÍCIO 1 ===\n")

def transacao_bancaria():
  if VALOR_TRANSACAO > var_auxiliar and TIPO_TRANSACAO == "transferência":
    print("Alerta: verificar origem de transferência")
  elif TIPO_TRANSACAO == "saque":
    print("Alerta: confirmar com o cliente")
  else:
    print("Transação normal")

transacao_bancaria()

#%% [markdown]
# ## Exercício 2

print("\n\n=== EXERCÍCIO 2 ===\n")

tempo_empresa_anos = 3
nota_avaliacao = 8.5
carga_horaria = 40

def verificar_promocional():
  if tempo_empresa_anos > 2 and nota_avaliacao >= 8.0:
    print("Elegível para promoção")
  else:
    print("Aguardando próxima avaliação")

verificar_promocional()

#%% [markdown]
# ## Exercício 3

print("\n\n=== EXERCÍCIO 3 ===\n")

distancia_km = 350
clima = "chuva"
zona_entrega = "rural"

def verificar_atraso():
  if distancia_km > 300 and (clima == "chuva" or zona_entrega == "rural"):
    print("Risco alto de atraso")
  else:
    print("Entrega dentro do previsto")

verificar_atraso()

#%% [markdown]
# ## Exercício 4

print("\n\n=== EXERCÍCIO 4 ===\n")


def tratar_sensores(codigo, temperatura):
  if codigo == "F1" and temperatura < 40:
    print("Reiniciar máquina")
  elif codigo == "F2" and temperatura > 60:
    print("Verificar conexão elétrica e sistema de refrigeração")
  elif codigo == "F3" and temperatura in range(45, 55):
    print("Ajustar temperatura da esteira")
  elif codigo == "F4":
    print("Realizar diagnóstico dos sensores ópticos")
  else:
    print("Falha não reconhecida pelo sistema de alarme. Acionar engenheiro responsável")

tratar_sensores('F2', 3)

#%% [markdown]
# ## Exercício 5

print("\n\n=== EXERCÍCIO 5 ===\n")

notas_avaliacao = [5, 8, 10, 6, 9, 4]

def percorrer_lista():
  for nota in notas_avaliacao:
    if nota > 7:
      print(f"{nota}")


percorrer_lista()

#%% [markdown]
# ## Exercício 6

print("\n\n=== EXERCÍCIO 7 ===\n")

lista = []
for comissao in range(0, 50, 5):
  lista.append(5)

print(lista)

#%% [markdown]
# ## Exercício 7

def controlar_conexao():
  tentativas_conexao = [False, False, False, False, True]
  tentativas=0
  limite_tentativas = 3
  while tentativas <= limite_tentativas:
    if tentativas_conexao[tentativas] == True:
      print("Conectado!")
      break
    elif tentativas == limite_tentativas:
      print("Conexão interrompida após limite de tentativas")
      break
    else:
      print("Tentando reconectar...")
      tentativas+=1
      continue

controlar_conexao()

#%% [markdown]
# ## Exercício 8

print("\n\n=== EXERCÍCIO 8 ===\n")

pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P456"
prioridade_urgente = True
pedido_urgente = "P999"

def reorganizar_pedidos():
  if prioridade_urgente == True:
    pedidos.insert(0, pedido_urgente)
    print(f"Fila final (Cenário A): {pedidos}.")
  else:
    for i in pedidos:
      if i == pedido_a_substituir: 
        indice = pedidos.index(i)
        pedidos[indice] = pedido_urgente
        print(f"Fila final (Cenário B): {pedidos}.")
        return
    print(f"Fila final (Cenário C): {pedidos}.")

reorganizar_pedidos()


#%% [markdown]
# ## Exercício 9

print("\n\n=== EXERCÍCIO 9 ===\n")




#%% [markdown]
# ## Exercício 10

print("\n\n=== EXERCÍCIO 10 ===\n")



#%% [markdown]
# ## Exercício 11

print("\n\n=== EXERCÍCIO 11 ===\n")


#%% [markdown]
# ## Exercício 12

print("\n\n=== EXERCÍCIO 12 ===\n")
