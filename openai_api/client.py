from openai import OpenAI, OpenAIError, RateLimitError, AuthenticationError, APIError

# Configuração do cliente OpenAI
client = OpenAI(
    api_key=''
)

# Função para obter a descrição do carro pela API
def get_car_ai_bio(model, brand, year):
    message = f'''
    Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres.
    Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    'role': 'user',
                    'content': message
                }
            ],
            max_tokens=1000,
            model='text-davinci-003',
        )
        return response.choices[0].message.content
    except RateLimitError:
        print("Erro: Créditos insuficientes ou limite de requisições atingido.")
    except AuthenticationError:
        print("Erro: Chave da API inválida.")
    except APIError as e:
        print(f"Erro na API: {str(e)}")
    except OpenAIError as e:
        print(f"Erro inesperado: {str(e)}")
    return None
