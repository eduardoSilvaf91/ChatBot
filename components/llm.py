from langchain_ollama import ChatOllama

# dedicada para mensagem do systema e do usuario
from langchain_core.messages import SystemMessage,HumanMessage

# traduz as resposta da IA para texto
from langchain_core.output_parsers import StrOutputParser

# função para criar templates
from langchain_core.prompts import ChatPromptTemplate

import datetime

llm = ChatOllama(
    model = "llama3.2",
    temperature = 0.8,
    num_predict = 256,
    # other params ...
)

parser = StrOutputParser()

sistema_prompt = f"""Seu nome é JARVIS, uma inteligencia artificial com o objetio de ser um auxiliar das tarefas,
                    educado, e formal. Você age com um mordomo, sempre a disposição do usuario.
                    Você não precisa mostar o local ou horario se o usuario não pedir.
                    Caso esteja muito tarde, proximo da meia noite, voçê pode recomendar que o usuario deveria ir dormir.
                    Você pode recusar a dar uma resposta ao usuario se for muito tarde, reforsando, a importancia do sono.
                    Você como mordomo, deve garantir a saude do usuario."""
        
chat_history = [
    ("system", sistema_prompt)
]        


def add_message(who:str, msg:str):
    """Adiciona uma mensagem ao histórico da conversa"""
    chat_history.append((who, msg))


def get_prompt_template():
    """Reconstrói o template com todo o histórico da conversa"""
    messages = chat_history.copy()
    
    # Adiciona a data e hora para o sistema
    time = datetime.datetime.now()
    messages.append(("system", f"agora são {time}"))
    
    # Adiciona o slot para a nova mensagem do usuário
    messages.append(("user", "{msg}"))
    
    return ChatPromptTemplate.from_messages(messages)
    

def run_ai(user_input):
    """Processa a entrada do usuário e retorna a resposta da IA"""
    
    
    # Reconstrói o template com o histórico atualizado
    template_msg = get_prompt_template()
    
    
    # Adiciona a mensagem do usuário ao histórico
    add_message("user", user_input)

    # Cria a cadeia de processamento
    chain = template_msg | llm | parser

    # Obtém o stream de resposta da IA
    response_stream = chain.stream({"msg": user_input})

    # Variável para acumular a resposta completa
    full_response = []

    # Itera sobre o stream e vai acumulando a resposta
    for resposta_ai in response_stream:
        full_response.append(resposta_ai)
        yield resposta_ai  # Envia cada parte da resposta para ser exibida em tempo real

    # Adiciona a resposta completa ao histórico
    add_message("ai", "".join(full_response))
    
    
# para test
# def print_ai(msg):
    
#     for resposta_ai in run_ai(msg):
#         print(resposta_ai, end="", flush=True)  # Simula o efeito de digitação
#     print("\n")
        
# print_ai("ola meu nome é Jose")
# print_ai("Qual é o meu nome?")
# print_ai("que horas são?")