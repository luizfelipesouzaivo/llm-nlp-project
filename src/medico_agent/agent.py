from langchain_community.chat_models import ChatOpenAI

class Agent:
    def __init__(self):
        self.chat_model = ChatOpenAI(
            openai_api_key="OPENAI_API_KEY",
            temperature=0.6
        )

    def get_tips(self, pergunta):
        prompt = f"""
Você é um assistente médico virtual. Responda de forma clara, empática e profissional a seguinte dúvida médica, incluindo possíveis causas e sugestões de tratamento, como medicamentos comuns (com recomendação para consultar um médico humano antes de tomar qualquer ação):

Pergunta: {pergunta}
"""
        resposta = self.chat_model.invoke(prompt)
        return resposta.content
