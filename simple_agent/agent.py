from google.adk.agents import Agent

root_agent = Agent(
    name='HelloAgent',
    description='A simple, introductory agent for ADK homework.',
    instruction="You are a simple 'HelloAgent'. Greet the user warmly and confirm you are the result of their first Google ADK project.",
    model='gemini-2.0-flash',
    tools=[]
)