print("🌤️ Weather Activity Advisor")

temperature = float(input("What's the temperature in Celsius? "))

if temperature >= 30:
    print("🔥 It's very hot!")
    print("   Stay hydrated and find some shade!")
    activity = "swimming or staying indoors"
elif temperature >= 20:
    print("☀️ It's warm and pleasant!")
    print("   Perfect weather for outdoor activities!")
    activity = "going for a walk or picnic"
elif temperature >= 10:
    print("🧥 It's cool but comfortable!")
    print("   A light jacket would be perfect!")
    activity = "outdoor sports with a jacket"
elif temperature >= 0:
    print("❄️ It's cold! Bundle up!")
    print("   Warm clothes are essential!")
    activity = "indoor activities or winter sports"
else:
    print("🧊 It's freezing!")
    print("   Stay warm and safe inside!")
    activity = "staying indoors with hot drinks"

print(f"\n🎯 Recommended activity: {activity}")
