# AgentsDebate
Autogen based Agents debate

This repository contains a Python script for a debate system involving multiple agents and a moderator. The agents engage in discussions on a given topic, exploring different perspectives, while the moderator provides analytical reflections and a comprehensive synthesis at the end.

## Features

- **Agents**: Two agents (Agent 1 and Agent 2) with distinct roles:
  - Agent 1: Intellectual discussion participant who explores positive aspects and potential benefits of the topic.
  - Agent 2: Analytical discussion participant who examines limitations and challenges of the topic.
- **Moderator**: A philosophical observer and critical thinker who analyzes discussions deeply, identifies patterns of thought, and synthesizes viewpoints into broader insights.
- **Discussion Rounds**: Conducts a series of three rounds where agents discuss the topic from their respective perspectives.
- **Analytical Synthesis**: The moderator provides a comprehensive summary and analysis of the discussion, including its own conclusion on the debate.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/agent-debate-system.git
   cd agent-debate-system

2. Install the required dependencies:

sh
pip install torch transformers autogen

3. Ensure you have the model downloaded and set up. This example uses the Flan-T5-Large model.

## Usage
Run the script:

sh
python debate_system.py
Enter a topic for philosophical discussion when prompted:

Enter a topic for discussion:
The agents will engage in a series of discussions, and the moderator will provide reflections and a final analytical synthesis at the end.

## Code Overview
Here is an overview of the main components of the script:

Model Loading

model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

help me create a github read.me file based on this python code for debate of agents
Sure! Here's a README.md file for your GitHub repository based on the debate of agents Python code:

markdown
# Agent Debate System

This repository contains a Python script for a debate system involving multiple agents and a moderator. The agents engage in discussions on a given topic, exploring different perspectives, while the moderator provides analytical reflections and a comprehensive synthesis at the end.

## Features

- **Agents**: Two agents (Agent 1 and Agent 2) with distinct roles:
  - Agent 1: Intellectual discussion participant who explores positive aspects and potential benefits of the topic.
  - Agent 2: Analytical discussion participant who examines limitations and challenges of the topic.
- **Moderator**: A philosophical observer and critical thinker who analyzes discussions deeply, identifies patterns of thought, and synthesizes viewpoints into broader insights.
- **Discussion Rounds**: Conducts a series of three rounds where agents discuss the topic from their respective perspectives.
- **Analytical Synthesis**: The moderator provides a comprehensive summary and analysis of the discussion, including its own conclusion on the debate.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/agent-debate-system.git
   cd agent-debate-system
Install the required dependencies:

sh
pip install torch transformers autogen
Ensure you have the model downloaded and set up. This example uses the Flan-T5-Large model.

Usage
Run the script:

sh
python debate_system.py
Enter a topic for philosophical discussion when prompted:

Enter a topic for philosophical discussion:
The agents will engage in a series of discussions, and the moderator will provide reflections and a final analytical synthesis at the end.

## Code Overview
Here is an overview of the main components of the script:

## Model Loading
python
model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

## Agent Class
class MyAgent(Agent):
    def __init__(self, name: str, role: str):
        super().__init__()
        self._name = name
        self._role = role

    def generate_text(self, prompt: str) -> str:
        ...
## Run Debate Function
def run_debate(topic: str):
    agent1 = MyAgent("Agent 1", "intellectual discussion participant who explores both positive aspects and potential benefits of the topic, while acknowledging valid counterpoints")
    agent2 = MyAgent("Agent 2", "analytical discussion participant who examines limitations and challenges of the topic, while recognizing legitimate advantages")
    moderator = MyAgent("Moderator", "philosophical observer and critical thinker who analyzes discussions deeply, identifies patterns of thought, and synthesizes viewpoints into broader insights")

    for round_num in range(3):
        ...
    synthesis = moderator.generate_text(synthesis_prompt)

## Main Function
def main():
    threading.Thread(target=load_model).start()
    topic = input("Enter a topic for philosophical discussion: ")
    run_debate(topic)

if __name__ == "__main__":
    main()

## Contribution
Feel free to contribute to this project by submitting issues or pull requests. Any improvements or new features are welcome!

## Note: This script requires a working installation of Python and the necessary libraries listed above. Ensure that you have a compatible environment to run the script successfully.
