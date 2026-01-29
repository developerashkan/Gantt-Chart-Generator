import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def generate_gantt():
    tasks = []

    print("--- Gantt Chart Generator (Single-Paste Mode) ---")
    print("Format: Task Name, YYYY-MM-DD, YYYY-MM-DD")
    print("Separate multiple tasks with a semicolon ';'")
    print("-" * 50)
    
    # Get input once and process immediately
    raw_input = input("Paste tasks here and press ENTER: ").strip()

    if not raw_input:
        print("❌ No input detected.")
        return

    # Split tasks by semicolon
    entries = [e.strip() for e in raw_input.split(";") if e.strip()]

    for entry in entries:
        try:
            parts = [p.strip() for p in entry.split(",")]
            
            # Validation 1: Field Count
            if len(parts) != 3:
                print(f"❌ ERROR: '{entry}' is missing commas or dates.")
                continue
                
            name, start_str, end_str = parts
            
            # Validation 2: Date Formats
            try:
                start_date = datetime.strptime(start_str, "%Y-%m-%d")
            except ValueError:
                print(f"❌ ERROR: Start date '{start_str}' in '{name}' must be YYYY-MM-DD.")
                continue
                
            try:
                end_date = datetime.strptime(end_str, "%Y-%m-%d")
            except ValueError:
                print(f"❌ ERROR: End date '{end_str}' in '{name}' must be YYYY-MM-DD.")
                continue

            # Validation 3: Logic
            if end_date < start_date:
                print(f"❌ ERROR: Task '{name}' ends before it starts ({end_str} < {start_str}).")
                continue
            
            tasks.append((name, start_date, end_date))
                
        except Exception as e:
            print(f"❌ UNEXPECTED ERROR: {e}")

    if not tasks:
        print("\nNo valid tasks found. Chart generation aborted.")
        return

    # Sort tasks: Earliest at the top
    tasks.sort(key=lambda x: x[1], reverse=True)

    task_names = [t[0] for t in tasks]
    start_dates = [t[1] for t in tasks]
    # +1 ensures same-day tasks are visible as 1-day bars
    durations = [(t[2] - t[1]).days + 1 for t in tasks]

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(task_names, durations, left=start_dates, color='#3498db', edgecolor='black', height=0.6)

    # Formatting X-axis (Dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    
    plt.xticks(rotation=45)
    plt.title("Project Schedule Overview", pad=20, fontsize=14, fontweight='bold')
    plt.xlabel("Date", fontsize=11)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    
    # Add day-count labels to bars
    for i, bar in enumerate(bars):
        ax.text(bar.get_x() + bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, 
                f'{durations[i]}d', va='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    print("\n✅ Rendering chart...")
    plt.show()

if __name__ == "__main__":
    generate_gantt()
