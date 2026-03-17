import json
from datetime import date

def load_data():
    try:
        with open("habits.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"habits": [], "history": {}}

def save_data(data):
    with open("habits.json", "w") as f:
        json.dump(data, f, indent=4)

def main():
    data = load_data()
    today = str(date.today())
    
    if today not in data["history"]:
        data["history"][today] = []

    while True:
        print(f"\n--- MISSION LOG: {today} ---")
        print("1. View/Check Habits")
        print("2. Add New Habit")
        print("3. View Progress Stats")
        print("4. Exit")
        
        choice = input("\nSelect an action: ")

        if choice == "1":
            if not data["habits"]:
                print("No habits added yet! Use option 2.")
                continue
            
            for i, habit in enumerate(data["habits"]):
                status = "✅" if habit in data["history"][today] else "❌"
                print(f"{i+1}. [{status}] {habit}")
            
            idx = input("\nEnter number to toggle (or 'b' to go back): ")
            if idx.isdigit() and 0 < int(idx) <= len(data["habits"]):
                habit_name = data["habits"][int(idx)-1]
                if habit_name in data["history"][today]:
                    data["history"][today].remove(habit_name)
                else:
                    data["history"][today].append(habit_name)
                save_data(data)

        elif choice == "2":
            new_habit = input("Enter the habit you want to track: ")
            if new_habit not in data["habits"]:
                data["habits"].append(new_habit)
                save_data(data)

        elif choice == "3":
            total = len(data["habits"])
            done = len(data["history"][today])
            percent = (done / total * 100) if total > 0 else 0
            print(f"\nDaily Completion: {percent:.1f}%")
            if percent == 100:
                print("🏆 BOSS LEVEL CLEARED!")

        elif choice == "4":
            break

if __name__ == "__main__":
    main()