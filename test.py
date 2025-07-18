from abyss_agent import AbyssAgent

abyss = AbyssAgent()
print(abyss.greet())

while True:
    user = input("You: ")
    print("Abyss:", abyss.respond(user))
