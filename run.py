from dotenv import load_dotenv
load_dotenv()



from agent import Agent

if __name__ == "__main__":
    agent = Agent(model="llama-3.1-8b-instant", max_steps=6)

    prompt = "Analyze Tesla and give me a quick financial snapshot."
    result = agent.run(prompt)

    print("\nFINAL OUTPUT:\n")
    print(result)

print("RUN FILE STARTED")