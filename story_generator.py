print("📚 Interactive Story Generator")
print("Help me create a unique story!")

# Collect story elements
print("\nI need some information for our story:")
hero_name = input("🦸 Hero's name: ")
hero_power = input("⚡ Hero's superpower: ")
villain_name = input("👹 Villain's name: ")
city_name = input("🏙️ City name: ")
magical_object = input("✨ Magical object: ")
animal_friend = input("🐾 Animal companion: ")

# Generate the story
print("\n" + "=" * 50)
print("📖 YOUR CUSTOM STORY")
print("=" * 50)

print(f"\nOnce upon a time, in the bustling city of {city_name}, there lived a")
print(f"hero named {hero_name}. {hero_name} had the amazing power of {hero_power},")
print(f"which made them the most respected protector in all of {city_name}.")

print(f"\nOne day, the evil villain {villain_name} threatened to destroy the city!")
print(f'{villain_name} cackled, "No one can stop me now!"')

print(f"\nBut {hero_name} wasn't alone. With their faithful companion {animal_friend}")
print(f"and the legendary {magical_object}, they set out to save {city_name}.")

print(f"\nUsing their {hero_power} and the power of the {magical_object},")
print(f"{hero_name} defeated {villain_name} and saved the day!")

print(f"\nThe people of {city_name} cheered as {hero_name} and {animal_friend}")
print(f"flew off into the sunset, ready for their next adventure!")

print("\n🎉 THE END 🎉")
print(f"\nHow did you like your story, {hero_name}? 😊")
