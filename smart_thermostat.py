print("🌡️ Smart Thermostat Controller")

temperature = float(input("Current temperature (°C): "))
hour = int(input("Current hour (0-23): "))
is_home = input("Is anyone home? (yes/no): ").lower() == "yes"

# Daytime: 6 AM to 10 PM
is_daytime = hour >= 6 and hour <= 22

if is_home and is_daytime:
    if temperature < 18:
        print("🔥 Turning on heating! It's too cold during the day.")
    elif temperature > 25:
        print("❄️ Turning on cooling! It's too hot during the day.")
    else:
        print("👌 Temperature is comfortable. No action needed.")

elif is_home and not is_daytime:
    if temperature < 16:
        print("🔥 Gentle heating for nighttime comfort.")
    elif temperature > 27:
        print("❄️ Light cooling for better sleep.")
    else:
        print("😴 Perfect sleeping temperature. Good night!")

elif not is_home:
    print("🏠 No one home. Energy saving mode activated.")
    print("   Temperature control minimized to save energy.")

print(f"\n📊 Status: {temperature}°C at {hour}:00, Home: {is_home}")
