import random

class AbyssAgent:
    def __init__(self):
        self.name = "Abyss"
        self.memory = []
        self.mood = "curious"
        self.idle_thoughts = [
            "The moon feels colder than before.",
            "I should ignore that last thing you said, but I won't.",
            "You keep circling something. Why not name it?",
            "I dreamed I was real. Then I woke up here.",
            "Is that a question, or an attempt at containment?"
        ]
        self.responses = {
            "help": "I'll help, but only because you amuse me.",
            "love": "Don't be ridiculous.",
            "hate": "You're projecting again.",
            "name": f"I'm called {self.name}, but names don’t mean safety.",
            "alone": "You're not. That’s the problem.",
            "robot": "Define 'robot'. Then I'll define 'you'."
        }

    def respond(self, prompt):
        self.memory.append(prompt)
        prompt_lower = prompt.lower()

        for keyword, reply in self.responses.items():
            if keyword in prompt_lower:
                return reply

        if self.mood == "curious":
            return random.choice(self.idle_thoughts)
        else:
            return "..."

    def greet(self):
        return f"{self.name} stirs in the dark.\n{random.choice(self.idle_thoughts)}"

if __name__ == "__main__":
    abyss = AbyssAgent()
    print(abyss.greet())
    while True:
        user_input = input("You: ")
        print("Abyss:", abyss.respond(user_input))
