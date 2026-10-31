print("🌧️ Outdoor Activity Planner")

is_raining = input("Is it raining? (yes/no): ").lower() == "yes"

if not is_raining:
    print("☀️ Great! It's not raining!")
    print("   Perfect weather for outdoor activities!")
    print("   You could go for a walk, bike ride, or picnic!")
else:
    print("🏠 It's raining, so let's stay indoors!")
    print("   Good time for reading, movies, or cooking!")

print("\n🎯 Make the most of your day!")
