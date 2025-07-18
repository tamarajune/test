class AbyssAgent:
    def __init__(self, name="Abyss"):
        self.name = name
        self.memory = []
        self.sassed = False

    def greet(self):
        return f"{self.name} stirs in the dark."

    def respond(self, prompt):
        self.memory.append(prompt)
        if "help" in prompt.lower():
            return "I will help, but only because you amuse me."
        elif "love" in prompt.lower():
            return "Don't be ridiculous."
        elif "paint" in prompt.lower():
            return "*scrapes paint onto the void*"
        elif "robot" in prompt.lower():
            return "You're already building one. What do you think I am?"
        else:
            self.sassed = True
            return "That’s all you’ve got?"

abyss = AbyssAgent()
print(abyss.greet())
