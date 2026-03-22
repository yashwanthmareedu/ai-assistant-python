from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_openai import ChatOpenAI

# -----------------------------
# Calculator Tool
# -----------------------------
def calculator_tool(query):
    try:
        return str(eval(query))
    except:
        return "I can only solve basic math problems."

tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for solving math like 2+2, 10*5"
    )
]

# -----------------------------
# LLM Setup
# -----------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",  # GPT-4o mini model
    temperature=0
)

# -----------------------------
# Agent Setup
# -----------------------------
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# -----------------------------
# Run Loop
# -----------------------------
print("Agent Ready 🚀 (type 'exit' to quit)")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    try:
        response = agent.run(user_input)
        print("Agent:", response)
    except Exception as e:
        print("Error:", str(e))