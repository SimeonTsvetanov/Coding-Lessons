class Job:
    def __init__(self, value, index, target=False):
        self.value = value
        self.index = index
        self.target = target


jobs_input = [int(job) for job in input().split(", ")]
i_target = int(input())
jobs = []

for i in range(len(jobs_input)):
    job_value = jobs_input[i]
    job_index = i
    job_target = False
    if i == i_target:
        job_target = True
    jobs.append(Job(job_value, job_index, job_target))

jobs = sorted(jobs, key=lambda x: x.value)
clock = 0

for job in jobs:
    clock += job.value
    if job.index == i_target:
        break

print(clock)
