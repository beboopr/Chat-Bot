import json
from difflib import get_close_matches

#Load knowledge base
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

#Save knowledge base - to reuse in the future
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

#Find best match for answer
def find_best_match(user_question: str, questions: list[str])-> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

#Get answer for question
def get_answer(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q ["question"] == question:
            return q ["answer"]
        




def chat_bot();
    knowledge_base: dict = load_knowledge_base("knowledge_base.json")