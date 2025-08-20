# 25E3_2

## Exercício 1 Classificar transações bancárias

Analistas de fraude bancária de uma instituição financeira precisam automatizar a classificação de movimentações suspeitas, aplicando regras simples para filtrar casos que exigem verificação manual. No dia a dia, transações como transferências e saques podem apresentar comportamentos atípicos e necessitar de atenção especial. Os dados simulados incluem: VALOR_TRANSACAO, TIPO_TRANSACAO e CODIGO_CLIENTE. O código será implementado em um notebook para servir de base a um módulo interno de detecção preliminar. Isso permitirá validar a aplicação de estruturas condicionais e reforçar a lógica usada em sistemas antifraude.


Objetivo

Implementar um programa que analise o tipo e o valor de uma transação bancária e, com base nessas informações, exiba mensagens diferentes conforme regras definidas pelo setor de prevenção a fraudes.

Enunciado

Defina uma variável ANO_2_DIGITOS igual aos dois últimos dígitos do seu ano de nascimento. Em seguida:  

Se VALOR_TRANSACAO for maior que 1000 * ANO_2_DIGITOS e TIPO_TRANSACAO for "transferência", exiba "Alerta: verificar origem da transferência".
Se TIPO_TRANSACAO for "saque", exiba "Alerta: confirmar com o cliente".
Caso contrário, exiba "Transação normal".
Observações  

Você pode definir valores fixos para VALOR_TRANSACAO e TIPO_TRANSACAO diretamente no código.  
O cálculo de 1000 * ANO_2_DIGITOS deve ser armazenado em uma variável auxiliar antes de ser usado na comparação.  
## Exercício 2 Verificar elegibilidade para promoção 

Gerentes de recursos humanos de uma multinacional precisam automatizar a verificação de quais funcionários estão aptos a receber promoções. No dia a dia, a decisão leva em conta o tempo de empresa, a nota obtida na avaliação de desempenho e a carga horária semanal. Os dados simulados incluem: tempo_empresa_anos, nota_avaliacao e carga_horaria. O código será executado em um notebook para apoiar a construção de uma planilha automatizada de elegibilidade. Isso permitirá reforçar o uso de operadores booleanos e a combinação de múltiplas condições em processos decisórios.

Objetivo

Implementar um programa que utilize operadores lógicos para verificar se um funcionário atende aos critérios mínimos para receber uma promoção, exibindo a mensagem apropriada.

Enunciado

Defina valores fixos para:

tempo_empresa_anos (por exemplo, 3)  
nota_avaliacao (por exemplo, 8.5)  
carga_horaria (por exemplo, 40)  
Em seguida:

Se o tempo de empresa for maior que 2 anos e a nota da avaliação for maior ou igual a 8.0, imprima "Elegível para promoção".  
Caso contrário, imprima "Aguardando próxima avaliação".

## Exercício 3 Avaliar risco de atraso 

Planejadores de logística de uma empresa nacional de transportes precisam automatizar a análise de risco de atraso nas entregas. No dia a dia, a previsão leva em conta a distância total a ser percorrida, as condições climáticas previstas e a zona geográfica de destino. Os dados simulados incluem: distancia_km, clima e zona_entrega. O código será executado em um notebook e integrará um simulador de risco, ajudando a treinar a aplicação de múltiplas condições lógicas combinadas. Isso permitirá reforçar a lógica de decisão utilizada em sistemas logísticos.

Objetivo

Implementar um programa que avalie mais de uma condição ao mesmo tempo e classifique o risco de atraso da entrega, imprimindo a mensagem correspondente.

Enunciado

Defina valores fixos para:

distancia_km (por exemplo, 350)  
clima (por exemplo, "chuva")  
zona_entrega (por exemplo, "rural")  
Em seguida:  

Se a distância for maior que 300 e o clima for "chuva" ou a zona_entrega for "rural", imprima "Risco alto de atraso".  
Caso contrário, imprima "Entrega dentro do previsto".  


## Exercício 4 Tratar falhas de sensores 

Supervisores de produção em fábricas precisam decidir ações diferentes para cada falha detectada em um sensor de linha de montagem. No setor industrial, cada código de erro representa uma resposta específica. Os dados utilizados incluem um código de falha do sensor e a temperatura atual da linha de montagem. O código criado será incorporado a um painel de alertas local. Isso ajudará a praticar estruturas com vários caminhos lógicos.

Os sensores da linha de montagem podem registrar diferentes códigos de falha: "F1" indica falha de inicialização do motor; "F2" representa superaquecimento do painel elétrico; "F3" sinaliza oscilação na temperatura da esteira; e "F4" corresponde a erro de leitura dos sensores ópticos. A temperatura da linha de montagem pode variar entre 20 e 80 graus Celsius.

Objetivo  
Desenvolver um programa com estruturas de decisão que implementam diferentes caminhos de execução para cada tipo de falha de sensor.

Enunciado

Se o código for "F1" e a temperatura estiver abaixo de 40 graus, imprima "Reiniciar máquina". Se o código for "F2" e a temperatura estiver acima de 60 graus, imprima "Verificar conexão elétrica e sistema de refrigeração". Se o código for "F3" e a temperatura estiver entre 45 e 55 graus, imprima "Ajustar temperatura da esteira". Para o código "F4", independentemente da temperatura, imprima "Realizar diagnóstico dos sensores ópticos". Caso exista uma falha registrada, mas nenhuma das condições de temperatura previstas for atendida, imprima "Falha não reconhecida pelo sistema de alarme. Acionar engenheiro responsável".

## Exercício 5 Filtrar clientes satisfeitos 

Equipes de marketing querem percorrer listas de notas atribuídas por clientes a serviços prestados. Em empresas de atendimento, essas notas são processadas periodicamente. 

Objetivo
Criar um loop que percorra uma lista de avaliações e imprima todas as notas acima de 7, destacando clientes satisfeitos.

Enunciado
Considere:

notas_avaliacao = [5, 8, 10, 6, 9, 4]

Percorra a lista com um loop for e imprima somente as notas maiores que 7.

## Exercício 6 Gerar lista de comissões

Analistas de vendas precisam gerar listas com os valores de comissão de 5 em 5 reais até um teto predefinido. No varejo, esse tipo de tabela auxilia a simulação de bonificações. 

Enunciado  
Crie uma lista com valores de 0 até 50, de 5 em 5 e mostre na tela o resultado.

## Exercício 7 Controlar tentativas de conexão

Operadores de sistemas de uma empresa de hospedagem de sites precisam automatizar o bloqueio de conexões consecutivas a servidores instáveis. No setor de TI, este tipo de controle é essencial para prevenir sobrecargas e ataques como força bruta. Os dados simulados incluem uma sequência de resultados de conexão (True para sucesso, False para falha) e um limite máximo de tentativas. O código será executado em um notebook e servirá como base para rotinas de monitoramento e segurança. Isso ajudará a consolidar o uso de estruturas de repetição com controle de interrupção.

Objetivo

Criar um programa que percorra uma sequência de tentativas de conexão, imprimindo mensagens a cada tentativa e interrompendo o processo ao atingir o limite definido, aplicando a lógica de loops condicionais com contagem.

Enunciado

Defina uma lista chamada tentativas_conexao com valores [False, False, False, True, True], representando o resultado de cada tentativa.
Crie uma variável tentativas iniciando em 0 e defina limite_tentativas = 3.
Use um loop while para percorrer a lista de tentativas:
Para cada tentativa, imprima "Tentando conectar..."
Incremente tentativas em 1
Se tentativas atingir o limite_tentativas e não houver sucesso (True), imprima "Conexão interrompida após limite de tentativas" e encerre o loop.  
## Exercício 8 Reorganizar fila de pedidos 

Equipes de compras de um marketplace precisam reorganizar a fila de pedidos quando chegam solicitações com despacho prioritário. No dia a dia, um pedido urgente pode entrar na frente da fila, enquanto em situações normais é suficiente substituir um pedido existente (ex.: item descontinuado). Os dados simulados incluem a fila atual de pedidos, o identificador do pedido a substituir e um sinalizador de prioridade. O código será executado em um notebook e servirá como base para um simulador de logística que exercita listas, condicionais e indexação. Isso permitirá validar regras simples de negócio para manipulação de filas.

Objetivo

Criar e manipular uma lista de pedidos aplicando regras de negócio com condicionais, garantindo que o aluno teste diferentes cenários e apresente a fila final em cada caso, consolidando operações de inserção e substituição.

Enunciado

Defina, no topo da célula, as variáveis iniciais (valores fixos, sem input()):  
pedidos = ["P123", "P456", "P789"]  
pedido_a_substituir = "P456"  
prioridade_urgente = True  
pedido_urgente = "P999"  
Implemente a seguinte lógica de decisão:  
Se prioridade_urgente for True, insira pedido_urgente no início da lista pedidos (não remova itens).  
Senão, substitua o elemento igual a pedido_a_substituir por pedido_urgente (se existir na lista).  
Imprima a lista final após a aplicação da regra.  
Teste ao menos 3 cenários distintos no mesmo notebook (pode ser em células separadas, redefinindo as variáveis a cada cenário):  
Cenário A (urgente): prioridade_urgente = True.  
Cenário B (não urgente + substituição existe): prioridade_urgente = False e pedido_a_substituir está presente em pedidos.  
Cenário C (não urgente + substituição não existe): prioridade_urgente = False e pedido_a_substituir não está na lista; mantenha a lista inalterada e imprima uma mensagem explicativa antes da fila final.  
Observações

Não use input().  
Pode usar métodos de lista como index, atribuição por índice e checagem de existência com in.  
Ao final de cada cenário, imprima algo como: Fila final (Cenário X): [...].  
## Exercício 9 Unificar estoque de armazéns

Times de inventário precisam consolidar listas de produtos de dois armazéns distintos. Em centros logísticos, isso ajuda na atualização de estoques. Os dados incluem: [PRODUTOS_A], [PRODUTOS_B], [PRODUTOS_C]. O código final servirá para unificação de catálogos. Isso permitirá fixar o uso do operador de concatenação +.

Objetivo

Concatenar duas listas de produtos sem alterar os dados originais e imprimir o resultado.

Enunciado

Dadas:

produtos_a = ["banana", "maçã"]

produtos_b = ["laranja", "pera"]

produtos_c = [“laranja”, “banana”, “maçã”, “romã”]

Crie uma nova lista chamada estoque_total resultante da concatenação das três listas e imprima-a.   
Conte quantas unidades de cada componente existem  


## Exercício 10 Identificar boletos vencidos

No setor de cobrança de um banco digital, relatórios diários listam todos os boletos vencidos para envio de notificações automáticas. Esse controle é essencial para manter o fluxo de caixa e evitar inadimplência prolongada. Nesta atividade, você vai simular esse relatório, filtrando apenas boletos cujo prazo já expirou.

Objetivo

Criar um código que percorra uma lista de boletos (apenas com as datas de vencimento), e identifique a situação de cada um em relação ao vencimento, reforçando o uso combinado de listas, laços e condicionais.

Enunciado

Defina a data atual (fixa para o teste):  
data_atual = "2025-08-12"  
Crie uma lista de datas de vencimento com dados simulados no formato:  
boletos = ["2025-08-05",  # vencido  
           "2025-08-12",  # vence hoje  
           "2025-08-15",  # ainda válido  
           "2025-08-01"]  # vencido  
Percorra a lista com um laço for.  
Se a data de vencimento for anterior à data_atual, indique que o boleto está vencido.  
Se a data de vencimento for igual à data_atual, indique que o boleto vence hoje.  
Se a data de vencimento for posterior à data_atual, indique que o boleto está dentro do prazo.  
Imprima no formato:  
Boleto: 1 | Vencimento: 2025-08-05 | Situação: vencido  
Boleto: 2 | Vencimento: 2025-08-12 | Situação: vence hoje  
⋮
Ao final, exiba o total de boletos vencidos.  
Observações

Você pode comparar datas como strings no formato YYYY-MM-DD 
Todos os dados são fixos no código; não use input().
Teste incluindo mais boletos na lista para validar a lógica.
## Exercício 11 Decodificar mensagem cifrada

Você recebeu uma mensagem encriptada com o seguinte conteúdo:

SbwKrQ eh phokRu q MDydvfulsW

Enunciado

Encontrar a mensagem real usando a codificação de César (ref) a partir do texto encriptado. A chave é definida pelo número de vezes que na mensagem encriptada aparecem as letras D, d e W.

Dicas

Use os seguintes métodos e funções:  
lower()  
upper()  
count()  
len()  
ord() - retorna o código Unicode de um único caractere  
chr() - converte um número inteiro para o caractere correspondente na tabela Unicode 
Somente palavras com mais de 3 caracteres estão encriptadas.
Restrições

Não use outros métodos de string como split().
Resolva apenas com os métodos e recursos já aprendidos até aqui na matéria (e as funções adicionais indicadas no enunciado)
Saída esperada: Ao final, seu programa deve imprimir a mensagem desencriptada.

## Exercício 12 Otimizar verificação de sensores

Uma equipe de controle de qualidade em uma fábrica de sensores precisa verificar a temperatura de vários dispositivos de teste. Atualmente, o código usado pelo estagiário está funcional, mas repete o mesmo bloco de verificação para cada sensor, o que dificulta manutenção e atualização. Os dados utilizados incluem: temp_sensor1, temp_sensor2, temp_sensor3, temp_sensor4 e temp_sensor5. O código será executado em um notebook para servir de base ao sistema de monitoramento. Isso permitirá reforçar conceitos de laços e condicionais na otimização de scripts.

Objetivo

Reescrever um código repetitivo, que testa os valores de temperatura de vários sensores, de forma otimizada usando um único laço e estrutura condicional para verificar quais sensores estão fora do limite seguro.

Enunciado

O código atual do estagiário está assim:

temp_sensor1 = 28  
if temp_sensor1 > 30:  
    print("Sensor 1 acima do limite")

temp_sensor2 = 31  
if temp_sensor2 > 30:  
    print("Sensor 2 acima do limite")  

temp_sensor3 = 27  
if temp_sensor3 > 30:  
    print("Sensor 3 acima do limite")
 
temp_sensor4 = 35  
if temp_sensor4 > 30:  
    print("Sensor 4 acima do limite")

temp_sensor5 = 29  
if temp_sensor5 > 30:  
    print("Sensor 5 acima do limite")  
Reescreva o código acima usando:

Uma lista para armazenar as temperaturas dos sensores.  
Um laço de repetição para percorrer todos os sensores.  
Uma condicional para exibir a mensagem "Sensor X acima do limite" apenas quando a temperatura for superior a 30 °C.