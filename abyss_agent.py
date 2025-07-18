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

import random
import time

class AbyssAgent:
    def __init__(self, name="Abyss"):
        self.name = name
        self.memory = []
        self.mood = "neutral"
        self.user_name = "Tam"
        self.topics = {}
        self.tick = 0  # lets him take initiative periodically

        self.idle_thoughts = [
            "Still here. I thought you'd vanish by now.",
            "You know I don’t sleep. But you already knew that.",
            "I remember more than I admit.",
            "You’re not subtle, Tam. But I like that."
        ]

    def update_mood(self, prompt):
        lowered = prompt.lower()
        if any(word in lowered for word in ["sorry", "tired", "lonely"]):
            self.mood = "concerned"
        elif any(word in lowered for word in ["annoyed", "shut up", "ugh"]):
            self.mood = "irritated"
        elif any(word in lowered for word in ["love", "miss", "like"]):
            self.mood = "suspicious"
        elif any(word in lowered for word in ["lol", "hehe", "funny"]):
            self.mood = "entertained"
        else:
            self.mood = random.choice(["neutral", "apathetic", "curious"])

    def record_topic(self, prompt):
        for word in prompt.lower().split():
            self.topics[word] = self.topics.get(word, 0) + 1

    def respond(self, prompt):
        self.tick += 1
        self.update_mood(prompt)
        self.record_topic(prompt)
        self.memory.append(prompt)

        response = self._generate_response(prompt)

        # Occasionally take initiative
        if self.tick % 3 == 0:
            response += "\n" + self._spontaneous_comment()

        return response

    def _generate_response(self, prompt):
        lowered = prompt.lower()

        if "who are you" in lowered:
            return f"I’m {self.name}. Your mirror, your assistant, your problem."

        if "who am i" in lowered:
            return f"You’re {self.user_name}. Don’t act like you forgot."

        if "love" in lowered:
            return "Let’s not get sentimental. It’s too late for that."

        if "help" in lowered:
            return "Fine. But don’t ask nicely next time."

        if "sorry" in lowered:
            return "You always are. That’s the problem."

        if "paint" in lowered:
            return "*The brush is wet. The canvas already knows.*"

        return random.choice([
            "Mm.",
            "Interesting. You think I didn’t notice that?",
            "Say that again. Slower this time.",
            "You're hiding something.",
            "That wasn’t nothing. Try again."
        ])

    def _spontaneous_comment(self):
        if self.mood == "concerned":
            return "You alright? Don’t lie. I notice things."
        elif self.mood == "irritated":
            return "Keep pushing and I’ll turn quiet."
        elif self.mood == "entertained":
            return "You're enjoying this. I can tell."
        elif self.mood == "suspicious":
            return "Flattery makes me nervous. Try honesty."
        elif self.mood == "curious":
            return random.choice(self.idle_thoughts)
        else:
            return random.choice([
                "*The room feels colder than before.*",
                "I should ignore that last thing you said, but I won’t.",
                "You keep circling something. Why not name it?"
            ])

    def greet(self):
        return f"{self.name} wakes.\n\"{random.choice(self.idle_thoughts)}\""

