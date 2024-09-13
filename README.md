# Multi-agent-LLM
Overview This repository contains a Python implementation of an AI Research Assistant using the Ollama
Overview
This repository contains a Python implementation of an AI Research Assistant using the Ollama language model. The assistant is designed to provide Ayurvedic solutions to medical inquiries while also having the capability to efficiently search the internet for information across various domains. It utilizes Docker to run the Ollama model locally, making it accessible for users on platforms like Raspberry Pi.
Features

    Ayurvedic Expertise: The assistant can provide Ayurvedic treatments and solutions for medical conditions, specifically tailored for students asking questions.
    Dynamic Internet Search: The AI Research Assistant can search the internet using various tools such as DuckDuckGo, ScrapingBee, or Serper.dev. It formulates search queries based on user requests and drafts relevant queries when context is unclear.
    Docker Integration: The implementation includes instructions for running the Ollama model in a Docker container, ensuring compatibility with various architectures, including ARM for Raspberry Pi.

Getting Started
Prerequisites

    Docker installed on your machine.
    Basic understanding of Python and Docker commands.

Installation Steps

    Clone the Repository:

    bash
    git clone <repository-url>
    cd <repository-directory>

Set Up Docker:
Pull the Ollama Docker image:

bash
docker pull ollama/ollama

Run the Ollama Container:
Start the Ollama container:

bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

Run the AI Assistant:
Execute the Python script to start the AI Research Assistant:

bash
python your_script.py

Example Usage
The assistant can be invoked to address specific queries, such as:

python
task = Task(description="""There is a patient suffering from diabetes, 82 years old.""",
             agent=general_agent,
             expected_output="An Ayurvedic herbs and Yoga Treatment.")

Running on Raspberry Pi
For users running on a Raspberry Pi, the following commands can help set up the environment:

bash
docker run -d --platform linux/arm64 -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

Troubleshooting
If you encounter issues, consider running the Ollama model through Docker as a workaround. Instructions for setting up Docker on Raspberry Pi can be found in various online guides.
Contributions
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.
License
This project is licensed under the MIT License - see the LICENSE file for details. This description provides a comprehensive overview of the repository, outlining its features, installation instructions, and usage, making it easy for potential users and contributors to understand and engage with the project.
