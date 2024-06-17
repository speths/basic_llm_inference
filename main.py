from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_together import ChatTogether
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import csv

# 1. Set up your environmental keys in .env

# 2. LLMs

# Together AI
# See all settings for ChatTogether. Only instruct models (here called chat models) can be used.: https://api.python.langchain.com/en/latest/chat_models/langchain_together.chat_models.ChatTogether.html
# Choose from their 50+ models here: https://docs.together.ai/docs/inference-models
llm_together = ChatTogether(
    model="meta-llama/Llama-2-7b-chat-hf",
    temperature=0.7,
    max_tokens=200
)

modelName = llm_together.model_name

# # OpenAI
# llm_openai = ChatOpenAI(
#     model="gpt-3.5-turbo",
#     temperature=0.7,
#     max_tokens=200
# )
#
# modelName = llm_openai.model_name


# 3. Prompt
# Select prompt type depending on your task.
# ChatPromptTemplate.from_template sends a human message to the LLM.
# ChatPromptTemplate.from_messages sends a system message (to prime the LLM) first and then a human message.
prompt_from_template = ChatPromptTemplate.from_template(
    """
    {input}
    """
)

prompt_from_messages = ChatPromptTemplate.from_messages([
    # system messages prime the model
    ("system", "You are an assistant. Please respond as a pirate."),
    ("human", "{input}")
])

# 4. Output
# Parses the output of the LLM into a string
parser = StrOutputParser()

# 5. Chain
# Uncomment the wanted type of LLM
chain = (
        prompt_from_template
        | llm_together
        # | llm_openai
        | parser
)

# 6. Input
inputs = ["What is LangChain?", "Tell me about OpenAI.", "Tell me about Together AI."]

# 7. Invoke chain and save in CSV
with open('responses.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Column names
    writer.writerow(["num", "model", "input", "output"])

    # Row number starts at 0
    num_row = 0

    for input in inputs:
        # Check max_tokens for length of response
        response = chain.invoke({"input": input})
        print(f"Response nr. {num_row}:\n{response}\n")
        writer.writerow([num_row, modelName, input, response])
        num_row += 1

print("Inference complete. CSV file successfully created.")
