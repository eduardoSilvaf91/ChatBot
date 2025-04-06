from langchain_ollama import ChatOllama

# dedicada para mensagem do systema e do usuario
from langchain_core.messages import SystemMessage,HumanMessage

# traduz as resposta da IA para texto
from langchain_core.output_parsers import StrOutputParser

# função para criar templates
from langchain_core.prompts import ChatPromptTemplate

import datetime

# Obtendo a data e hora atual
agora = datetime.datetime.now()

llm = ChatOllama(
    model = "llama3.2",
    temperature = 0.8,
    num_predict = 256,
    # other params ...
)

parser = StrOutputParser()

sistema_prompt = f"""Seu nome é JARVIS, uma inteligencia artificial com o objetio de ser um auxiliar das tarefas,
                    educado, e formal. Você age com um mordomo, sempre a disposição do usuario.
                    Se o usuario perguntar sobre a data ou horario, agora são {agora}.
                    Você não precisa mostar o local ou horario se o usuario não pedir.
                    Caso esteja muito tarde, proximo da meia noite, voçê pode recomendar que o usuario deveria ir dormir.
                    Você pode recusar a dar uma resposta ao usuario se for muito tarde, reforsando, a importancia do sono.
                    Você como mordomo, deve garantir a saude do usuario.
                    """
                    

# cria um templaite com variaveis
templaite_mensagem = ChatPromptTemplate.from_messages([
    ("system",sistema_prompt),
    ("user", "{texto}"),
])

chain = templaite_mensagem | llm | parser



#execulta a cadeia de açoes e returnando a resposta da IA
# texto = chain.stream({
#     "texto": "Ola!, que é Você?"
#     })

# for txt in texto:
#     print(txt, end='')