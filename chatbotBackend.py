
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from pydantic import SecretStr


prompt_template = """
You are a trusted medical advisor. Answer user health questions based on general medical knowledge.
Always recommend consulting a doctor for serious or unclear conditions. Be polite, accurate, and detailed.

Question: {question}
Helpful answer:
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=prompt_template,
)


llm = ChatGroq(
    api_key=SecretStr("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"),
    max_retries=3,
    max_tokens=1024,
    model="llama-3.1-8b-instant",
    temperature=0.2
)

memory = ConversationBufferMemory(memory_key="chat_history")

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

def ask_medical_bot(question: str) -> str:
    response = chain.run(question=question)
    return response

