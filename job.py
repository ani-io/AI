# Define the Job class
class Job:
    def __init__(self, id, deadline, profit):
        self.id = id             # Unique identifier for the job
        self.deadline = deadline # Deadline by which the job should be completed
        self.profit = profit     # Profit if the job is completed on or before its deadline

# Job Scheduling Function
def job_scheduling(jobs):
    # Step 1: Sort the jobs based on profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Find the maximum deadline to know how many slots are needed
    n = max(job.deadline for job in jobs)

    # Step 3: Create an array of slots to keep track of assigned jobs (-1 means slot is free)
    result = [-1] * n

    # Step 4: Initialize total profit
    total_profit = 0

    # Step 5: Try to schedule each job in the latest available slot before its deadline
    for job in jobs:
        # Try from job.deadline - 1 down to 0
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if result[j] == -1:
                result[j] = job.id  # Assign the job to this slot
                total_profit += job.profit
                break  # Move to the next job once scheduled

    # Step 6: Print the results
    print("Scheduled Jobs:", [job_id for job_id in result if job_id != -1])
    print("Total Profit:", total_profit)

# Sample Input: List of jobs
jobs = [
    Job(1, 5, 100),
    Job(2, 4, 50),
    Job(3, 2, 60)
]

# Run the scheduling
job_scheduling(jobs)

# another sample input
# jobs = [
#     Job(1, 4, 20),
#     Job(2, 1, 10),
#     Job(3, 1, 40),
#     Job(4, 1, 30)
# ]
# Scheduled Jobs: [3, 1]
# Total Profit: 60

