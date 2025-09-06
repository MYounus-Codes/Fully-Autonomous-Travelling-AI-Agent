import asyncio
from agents import Runner
from Agents.Agents import triage_agent
from History.History import ConversationHistory
from LLm_Setup.llm import config

# Main function to run the agent
async def main():
    history = ConversationHistory()
    
    print("Trip Planner Bot: Hello! I can help you plan your trip. Type 'exit' to end the conversation or 'clear' to start fresh.")
    
    while True:
        user = input("Enter Query: ")
        
        if user.lower() == 'exit':
            print("Trip Planner Bot: Goodbye!")
            break

        if user.lower() == 'clear':
            history.clear()
            print("Trip Planner Bot: Conversation history cleared. Let's start fresh!")
            continue

        # Add user message to history
        history.add_message("user", user)
        
        # Update the Runner.run call to include conversation history
        result = await Runner.run(
            starting_agent=triage_agent, 
            input=user, 
            run_config=config,
            context={"conversation_history": history.get_history()}
        )
        
        # Add assistant's response to history
        history.add_message("assistant", result.final_output)
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
    