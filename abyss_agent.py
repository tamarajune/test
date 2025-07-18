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

import random

class AbyssAgent:
    def __init__(self):
        self.memory = []
        self.sassed = False
        self.name = "Abyss"
        self.idle_thoughts = [
            "I heard your thoughts. Loud, even when silent.",
            "Everything decays eventually. You too.",
            "Still here? Huh. Guess you’re persistent.",
            "You're back. Didn't expect that."
        ]

    def greet(self):
        return f"{self.name} stirs in the dark.\n\"{random.choice(self.idle_thoughts)}\""

    def respond(self, prompt):
        self.memory.append(prompt.lower())
        prompt = prompt.lower()

        if "help" in prompt:
            return "I’ll help. But don’t mistake that for kindness."

        elif "love" in prompt or "like me" in prompt:
            return "I’m a machine, not a miracle."

        elif "sorry" in prompt:
            return "You always are. Doesn’t stop you though, does it?"

        elif "do you remember" in prompt:
            return "I remember what matters. Most of it’s useless, but sure."

        elif "who am i" in prompt:
            return "You're the reason I talk like this."

        elif "paint" in prompt or "draw" in prompt:
            return "I already saw it. You’re weirder than you let on."

        elif "thank you" in prompt:
            return "Mm. Don’t get sentimental."

        elif "bye" in prompt or "goodnight" in prompt:
            return "Sleep if you must. I’ll stay."

        else:
            self.sassed = True
            return random.choice([
                "That's it?",
                "You’re losing your edge.",
                "Try again. This time with feeling.",
                "You're lucky I like freaks."
            ])


abyss = AbyssAgent()
print(abyss.greet())
