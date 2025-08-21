from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="moonshotai/Kimi-K2-Instruct",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm, temperature=0)

template1 = PromptTemplate(
    template="Give me brief summary about {topic}?",
    input_variables=["topic"],
)

template2 = PromptTemplate(
    template="Generate 5 points on the given text {text}",
    input_variables=["text"],
)

output_parser = StrOutputParser()

# prompt1 = template1.invoke({"topic": "Black Hole"})
# result = model.invoke(prompt1)
# result = output_parser.invoke(result)
# prompt2 = template2.invoke({"text": result})
# result = model.invoke(prompt2)
# result = output_parser.invoke(result)

chain = template1 | model | output_parser | template2 | model | output_parser

result = chain.invoke({"topic": "Black Hole"})

print(result)


