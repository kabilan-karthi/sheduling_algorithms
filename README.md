# sheduling_algorithms
This Streamlit app is designed to help users visualize various operating system (OS) scheduling algorithms, such as First-Come, First-Served (FCFS), Shortest Job First (SJF), and Round Robin. 
This Streamlit app is designed to help users visualize various operating system (OS) scheduling algorithms, such as First-Come, First-Served (FCFS), Shortest Job First (SJF), and Round Robin. The app provides an interactive interface where users can input details for multiple processes, such as their arrival and burst times, and then see how these processes are scheduled according to the selected algorithm.

## Features
- **Algorithm Selection**: Users can choose from different scheduling algorithms using a sidebar dropdown menu.
- **Process Input**: The sidebar allows users to specify the number of processes and input details for each process, including arrival and burst times.
- **Scheduling Execution**: On clicking the "Schedule" button, the selected scheduling algorithm is executed, and the results are displayed.
- **Gantt Chart Visualization**: A Gantt chart is generated to visually represent the scheduling of processes over time.
- **Summary Metrics**: The app calculates and displays key performance metrics, such as average turnaround time and average waiting time.

## Usage
1. **Select Algorithm**: Use the sidebar to select an algorithm (e.g., FCFS).
2. **Input Process Details**: Specify the number of processes. For each process, enter its arrival time and burst time.
3. **Execute Scheduling**: Click the "Schedule" button to perform the scheduling.
4. **View Results**: The app displays a Gantt chart of the scheduling and shows a dataframe with detailed process information, including start time, completion time, turnaround time, and waiting time.
5. **Review Metrics**: Check the average turnaround time and waiting time for an overall performance summary.

## Implementation Details
- **FCFS Scheduling**: The provided code includes the implementation of the FCFS scheduling algorithm, which processes tasks in the order they arrive.
- **Interactive Sidebar**: The sidebar is used to gather user inputs and initiate the scheduling process.
- **Data Visualization**: Plotly is used to create an interactive Gantt chart that helps users understand the scheduling sequence.
- **Styling**: Custom CSS is applied to improve the app's visual appearance, ensuring a clean and user-friendly interface.

By using this app, users can gain a better understanding of how different OS scheduling algorithms work and compare their performance using various metrics. This educational tool is ideal for students, educators, and professionals interested in learning about process scheduling in operating systems.
