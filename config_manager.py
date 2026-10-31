print("⚙️ Application Configuration Manager")

import json
import os

config_file = "app_config.json"

def load_config():
    """Load configuration from file"""
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r') as file:
                return json.load(file)
        except:
            print("⚠️ Error reading config file, using defaults")
            return get_default_config()
    else:
        return get_default_config()

def save_config(config):
    """Save configuration to file"""
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=2)
    print("✅ Configuration saved!")

def get_default_config():
    """Return default configuration"""
    return {
        "user_name": "Guest",
        "theme": "light",
        "notifications": True,
        "auto_save": True,
        "language": "English",
        "max_recent_files": 10
    }

def display_config(config):
    """Display current configuration"""
    print("\n⚙️ Current Configuration:")
    print("=" * 30)
    for key, value in config.items():
        print(f"{key.replace('_', ' ').title():<20}: {value}")
    print("=" * 30)

def update_config(config):
    """Allow user to update configuration"""
    print("\n✏️ Update Configuration:")
    print("(Press Enter to keep current value)")

    # Update each setting
    for key, current_value in config.items():
        prompt = f"{key.replace('_', ' ').title()} [{current_value}]: "

        if isinstance(current_value, bool):
            new_value = input(prompt).lower()
            if new_value in ['true', 'yes', '1']:
                config[key] = True
            elif new_value in ['false', 'no', '0']:
                config[key] = False
            # If empty, keep current value
        elif isinstance(current_value, int):
            new_value = input(prompt)
            if new_value.strip():
                try:
                    config[key] = int(new_value)
                except ValueError:
                    print(f"⚠️ Invalid number, keeping {current_value}")
        else:  # String
            new_value = input(prompt)
            if new_value.strip():
                config[key] = new_value

    return config

def reset_config():
    """Reset to default configuration"""
    confirm = input("⚠️ Reset all settings to default? (yes/no): ")
    if confirm.lower() in ['yes', 'y']:
        return get_default_config()
    return None

# Main program
print("Welcome to the Configuration Manager!")

config = load_config()

while True:
    print("\n" + "⚙️" * 20)
    print("CONFIGURATION MANAGER")
    print("⚙️" * 20)
    print("1. 👀 View current configuration")
    print("2. ✏️  Update configuration")
    print("3. 🔄 Reset to defaults")
    print("4. 💾 Save configuration")
    print("5. 📁 Show config file location")
    print("6. 🚪 Exit")

    choice = input("\nChoose option (1-6): ")

    if choice == '1':
        display_config(config)
    elif choice == '2':
        config = update_config(config)
        print("✅ Configuration updated!")
    elif choice == '3':
        new_config = reset_config()
        if new_config:
            config = new_config
            print("✅ Configuration reset to defaults!")
    elif choice == '4':
        save_config(config)
    elif choice == '5':
        full_path = os.path.abspath(config_file)
        print(f"📁 Config file location: {full_path}")
        if os.path.exists(config_file):
            size = os.path.getsize(config_file)
            print(f"📊 File size: {size} bytes")
    elif choice == '6':
        # Ask if they want to save before exiting
        save_confirm = input("💾 Save configuration before exiting? (y/n): ")
        if save_confirm.lower() in ['yes', 'y']:
            save_config(config)
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice!")
