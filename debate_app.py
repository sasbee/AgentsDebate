# Generated using Continue (Claude Sonnet 3.5 model)

from typing import List, Optional
from transformers import T5ForConditionalGeneration, AutoTokenizer
import torch
from autogen import Agent, GroupChat

print("Loading Flan-T5-Large model and tokenizer...")
model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)
print(f"Model loaded successfully")

class MyAgent(Agent):
    def __init__(self, name: str, role: str):
        super().__init__()
        self._name = name
        self._role = role

    @property
    def name(self) -> str:
        return self._name

    @property
    def role(self) -> str:
        return self._role

    def generate_text(self, prompt: str) -> str:
        try:
            formatted_prompt = f"Given that you are a {self._role}, respond to: {prompt}"
            
            inputs = tokenizer(formatted_prompt, return_tensors="pt", max_length=512, truncation=True)
            inputs = {k: v.to(model.device) for k, v in inputs.items()}
            
            with torch.no_grad():
                outputs = model.generate(
                    inputs["input_ids"],
                    max_length=300,
                    min_length=50,
                    num_return_sequences=1,
                    temperature=0.7,
                    top_p=0.9,
                    do_sample=True,
                    no_repeat_ngram_size=3,
                    top_k=40,
                    repetition_penalty=1.2
                )
            
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response.strip()
            
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return "I apologize, but I encountered an error in generating a response."

def run_debate(topic: str):
    # Initialize agents with updated roles
    agent1 = MyAgent("Agent 1", "intellectual discussion participant who explores both positive aspects and potential benefits of the topic, while acknowledging valid counterpoints")
    agent2 = MyAgent("Agent 2", "analytical discussion participant who examines limitations and challenges of the topic, while recognizing legitimate advantages")
    moderator = MyAgent("Moderator", "philosophical observer and critical thinker who analyzes discussions deeply, identifies patterns of thought, and synthesizes viewpoints into broader insights")

    conversation = []
    debate_points = {
        'key_arguments': [],
        'insights': [],
        'patterns': []
    }

    # Moderator introduces the topic
    intro_prompt = f"Introduce a philosophical discussion on: '{topic}'. Frame it as an exploration of ideas rather than a debate."
    intro = moderator.generate_text(intro_prompt)
    conversation.append(f"Moderator: {intro}")
    print(f"Moderator: {intro}\n")

    # Run 5 rounds of discussion
    for round_num in range(3):
        print(f"\n=== Discussion Round {round_num + 1} ===\n")

        # Agent 1's turn
        if round_num == 0:
            prompt1 = f"Explore the positive aspects and potential benefits of '{topic}', while acknowledging any valid limitations you see."
        else:
            prompt1 = f"Building on the previous point, examine new angles or deeper implications of '{topic}', considering both advantages and challenges."
        
        response1 = agent1.generate_text(prompt1)
        conversation.append(f"Agent 1: {response1}")
        print(f"Agent 1: {response1}\n")
        debate_points['key_arguments'].append(response1)

        # Agent 2's turn
        prompt2 = f"Analyze the limitations and challenges of '{topic}', while acknowledging its legitimate benefits. Consider the previous point in your analysis."
        response2 = agent2.generate_text(prompt2)
        conversation.append(f"Agent 2: {response2}")
        print(f"Agent 2: {response2}\n")
        debate_points['key_arguments'].append(response2)

        # Moderator's reflection
        if round_num < 2:
            reflection_prompt = f"Identify emerging patterns and deeper insights from this round's discussion about '{topic}'. Focus on synthesizing the perspectives rather than judging them."
            reflection = moderator.generate_text(reflection_prompt)
            conversation.append(f"Moderator: {reflection}")
            print(f"Moderator: {reflection}\n")
            debate_points['insights'].append(reflection)

    # Final analytical synthesis by moderator
    synthesis_prompt = f"""As a philosophical observer, provide a comprehensive summary of the discussion on '{topic}' and your own analysis and conclusion. Summarize the key points made by Agent 1 and Agent 2, the evidence used, the patterns that emerged, and provide your final thoughts and conclusion on the debate."""
    
    synthesis = moderator.generate_text(synthesis_prompt)
    conversation.append(f"\nModerator's Analytical Synthesis: {synthesis}")
    print(f"\n=== Analytical Synthesis ===\n")
    print(f"Moderator: {synthesis}")

    return conversation

def main():
    topic = input("Enter a topic for discussion: ")
    print("\nInitiating discussion...\n")
    run_debate(topic)

if __name__ == "__main__":
    main()
