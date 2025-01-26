# classificador_de_phishing
Um script em python que analisa um email e o classifica. Este projeto faz parte do Desafio de Cibersegurança DIO


Descrição
Crie uma solução para analisar uma lista de e-mails recebidos, verificando padrões comuns de phishing nas mensagens. Se um e-mail contiver palavras suspeitas como "ganhe", "prêmio", "urgente", "desconto", "click" e "promoção" ele deve ser classificado como "Phishing" e "Seguro".

Entrada
Uma String contendo um conteúdo único representando o corpo do e-mail.

Saída
"Phishing" ou "Seguro" para cada e-mail.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Ganhe um prêmio incrível hoje!	Classificação: Phishing
Não perca esta promoção exclusiva!	Classificação: Phishing
Você está convidado para a reunião amanhã!	Classificação: Seguro
