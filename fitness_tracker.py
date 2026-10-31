print("🏃 Health & Fitness Tracker")

age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
exercise_days = int(input("How many days per week do you exercise? "))

# Calculate BMI
height_meters = height / 100
bmi = weight / (height_meters ** 2)

print(f"\n📋 Health Assessment:")
print(f"   Age: {age} years")
print(f"   BMI: {bmi:.1f}")

# BMI categories
if bmi < 18.5:
    bmi_category = "Underweight"
    bmi_advice = "Consider consulting a nutritionist to gain healthy weight"
elif bmi < 25:
    bmi_category = "Normal weight"
    bmi_advice = "Great! Maintain your current healthy weight"
elif bmi < 30:
    bmi_category = "Overweight"
    bmi_advice = "Consider a balanced diet and regular exercise"
else:
    bmi_category = "Obese"
    bmi_advice = "Strongly recommend consulting a healthcare professional"

print(f"   Category: {bmi_category}")
print(f"   Advice: {bmi_advice}")

# Exercise evaluation
print(f"\n🏋️ Exercise Analysis:")
print(f"   Exercise days per week: {exercise_days}")

if exercise_days == 0:
    print("   ❌ No exercise - This is concerning for your health")
    print("   Recommendation: Start with 2-3 days per week")
elif exercise_days < 3:
    print("   🔸 Some exercise - Good start, but could be better")
    print("   Recommendation: Try to reach 3-4 days per week")
elif exercise_days <= 5:
    print("   ✅ Regular exercise - Excellent habit!")
    print("   You're meeting health guidelines")
else:
    print("   🏆 Very active lifestyle - Outstanding!")
    print("   Make sure to include rest days for recovery")

# Overall health score
health_score = 0
if 18.5 <= bmi < 25:
    health_score += 40
elif 25 <= bmi < 30:
    health_score += 25
elif bmi < 18.5 or bmi >= 30:
    health_score += 10

if exercise_days >= 5:
    health_score += 40
elif exercise_days >= 3:
    health_score += 30
elif exercise_days >= 1:
    health_score += 15

if age < 30:
    health_score += 20
elif age < 50:
    health_score += 15
else:
    health_score += 10

print(f"\n🎯 Overall Health Score: {health_score}/100")

if health_score >= 80:
    print("   🌟 Excellent health profile!")
elif health_score >= 60:
    print("   👍 Good health, minor improvements possible")
elif health_score >= 40:
    print("   ⚠️ Average health, focus on improvements")
else:
    print("   🚨 Health needs attention, consider lifestyle changes")
