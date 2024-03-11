from openai import OpenAI

client = OpenAI(
    api_key=''
)

def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descricao de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas especificas deste modelo 
    Descreva especificacoes tecnicas deste modelo.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'roles': 'user',
                'content':message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )
    return response.choises[0].message.content
