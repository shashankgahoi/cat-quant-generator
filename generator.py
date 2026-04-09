import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_question(topic="Arithmetic", difficulty="Medium"):
    prompt = f"""
    Generate a CAT Quantitative Aptitude question.

    Topic: {topic}
    Difficulty: {difficulty}

    Format:
    Question:
    A)
    B)
    C)
    D)

    Answer:
    Explanation:
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
