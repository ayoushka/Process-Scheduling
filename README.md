#  Process-Scheduling

This project implements three different process Scheduling algorithms: First Come Fist Served (FCFS), Shortest Job Next (SJN), and Round Robin (RR).This code calculates completion time for each process and generates a Gantt chart to visualize the Scheduling order.

## Table of contents
-[Introduction](#introduction)
-[Features](#features)
-[Installation](#installation)
-[Usage](#usage)
-[Examples](#examples)
-[Contributing](#contributing)
-[License](#license)

##Introduction
Process Scheduling is a critical aspect of operating systems that determines the order in which processes are executed.This project demonstrates the implementation of three common Scheduling algorithms and provides insights into their performance.

##Features
-**FCFS (First Come First Served)**: processes are Scheduling in the order of    their arrival times.
-**SJN (Shortest Job Next)**: processes with the Shortest burst times are Scheduled First.
-**RR (Round Robin)**:processes are Scheduled in a cyclic order based on a fixed time quantum.

##Installation
To run this project, ensure you have python installed on your system. You can download python from [python.org](https://www.python.org/downloads/).

Clone this repository:
```bash
git clone https://github.com/ayoushka/Process-Scheduling.git
cd Process-Scheduling

##Usage
Bash
python main.python

##Examples
**FCFS (First Come First Served)**
Choose a Scheduling algorithm:
1. FCFS (First Come First Served)
2. SJN (Shirtest Job Next)
3. RR (Round Robin)
Enter your choice (1/2/3): 1
Enter the number of processes: 3
Enter arrival time for process P1: 0
Enter burst time for process P1: 5
Enter arrival time for process P2: 1
Enter burst time for process P2: 3
Enter arrival time for Process P3: 2
Enter burst time for process P3: 8

**SJN (Shortest Job Next)**
Choose a Scheduling algorithm:
1. FCFS (First Come First Served)
2. SJN (Shirtest Job Next)
3. RR (Round Robin)
Enter your choice (1/2/3): 2
Enter the number of processes: 3
Enter arrival time for process P1: 0
Enter burst time for process P1: 5
Enter arrival time for process P2: 1
Enter burst time for process P2: 3
Enter arrival time for Process P3: 2
Enter burst time for process P3: 8

**RR (Round Robin)**
Choose a Scheduling algorithm:
1. FCFS (First Come First Served)
2. SJN (Shirtest Job Next)
3. RR (Round Robin)
Enter your choice (1/2/3): 3
Enter the number of processes: 3
Enter arrival time for process P1: 0
Enter burst time for process P1: 5
Enter arrival time for process P2: 1
Enter burst time for process P2: 3
Enter arrival time for Process P3: 2
Enter burst time for process P3: 8
Enter time quantum: 2

##Contributing
Feel free to open issues or submit pull requests>

##Licence
This project is licensed under the MIT License.See the LICENSE file for more details.
Feel free to costomize this file to better suit your project and include any additinal information that might be relevant.
 
