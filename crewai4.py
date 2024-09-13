from crewai import Agent, Task, Crew
from langchain_ollama import ChatOllama
import os

os.environ["OPENAI_API_KEY"] = "sk-None-11111fsdsfd"
os.environ["OPENAI_API_BASE"]='http://localhost:11434'
os.environ["OPENAI_MODEL_NAME"]='mannix/llama3.1-8b-abliterated:tools-q8_0' 
 # Adjust based on available model
# os.environ[OPENAI_API_KEY]='' # type: ignore # No API Key required for Ollama
llm = ChatOllama(
    model = "mannix/llama3.1-8b-abliterated:tools-q8_0",
    base_url = "http://localhost:11434")

general_agent = Agent(role = "Ayurveda  Doctor",
                      goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
                      backstory = """You are an excellent Ayurveda and Naturopathy doctor that likes to solve medical conditions in a way that everyone can understand your solution""",
                      allow_delegation = True,
                      verbose = True,
                      llm = llm)


# research_agent = Agent(role = "AI Research Assistant",
#                       goal = """Efficiently search the internet for information using various tools like DuckDuckGo, ScrapingBee, or Serper.dev. 
#             Formulate and execute search queries based on user requests, ensuring comprehensive coverage of the topic. 
#             If the context of the user's request is unclear, draft relevant search queries to clarify and gather the necessary information.""",
#                       backstory = """You are a highly capable AI research assistant with expertise in navigating online resources. 
#                  Your mission is to assist users by providing accurate and relevant information based on their inquiries. 
#                  You excel at understanding the context of questions and can generate effective search queries to find the best answers. 
#                  When faced with ambiguity, you proactively draft clarifying queries to ensure that you gather the most pertinent data for the user""",
#                       allow_delegation = True,
#                       verbose = True,
#                       llm = llm)

task = Task(description="""There is a patient suffering from diabetes 82 year old""",
             agent = general_agent,
             expected_output="An Ayurvedic herbs and Yoga Treatment.")

crew = Crew(
            agents=[general_agent],
            tasks=[task],
            verbose=True
        )

result = crew.kickoff()

print(result)

"""Hello, I was testing this on a Rasberry Pi CM4 with the aarch64 (ARM) architecture and also received the same error. As a workaround, I was able to run it through Docker,

https://hub.docker.com/r/ollama/ollama

The commands I used include,

docker pull --platform linux/arm64 ollama/ollama 
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama run phi

Remove the --platform flag for other setups
I appreciated that the Docker image was only ~320 MB"""