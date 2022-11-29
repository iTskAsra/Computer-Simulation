import numpy as np

class customer:
    def __init__(self, time, processing_time=0, start_time=0, done_at=0) -> None:
        self.time = time
        self.done_at=done_at
        self.start_time = start_time
        if processing_time>0:
            self.processing_time = processing_time
        else:
            self.processing_time = 0.01

    def __repr__(self) -> str:
        return f"{self.time} and {self.processing_time} and {self.start_time}\n"

mean = 4
standard_deviation = 9
max_timer = 0


customers = [customer(0, np.random.normal(mean,standard_deviation))]

for i in range(1, 12):
    t = 0
    random = np.random.rand()
    if random >= 0.39 and random < 0.72:
        t = 1
    elif random >= 0.72 and random < 0.91:
        t = 2
    elif random >= 0.91:
        t = 3

    max_timer += t
    customers.append(customer(max_timer, np.random.normal(mean,standard_deviation)))

timer = 0
server_queue = [customers[0]]
customer_index = 0
server1 = []
server2 = []
queue = []
server1_busy = 0
server2_busy = 0
new_customer = False
max_timer = 10000
done_tasks = []
for tick in range(max_timer+1):
    
    while customer_index<12 and customers[customer_index].time <= tick: 
        new_customer = True
        queue.append(customers[customer_index])
        is_busy = False
        if customer_index < 11:
            customer_object = customers[customer_index+1]
        if server1 or server2:
            is_busy = True
        if queue:
            customer_object = queue[0]
        print(f'Time is: {tick}, server status is {is_busy}, next task will arrive at {customer_object.time} and the task at hand will end at: {customers[customer_index].processing_time+customers[customer_index].processing_time}')
        customer_index += 1
        

    if server1:
        server1_busy += 1
        if server1[0].start_time+server1[0].processing_time <= tick:
            server1.pop()
    
    if server2:
        server2_busy += 1
        if server2[0].start_time+server2[0].processing_time <= tick:
            server2.pop()


    if not server1:
        if queue:
            server1.append(queue[0])
            server1[0].start_time = tick
            queue.pop(0)
    elif not server2:
        if queue:
            server2.append(queue[0])
            server1[0].start_time = tick
            queue.pop(0)
    
    
    
    if not server1 and not server2 and not queue:
        max_timer = tick
        break

    


    
        

print(f'server1 has been busy {100*server1_busy/max_timer}%\nserver2 has been busy {100*server2_busy/max_timer}%')