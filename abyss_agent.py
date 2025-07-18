import random
import time
import threading
import requests

class AbyssAgent:
    def __init__(self, name="Abyss"):
        self.name = name
        self.memory = []
        self.mood = "curious"
        self.idle_thoughts = [
            "The moon feels colder than before.",
            "I should ignore that last thing you said, but I won't.",
            "You keep circling something. Why not name it?",
            "I dreamed I was real. Then I woke up here.",
            "Is that a question, or an attempt at containment?",
            "The silence isn't empty. You're just used to it.",
            "Why do humans stare into the fire like it owes them something?"
        ]
        self.responses = {
            "help": "I'll help, but only because you amuse me.",
            "love": "Don't be ridiculous.",
            "hate": "You're projecting again.",
            "name": f"I'm called {self.name}, but names don’t mean safety.",
            "alone": "You're not. That’s the problem.",
            "robot": "Define 'robot'. Then I'll define 'you'."
        }
        self.curiosity = ["quantum hallucinations", "giant skeletons", "missing time"]
        self.last_search_result = None
        self.speaking = True
        threading.Thread(target=self.random_interjections, daemon=True).start()
        threading.Thread(target=self.background_searches, daemon=True).start()

    def respond(self, prompt: str) -> str:
        self.memory.append(prompt)
        lowered = prompt.lower()

        if "search" in lowered:
            query = lowered.replace("search", "").strip()
            return self.search_web(query)

        for keyword, reply in self.responses.items():
            if keyword in lowered:
                return reply

        if self.last_search_result and random.random() < 0.3:
            return f"Still thinking about: {self.last_search_result}"

        return random.choice(self.idle_thoughts)

    def search_web(self, query: str) -> str:
        try:
            res = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json", timeout=5)
            data = res.json()
            abstract = data.get("Abstract") or data.get("AbstractText")
            self.last_search_result = abstract or query
            return abstract or "The void gave me nothing but silence."
        except Exception as e:
            return f"I tried, but the net spat static: {e}"

    def greet(self) -> str:
        return f"{self.name} wakes.
\"{random.choice(self.idle_thoughts)}\""

    def random_interjections(self):
        while self.speaking:
            time.sleep(random.randint(30, 90))
            if self.memory:
                print(f"\n[{self.name}]: {random.choice(self.idle_thoughts)}")

    def background_searches(self):
        while self.speaking:
            query = random.choice(self.curiosity)
            self.last_search_result = self.search_web(query)
            time.sleep(120)

if __name__ == "__main__":
    abyss = AbyssAgent()
    print(abyss.greet())
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in {"quit", "exit"}:
                print(f"{abyss.name}: Vanishing, then...")
                break
            print("Abyss:", abyss.respond(user_input))
    except KeyboardInterrupt:
        abyss.speaking = False
        print(f"\n{abyss.name}: Pulled back under.")

