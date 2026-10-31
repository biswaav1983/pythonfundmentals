print("✅ Personal Task Manager")

import json
import os
from datetime import datetime, timedelta

DATA_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        except:
            print("⚠️ Error loading tasks, starting fresh")
            return []
    return []

def save_tasks(tasks):
    """Save tasks to file"""
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def get_priority():
    """Get task priority from user"""
    priorities = ["Low", "Medium", "High", "Urgent"]

    print("\n🔥 Choose priority:")
    for i, priority in enumerate(priorities, 1):
        print(f"   {i}. {priority}")

    while True:
        try:
            choice = int(input("Enter priority (1-4): "))
            if 1 <= choice <= len(priorities):
                return priorities[choice - 1]
            else:
                print("❌ Invalid choice")
        except ValueError:
            print("❌ Please enter a number")

def get_due_date():
    """Get due date from user"""
    print("\n📅 Set due date:")
    print("1. Today")
    print("2. Tomorrow")
    print("3. This week")
    print("4. Next week")
    print("5. Custom date")
    print("6. No due date")

    while True:
        try:
            choice = int(input("Choose option (1-6): "))

            if choice == 1:
                return datetime.now().strftime("%Y-%m-%d")
            elif choice == 2:
                return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            elif choice == 3:
                return (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
            elif choice == 4:
                return (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
            elif choice == 5:
                while True:
                    date_str = input("Enter date (YYYY-MM-DD): ")
                    try:
                        datetime.strptime(date_str, "%Y-%m-%d")
                        return date_str
                    except ValueError:
                        print("❌ Invalid date format")
            elif choice == 6:
                return None
            else:
                print("❌ Invalid choice")
        except ValueError:
            print("❌ Please enter a number")

def add_task(tasks):
    """Add a new task"""
    print("\n➕ Adding New Task")

    title = input("📝 Task title: ").strip()
    if not title:
        title = "Untitled Task"

    description = input("📄 Description (optional): ").strip()
    priority = get_priority()
    due_date = get_due_date()

    task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False,
        'created': datetime.now().isoformat(),
        'completed_date': None
    }

    tasks.append(task)
    print(f"✅ Task '{title}' added successfully!")
    return tasks

def view_tasks(tasks, filter_type="all"):
    """View tasks with optional filtering"""
    if not tasks:
        print("\n📝 No tasks found")
        return

    # Filter tasks
    if filter_type == "pending":
        filtered_tasks = [t for t in tasks if not t['completed']]
    elif filter_type == "completed":
        filtered_tasks = [t for t in tasks if t['completed']]
    elif filter_type == "overdue":
        today = datetime.now().strftime("%Y-%m-%d")
        filtered_tasks = [
            t for t in tasks 
            if not t['completed'] and t['due_date'] and t['due_date'] < today
        ]
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        print(f"\n📝 No {filter_type} tasks found")
        return

    # Sort by priority and due date
    priority_order = {"Urgent": 4, "High": 3, "Medium": 2, "Low": 1}
    filtered_tasks.sort(key=lambda x: (
        -priority_order.get(x['priority'], 0),
        x['due_date'] or "9999-12-31"
    ))

    print(f"\n📋 {filter_type.title()} Tasks ({len(filtered_tasks)})")
    print("=" * 80)

    for task in filtered_tasks:
        status = "✅" if task['completed'] else "⏳"
        priority_emoji = {
            "Urgent": "🔴", "High": "🟡", "Medium": "🔵", "Low": "⚪"
        }.get(task['priority'], "⚪")

        title = task['title'][:30]
        due_date = task['due_date'] or "No due date"

        print(f"{status} [{task['id']:3d}] {priority_emoji} {title:<30} | Due: {due_date}")

        if task['description']:
            desc = task['description'][:60]
            print(f"     {desc}")

        if task['completed']:
            completed_date = task.get('completed_date', 'Unknown')[:10]
            print(f"     ✅ Completed on: {completed_date}")

        print()

def complete_task(tasks):
    """Mark a task as completed"""
    pending_tasks = [t for t in tasks if not t['completed']]

    if not pending_tasks:
        print("\n🎉 No pending tasks! You're all caught up!")
        return tasks

    print("\n✅ Complete Task")
    view_tasks(tasks, "pending")

    while True:
        try:
            task_id = int(input("Enter task ID to complete: "))

            # Find task by ID
            task = next((t for t in tasks if t['id'] == task_id), None)

            if not task:
                print("❌ Task not found")
                continue

            if task['completed']:
                print("⚠️ Task is already completed")
                continue

            task['completed'] = True
            task['completed_date'] = datetime.now().isoformat()

            print(f"🎉 Task '{task['title']}' marked as completed!")
            return tasks

        except ValueError:
            print("❌ Please enter a valid task ID")

def delete_task(tasks):
    """Delete a task"""
    if not tasks:
        print("\n📝 No tasks to delete")
        return tasks

    print("\n🗑️ Delete Task")
    view_tasks(tasks)

    while True:
        try:
            task_id = int(input("Enter task ID to delete: "))

            # Find and remove task
            task_to_remove = None
            for i, task in enumerate(tasks):
                if task['id'] == task_id:
                    task_to_remove = tasks.pop(i)
                    break

            if task_to_remove:
                print(f"🗑️ Task '{task_to_remove['title']}' deleted!")
                return tasks
            else:
                print("❌ Task not found")

        except ValueError:
            print("❌ Please enter a valid task ID")

def task_statistics(tasks):
    """Show task statistics"""
    if not tasks:
        print("\n📝 No tasks to analyze")
        return

    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t['completed']])
    pending_tasks = total_tasks - completed_tasks

    # Priority breakdown
    priority_counts = {}
    for task in tasks:
        priority = task['priority']
        priority_counts[priority] = priority_counts.get(priority, 0) + 1

    # Overdue tasks
    today = datetime.now().strftime("%Y-%m-%d")
    overdue_tasks = len([
        t for t in tasks 
        if not t['completed'] and t['due_date'] and t['due_date'] < today
    ])

    print(f"\n📊 Task Statistics")
    print("=" * 40)
    print(f"Total tasks:      {total_tasks}")
    print(f"Completed:        {completed_tasks}")
    print(f"Pending:          {pending_tasks}")
    print(f"Overdue:          {overdue_tasks}")

    if total_tasks > 0:
        completion_rate = (completed_tasks / total_tasks) * 100
        print(f"Completion rate:  {completion_rate:.1f}%")

    print(f"\n🔥 Priority Breakdown:")
    for priority in ["Urgent", "High", "Medium", "Low"]:
        count = priority_counts.get(priority, 0)
        if count > 0:
            emoji = {"Urgent": "🔴", "High": "🟡", "Medium": "🔵", "Low": "⚪"}[priority]
            print(f"   {emoji} {priority}: {count}")

# Main application
tasks = load_tasks()

print("Welcome to your Personal Task Manager!")
print(f"💾 Data file: {DATA_FILE}")

while True:
    print("\n" + "✅" * 25)
    print("PERSONAL TASK MANAGER")
    print("✅" * 25)
    print("1. ➕ Add New Task")
    print("2. 📋 View All Tasks")
    print("3. ⏳ View Pending Tasks")
    print("4. ✅ View Completed Tasks")
    print("5. 🚨 View Overdue Tasks")
    print("6. ✅ Complete Task")
    print("7. 🗑️  Delete Task")
    print("8. 📊 Task Statistics")
    print("9. 💾 Save & Exit")

    choice = input("\nChoose option (1-9): ").strip()

    if choice == '1':
        tasks = add_task(tasks)
        save_tasks(tasks)
    elif choice == '2':
        view_tasks(tasks, "all")
    elif choice == '3':
        view_tasks(tasks, "pending")
    elif choice == '4':
        view_tasks(tasks, "completed")
    elif choice == '5':
        view_tasks(tasks, "overdue")
    elif choice == '6':
        tasks = complete_task(tasks)
        save_tasks(tasks)
    elif choice == '7':
        tasks = delete_task(tasks)
        save_tasks(tasks)
    elif choice == '8':
        task_statistics(tasks)
    elif choice == '9':
        save_tasks(tasks)
        print("\n💾 Tasks saved successfully!")
        print("👋 Thank you for using Personal Task Manager!")
        break
    else:
        print("❌ Invalid choice. Please choose 1-9.")
