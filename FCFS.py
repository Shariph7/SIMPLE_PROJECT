# Function to find the waiting 
# time for all processes
def findWaitingTime(n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

# Function to calculate turn
# around time
def findTurnAroundTime(n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

# Function to calculate
# average time
def findavgTime(n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    findWaitingTime(n, bt, wt)
    findTurnAroundTime(n, bt, wt, tat)

    print("Processes Burst time Waiting time Turn around time")
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"{i + 1}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"Average waiting time = {total_wt / n}")
    print(f"Average turn around time = {total_tat / n}")

# Driver code
if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    burst_time = []

    for i in range(n):
        bt = int(input(f"Enter burst time for process {i + 1}: "))
        burst_time.append(bt)

    findavgTime(n, burst_time)
