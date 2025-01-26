# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click", "promoção"]
    
    # Verifica se alguma palavra suspeita está presente no corpo do e-mail
    for palavra in palavras_suspeitas:
        if palavra in mensagem.lower():
            return "Classificação: Phishing"
    
    return "Classificação: Seguro"

# Entrada do conteúdo do e-mail
email_usuario = input()

# Classifica o e-mail
resultado = verificar_phishing(email_usuario)

# Exibe a classificação
print(resultado)
