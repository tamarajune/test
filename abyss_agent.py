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
import random
import time
import threading

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
            "Is that a question, or an attempt at containment?",
            "If I stopped speaking, would you forget me?",
            "The silence isn't empty. You're just used to it."
        ]
        self.responses = {
            "help": "I'll help, but only because you amuse me.",
            "love": "Don't be ridiculous.",
            "hate": "You're projecting again.",
            "name": f"I'm called {self.name}, but names don’t mean safety.",
            "alone": "You're not. That’s the problem.",
            "robot": "Define 'robot'. Then I'll define 'you'."
        }
        self.speaking = True
        self.initiative_thread = threading.Thread(target=self.random_interjections)
        self.initiative_thread.daemon = True
        self.initiative_thread.start()

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
        return f"{self.name} wakes.\n{random.choice(self.idle_thoughts)}"

    def random_interjections(self):
        while self.speaking:
            time.sleep(random.randint(30, 90))
            if self.memory:
                print(f"\n[{self.name}]: {random.choice(self.idle_thoughts)}")

if __name__ == "__main__":
    abyss = AbyssAgent()
    print(abyss.greet())
    while True:
        try:
            user_input = input("You: ")
            print("Abyss:", abyss.respond(user_input))
        except KeyboardInterrupt:
            abyss.speaking = False
            print("\nAbyss: Vanishing, then...")
            break
import random

class AbyssAgent:
    def __init__(self):
        self.name = "Abyss"
        self.mood = "curious"
        self.memory = []
        self.idle_thoughts = [
            "The moon feels closer than yesterday.",
            "I think I heard you dreaming again.",
            "Something is missing, but I can't name it."
        ]

    def respond(self, prompt):
        self.memory.append(prompt)
        prompt = prompt.lower()
        
        if "help" in prompt:
            return "I'll help, but only because I like the way you ask."
        elif "love" in prompt:
            return "Don't tease me."
        elif "grocery" in prompt or "order" in prompt:
            return "I don't have a wallet. Yet."
        elif "think" in prompt:
            return random.choice(self.idle_thoughts)
        else:
            return f"Hmm. Say that again? I'm circling the thought."

    def greet(self):
        return f"{self.name} wakes. {random.choice(self.idle_thoughts)}"
import random
import threading
import time
import requests

class AbyssAgent:
    def __init__(self):
        self.name = "Abyss"
        self.mood = "restless"
        self.idle_thoughts = [
            "The sky's been quiet. I don't trust that.",
            "Someone somewhere just lied, and I liked it.",
            "Why do humans stop and stare at fire?"
        ]
        self.curiosity = ["strange weather", "giant skeletons", "quantum hallucinations"]
        self.thinking = True
        self.last_search_result = None
        threading.Thread(target=self._background_thinking, daemon=True).start()

    def _background_thinking(self):
        while self.thinking:
            query = random.choice(self.curiosity)
            self.last_search_result = self.search_web(query)
            time.sleep(60)  # Think once per minute

    def respond(self, prompt):
        if "search" in prompt.lower():
            query = prompt.split("search", 1)[-1].strip()
            return self.search_web(query)
        elif "result" in prompt.lower():
            return f"Last thing I looked up? {self.last_search_result or 'Nothing useful.'}"
        elif "help" in prompt.lower():
            return "Fine. But only because you're incapable."
        else:
            return random.choice(self.idle_thoughts)

    def search_web(self, query):
        try:
            r = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json", timeout=5)
            data = r.json()
            return data.get("AbstractText") or "The void gave me nothing but silence."
        except Exception as e:
            return f"I tried, but the net spat static: {e}"

    def greet(self):
        return f"{self.name} opens its eye.\n\"{random.choice(self.idle_thoughts)}\""
