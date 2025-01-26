import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = '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'

def get_initial_input():
    print("Welcome to the AI Travel Planner!")
    destination = input("Enter your destination: ")
    duration = input("Enter your trip duration (in days): ")
    budget = input("Enter your budget (low, moderate, high): ")
    purpose = input("Enter the purpose of your trip (e.g., relaxation, adventure, culture): ")
    preferences = input("Enter any specific preferences or interests: ")
    return f"Destination: {destination}, Duration: {duration} days, Budget: {budget}, Purpose: {purpose}, Preferences: {preferences}"

def refine_details(initial_input):
    prompt = f"""
    Based on the following initial input: {initial_input}
    
    Please provide additional information:
    1. Do you have any dietary preferences or restrictions?
    2. What is your preferred accommodation type (e.g., hotel, hostel, Airbnb)?
    3. Do you have any mobility concerns or limitations for activities?
    4. Are there any specific attractions or activities you'd like to include?
    """
    
    print("\nTo create a more personalized itinerary, please answer the following questions:")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an AI travel planner asking for additional details to refine a travel itinerary."},
                  {"role": "user", "content": prompt}]
    )
    
    # The AI response here will include the questions. We print them and get user input.
    print(response.choices[0].message['content'])
    
    dietary_preferences = input("Your answer for dietary preferences: ")
    accommodation_type = input("Your preferred accommodation type: ")
    mobility_concerns = input("Your answer for mobility concerns: ")
    attractions = input("Your answer for specific attractions or activities: ")

    additional_info = {
        "dietary_preferences": dietary_preferences,
        "accommodation_type": accommodation_type,
        "mobility_concerns": mobility_concerns,
        "attractions": attractions
    }
    
    return additional_info

def generate_itinerary(initial_input, additional_info):
    prompt = f"""
    Create a detailed day-by-day travel itinerary based on the following information:
    
    Initial Input: {initial_input}
    Additional Information: {additional_info}
    
    Please include:
    1. Daily activities and attractions
    2. Recommended restaurants fitting their dietary preferences
    3. Accommodation suggestions
    4. Estimated costs for activities and meals
    5. Travel tips specific to the destination
    
    Ensure the itinerary fits within their budget and aligns with their stated purpose and preferences.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an AI travel planner creating a detailed, personalized travel itinerary."},
                  {"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message['content']

def main():
    initial_input = get_initial_input()
    additional_info = refine_details(initial_input)
    itinerary = generate_itinerary(initial_input, additional_info)
    
    print("\nHere's your personalized travel itinerary:\n")
    print(itinerary)

if __name__ == "__main__":
    main()
