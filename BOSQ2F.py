# Importing necessary libraries
from collections import deque

# Function for FCFS Scheduling
def fcfs_scheduling(processes):
    n = len(processes)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    gantt_chart = []

    # Sorting processes by arrival time
    processes.sort(key=lambda x: x[1])

    # Calculating Completion Time
    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i][1] + processes[i][2]
        else:
            if completion_time[i - 1] < processes[i][1]:
                completion_time[i] = processes[i][1] + processes[i][2]
            else:
                completion_time[i] = completion_time[i - 1] + processes[i][2]
        gantt_chart.append((processes[i][0], completion_time[i] - processes[i][2], completion_time[i]))

    # Calculating Turnaround Time and Waiting Time
    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]

    return gantt_chart, turnaround_time, waiting_time


# Function for SJN Scheduling
def sjn_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time, then burst time
    completed = 0
    time = 0
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt_chart = []
    visited = [False] * n

    while completed < n:
        # Find the next process with the shortest job and has arrived
        idx = -1
        shortest_burst = float('inf')
        for i in range(n):
            if not visited[i] and processes[i][1] <= time and processes[i][2] < shortest_burst:
                shortest_burst = processes[i][2]
                idx = i

        if idx == -1:  # No process is ready, advance time
            time += 1
        else:
            # Execute the process
            visited[idx] = True
            start_time = time
            time += processes[idx][2]
            completion_time[idx] = time
            gantt_chart.append((processes[idx][0], start_time, time))
            turnaround_time[idx] = completion_time[idx] - processes[idx][1]
            waiting_time[idx] = turnaround_time[idx] - processes[idx][2]
            completed += 1

    return gantt_chart, turnaround_time, waiting_time


# Function for Round Robin Scheduling
def rr_scheduling(processes, quantum):
    n = len(processes)
    processes = [[*process] for process in processes]  # Create a mutable copy
    time = 0
    queue = deque()
    gantt_chart = []
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_burst = [p[2] for p in processes]
    completion_time = [0] * n

    # Enqueue processes as they arrive
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    idx = 0
    while idx < n or queue:
        while idx < n and processes[idx][1] <= time:
            queue.append(processes[idx])
            idx += 1

        if queue:
            current_process = queue.popleft()
            process_id = current_process[0]
            arrival_time = current_process[1]
            burst_time = current_process[2]
            executed_time = min(quantum, remaining_burst[process_id - 1])

            start_time = time
            time += executed_time
            remaining_burst[process_id - 1] -= executed_time

            # Record the Gantt chart entry
            gantt_chart.append((process_id, start_time, time))

            if remaining_burst[process_id - 1] == 0:
                completion_time[process_id - 1] = time
                turnaround_time[process_id - 1] = completion_time[process_id - 1] - arrival_time
                waiting_time[process_id - 1] = turnaround_time[process_id - 1] - burst_time
            else:
                # Re-enqueue the process if it's not finished
                queue.append(current_process)
        else:
            time += 1

    return gantt_chart, turnaround_time, waiting_time

# Helper function to display results
def display_results(gantt_chart, turnaround_time, waiting_time):
    print("\nGantt Chart:")
    for process in gantt_chart:
        print(f"P{process[0]} [{process[1]}-{process[2]}]", end="  ")
    print("\n\nProcess\tTurnaround Time\tWaiting Time")
    for i in range(len(turnaround_time)):
        print(f"P{i + 1}\t{turnaround_time[i]}\t\t{waiting_time[i]}")

    avg_tat = sum(turnaround_time) / len(turnaround_time)
    avg_wt = sum(waiting_time) / len(waiting_time)
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")


# Main Program
if __name__ == "__main__":
    print("Choose a scheduling algorithm: ")
    print("1. FCFS (First Come First Served)")
    print("2. SJN (Shortest Job Next)")
    print("3. RR (Round Robin)")

    choice = int(input("Enter your choice (1/2/3): "))
    n = int(input("Enter the number of processes: "))
    processes = []

    for i in range(1, n + 1):
        arrival_time = int(input(f"Enter arrival time for process P{i}: "))
        burst_time = int(input(f"Enter burst time for process P{i}: "))
        processes.append([i, arrival_time, burst_time])

    if choice == 1:
        gantt_chart, tat, wt = fcfs_scheduling(processes)
    elif choice == 2:
        gantt_chart, tat, wt = sjn_scheduling(processes)
    elif choice == 3:
        quantum = int(input("Enter time quantum: "))
        gantt_chart, tat, wt = rr_scheduling(processes, quantum)
    else:
        print("Invalid choice!")
        exit()

    display_results(gantt_chart, tat, wt)
