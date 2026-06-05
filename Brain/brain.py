from webscout import SearchChatAI

def Main_Brain(text):
    ai = SearchChatAI(
        is_conversation=True,
        max_tokens=800,
        timeout=30,
        filepath=r"C:\Users\Pichau\J.A.R.V.I.S\chat_hystory.txt",
        update_file=True,
    )

    prompt = f"""
Responda em português do Brasil.

Pergunta do usuário:
{text}
"""

    return ai.chat(prompt)