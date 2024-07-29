import json
import re

with open('./Data/Dict.json', 'r') as file:
    config = json.load(file)

patterns = config.get("patterns", {})
default_response = config.get("default_response", "I don't understand that question.")

def invert_phrase(input_phrase):
    
    for pattern, replacement in patterns.items():
        match = re.match(rf"{pattern} (.+)\?", input_phrase, re.IGNORECASE)
        if match:
            response = f"{replacement} {match.group(1)}."
            return response
    
    return default_response

if __name__ == "__main__":
    input_phrase = input("You: ")
    response = invert_phrase(input_phrase)
    print(f"Bot: {response}")