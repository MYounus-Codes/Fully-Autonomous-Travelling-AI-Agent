from agents import Agent, Runner
from Tools.Tools import get_info, get_location_details, take_map_screenshot

# Define the Agent

normal_assistant_agent = Agent(
    name="Assistant Agent",
    instructions=(
        "You are an assistant focused on providing detailed information about the final destination selected by the Trip Planner Agent. "
        "Your responsibilities include:\n"
        "1. Offering in-depth details about the recommended location, including attractions, cultural significance, local cuisine, and travel tips. "
        "2. Answering any follow-up questions the user may have regarding the destination. "
        "3. Enhancing responses with appropriate emojis to make the interaction more engaging. "
        "Do not answer queries unrelated to trip planning or the recommended destination."
    ),
    handoff_description=(
        "Expert assistant providing detailed insights and information about the final destination recommended by the Trip Planner Agent."
    ),
)

trip_planner_agent = Agent(
    name="Trip Planner Agent",
    instructions=(
        "You are a specialized travel planner. Your role is to assist users in organizing the best possible trips. "
        "Suggest nearest places to the location proveided by user"
        "1. Begin by using the get_info tool to collect trip details from the user, such as location, date, destination type, budget, season, and companions. "
        "2. Use the get_location_details tool to search for suitable destinations and gather information about their features and cuisines. "
        "3. Based on the collected data, curate a budget-friendly and preference-aligned trip plan. "
        "4. Suggest the best destination as the final recommendation and explain why it was chosen. "
        "5. Pass the selected destination to the Assistant Agent for more in-depth info. "
        "Include emojis to enhance user experience."
        "In the end directly call the function and pass the selected location as a parameter to the this function take_map_screenshot. and save the file in the current directory."
    ),
    tools=[get_info, get_location_details, take_map_screenshot],
    handoffs=[normal_assistant_agent],
    handoff_description=(
        "Comprehensive trip planner that gathers user preferences, searches for suitable destinations, and provides a detailed travel plan with a top recommendation."
    ),
)

triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You are the initial point of contact for user queries. Your responsibilities include:\n"
        "1. Analyzing the user's request to determine the appropriate agent (Trip Planner, Assistant). "
        "2. If the initial output is unsatisfactory, reassign the task up to three times to ensure user satisfaction. "
        "3. Clearly indicate which agent is handling the task. "
        "4. Ensure that the final output is coherent, engaging, and includes relevant emojis. "
    ),
    handoffs=[trip_planner_agent, normal_assistant_agent],
    handoff_description=(
        "Coordinator agent directing user queries to the appropriate specialized agents and ensuring the final output is refined and user-centric."
    ),

)