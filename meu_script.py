def minha_funcao():
    try:
        print("Executando função")
        # Código principal
        # Exemplo de código principal
        resultado = 10 / 2  # Este é um exemplo simples
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Erro: {str(e)}")
        raise

# Chamando a função para teste
minha_funcao()
