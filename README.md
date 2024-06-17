This basic template offers the possibility to run LLMs from Together AI and OpenAI with LangChain.

------------------------------------------------------------------------------------------------------------------------

### Installation guide

#### 1. Create a new project and conda environment in PyCharm

#### 2. Clone the repo

    git clone https://github.com/speths/basic_llm_inference.git

#### 3. Install the following packages in the terminal with `pip`
- `pip install python-dotenv`
- `pip install langchain-openai`
- `pip install langchain-together`
- `pip install langchain-core`

------------------------------------------------------------------------------------------------------------------------

### Further information

#### Tutorials

If you would like to deeper understand the code, look into the following links:

1. Watch the first three videos of this playlist
   - https://www.youtube.com/watch?v=ekpnVh-l3YA&list=PL4HikwTaYE0GEs7lvlYJQcvKhq0QZGRVn
2. Do this tutorial of the LangChain series
   - https://python.langchain.com/v0.2/docs/tutorials/llm_chain/

#### Models 

Here you can find all the models that you can run. Just change the name in code accordingly. At the moment only instruct models (chat models) are supported.
1. Together AI
   - https://docs.together.ai/docs/inference-models
   - e.g. `mistralai/Mistral-7B-Instruct-v0.3`
3. OpenAI
   - https://platform.openai.com/docs/models
   - e.g. `gpt-4-turbo`
     
