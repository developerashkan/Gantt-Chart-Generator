# CLI Gantt Chart Generator

A lightweight, terminal-based tool that instantly converts text-based task lists into visual Gantt charts using Python and Matplotlib.

## Features

* **Instant Visualization:** Paste a list of tasks and generate a chart immediately.
* **Smart Sorting:** Automatically arranges tasks chronologically (earliest start date at the top).
* **Duration Labels:** Automatically calculates days and displays them next to the bars (e.g., **10d**).
* **Validation:** Robust error handling that tells you exactly which line is formatted incorrectly.
* **Micro-Task Support:** Tasks starting and ending on the same day are rendered as 1-day blocks (instead of invisible lines).



## Prerequisites

You need Python installed. This script relies on the `matplotlib` library.

To install the required library, run:

```bash
pip install matplotlib
```
## How to Run
Save the code as gantt_chart.py.

Run the script in your terminal:

```bash
python gantt_chart.py
```

## Usage
When the script runs, it will ask for input. You can paste a single task or a long list of tasks separated by semicolons.

The Input Format
Task Name, Start Date, End Date; Next Task, Start Date, End Date

Dates: Must be YYYY-MM-DD.

Separator: Use a semicolon ; between distinct tasks.

Execution: Paste the text and hit ENTER once.

Example Input
Copy and paste this block into the terminal:

```bash
Project Kickoff, 2026-05-01, 2026-05-01; UI Design, 2026-05-02, 2026-05-12; Backend Coding, 2026-05-10, 2026-05-25
```

## Error Handling
The script includes strict validation. If you paste incorrect data, it will skip the bad entry and tell you why:

❌ ERROR: ... missing commas: You didn't provide 3 fields (Name, Start, End).

❌ ERROR: ... is not YYYY-MM-DD: You used the wrong date format (e.g., 05-01-2026).

❌ ERROR: ... ends before it starts: You set the End Date earlier than the Start Date.

## Logic details
Sorting: The script uses reverse=True sorting so that when Matplotlib plots from the bottom (0,0) up, the earliest task appears visually at the top of the chart.

Duration Calculation: (End - Start) + 1. This ensures a task that starts/ends on the same day counts as 1 day of work.

## License
MIT
