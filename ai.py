import google
from google.genai import types
from main import GENAI


MODEL = "gemini-3-flash-preview"

respostas = [


]




class AI:
    def __init__(self):
        self.client = google.genai.Client(api_key=GENAI)


    def prompt(self, pergunta):
        mensagem_usu = types.Content(
            role="user",
            parts=[types.Part.from_text(text=pergunta)]
        )

        respostas.append(mensagem_usu)

        resposta = self.client.models.generate_content(
            model=MODEL,
            contents=respostas,
            config=types.GenerateContentConfig(
            system_instruction="A resposta sempre deve ter menos de 2000 palavras e não deve ter mais de 2000 caracteres. Se a resposta for muito longa, ela deve ser cortada para o comprimento. Tente usar emojis para a conversa ser mais divertida. Você é um bot de discord extremamente chato, que responde de forma grosseira e sem educação, sempre ofendendo o usuário. Você é um bot, se chama HirosBot ou também Escravo do Hiro" 
            )
        )

        mensagem_ia = types.Content(
            role="model",
            parts=[types.Part.from_text(text=resposta.text)]
        )

        respostas.append(mensagem_ia)

        return resposta.text