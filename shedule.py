import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Function to simulate FCFS scheduling
def fcfs_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x['arrival_time'])
    current_time = 0
    for i in range(n):
        if current_time < processes[i]['arrival_time']:
            current_time = processes[i]['arrival_time']
        processes[i]['start_time'] = current_time
        current_time += processes[i]['burst_time']
        processes[i]['completion_time'] = current_time
        processes[i]['turnaround_time'] = processes[i]['completion_time'] - processes[i]['arrival_time']
        processes[i]['waiting_time'] = processes[i]['turnaround_time'] - processes[i]['burst_time']
    return processes

# Sidebar for user inputs
st.sidebar.header('Scheduling Algorithm')
algorithm = st.sidebar.selectbox('Select Algorithm', ('FCFS', 'SJF', 'Round Robin'))

st.sidebar.header('Process Details')
process_count = st.sidebar.number_input('Number of processes', min_value=1, max_value=10, value=3)

processes = []
for i in range(process_count):
    st.sidebar.subheader(f'Process {i+1}')
    arrival_time = st.sidebar.number_input(f'Arrival Time P{i+1}', min_value=0, max_value=100, value=0)
    burst_time = st.sidebar.number_input(f'Burst Time P{i+1}', min_value=1, max_value=100, value=1)
    processes.append({
        'pid': f'P{i+1}',
        'arrival_time': arrival_time,
        'burst_time': burst_time,
        'start_time': 0,
        'completion_time': 0,
        'turnaround_time': 0,
        'waiting_time': 0,
    })

if st.sidebar.button('Schedule'):
    if algorithm == 'FCFS':
        scheduled_processes = fcfs_scheduling(processes)
    # Implement other scheduling algorithms here (SJF, Round Robin, etc.)

    st.subheader(f'{algorithm} Scheduling')
    df = pd.DataFrame(scheduled_processes)
    st.dataframe(df)

    # Plotting Gantt Chart
    fig = go.Figure()
    for process in scheduled_processes:
        fig.add_trace(go.Bar(
            x=[process['burst_time']],
            y=[process['pid']],
            orientation='h',
            text=f"Start: {process['start_time']}<br>End: {process['completion_time']}",
            hoverinfo="text",
            marker=dict(color=px.colors.qualitative.Plotly[processes.index(process)])
        ))

    fig.update_layout(
        title='Gantt Chart',
        xaxis_title='Time',
        yaxis_title='Processes',
        bargap=0.2,
        height=400
    )

    st.plotly_chart(fig)

    # Display summary metrics
    st.subheader('Summary Metrics')
    avg_turnaround_time = df['turnaround_time'].mean()
    avg_waiting_time = df['waiting_time'].mean()

    st.write(f'**Average Turnaround Time:** {avg_turnaround_time}')
    st.write(f'**Average Waiting Time:** {avg_waiting_time}')

st.markdown("""
<style>
    .css-18e3th9 {
        padding: 2rem 1rem 2rem 1rem;
        background-color: #f0f2f6;
    }
    .css-1aumxhk {
        padding: 1rem;
    }
    .css-15zrgzn {
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title('OS Scheduling Algorithms')
st.write("""
This Streamlit app allows you to visualize various OS scheduling algorithms like FCFS, SJF, and Round Robin.
Use the sidebar to select the algorithm and input process details.
""")
