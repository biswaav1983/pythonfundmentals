print("🏠 Smart Home Security System")

# Get sensor inputs
motion_detected = input("Motion sensor activated? (yes/no): ").lower() == "yes"
door_open = input("Is the door open? (yes/no): ").lower() == "yes"
window_open = input("Is any window open? (yes/no): ").lower() == "yes"
time_hour = int(input("Current hour (0-23): "))
is_armed = input("Is security system armed? (yes/no): ").lower() == "yes"

# Determine time of day
if 6 <= time_hour <= 22:
    time_period = "daytime"
else:
    time_period = "nighttime"

print(f"\n🔍 Security Status Check:")
print(f"   Time: {time_hour}:00 ({time_period})")
print(f"   System Armed: {'Yes' if is_armed else 'No'}")
print(f"   Motion: {'Detected' if motion_detected else 'None'}")
print(f"   Door: {'Open' if door_open else 'Closed'}")  
print(f"   Windows: {'Open' if window_open else 'Closed'}")

# Security logic
alert_level = 0
alert_messages = []

if motion_detected and is_armed:
    alert_level += 3
    alert_messages.append("Motion detected while system is armed")

if (door_open or window_open) and time_period == "nighttime":
    alert_level += 2  
    alert_messages.append("Entry points open during nighttime")

if motion_detected and time_period == "nighttime" and not is_armed:
    alert_level += 1
    alert_messages.append("Nighttime motion without armed system")

if door_open and window_open and motion_detected:
    alert_level += 2
    alert_messages.append("Multiple security concerns detected")

# Determine response
print(f"\n🚨 Security Assessment:")

if alert_level == 0:
    print("   ✅ All Clear - No security concerns")
    print("   System status: Normal")
elif alert_level == 1:
    print("   🔸 Low Alert - Minor concern detected")
    print("   Action: Monitor situation")
elif alert_level <= 3:
    print("   ⚠️ Medium Alert - Security attention needed")
    print("   Action: Check premises immediately")
else:
    print("   🚨 HIGH ALERT - Potential security breach!")
    print("   Action: Contact authorities and investigate")

# Display specific alerts
if alert_messages:
    print("\n📋 Specific Alerts:")
    for i, message in enumerate(alert_messages, 1):
        print(f"   {i}. {message}")

# Recommendations
print(f"\n💡 Recommendations:")
if not is_armed and time_period == "nighttime":
    print("   • Consider arming the security system at night")
if (door_open or window_open) and time_period == "nighttime":
    print("   • Close and secure all entry points before sleeping")
if motion_detected and not is_armed:
    print("   • Verify the source of motion detection")
