import heapq
jobs = []
n=int(input("Enter number of elements :" ))
for i in range(n):
      job=input("Enter Job : ")
      prior=int(input(f"Enter Priority of job {job} : "))
      heapq.heappush(jobs,(prior,job))
print("Jobs in heap order")
for priority, job in jobs:
    print("Processing : ",job,"Priority : ", -priority)
print("\nHighest priority job : ",jobs[0][1])
print("Priority : ", -jobs[0][0])
priority,job = heapq.heappop(jobs)
print("\nProcessed job : ",job)
print("Priority : ", -priority)
print("\nRemaining jobs : ")
for priority, job in jobs:
    print(job,"Priority : ", -priority)
