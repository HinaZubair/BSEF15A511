process = []

total_waiting_time = 0

number = int(input('Enter no of processes: '))

for i in range(number):

    process.append([])

    process[i].append(input('Enter process name: '))

    process[i].append(int(input('Enter parrival time: ')))

    total_waiting_time += process[i][1]
    process[i].append(int(input('Enter p_burst time: ')))

process.sort(key = lambda process:process[0])


print ('Process_Name\tArrival_Time\tBurst_Time')

for i in range(number):
    
    print process[i][0],  '\t\t', process[i][1],  '\t\t',  process[i][2]
    

print ('Total_waiting_time: ')
print(total_waiting_time)

print ('Average_waiting_time: ')
print(total_waiting_time/number)

