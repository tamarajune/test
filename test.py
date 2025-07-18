from abyss_agent import AbyssAgent

abyss = AbyssAgent()
print(abyss.greet())

while True:
    user = input("You: ")
    print("Abyss:", abyss.respond(user))
from abyss_agent import AbyssAgent
def main() -> None:
    abyss = AbyssAgent()
    print(abyss.greet())
    try:
        while True:
            user = input("You: ")
            if user.lower() in {"quit", "exit"}:
                break
            print("Abyss:", abyss.respond(user))
    except KeyboardInterrupt:
        pass

abyss = AbyssAgent()

while True:
    user = input("You: ")
    if user.lower() in ["quit", "exit"]:
        break
    print("Abyss:", abyss.respond(user))
if __name__ == "__main__":
    main()
