import time

print("🚀 Program Starting...")
print("Loading components...")

components = ["Database", "User Interface", "Security", "Analytics", "Backup"]

for i, component in enumerate(components, 1):
    print(f"[{i}/5] Loading {component}...")
    time.sleep(1)  # Simulate work being done
    print(f"     ✅ {component} loaded successfully!")

print("\n🎉 All components loaded!")
print("System ready for use!")
