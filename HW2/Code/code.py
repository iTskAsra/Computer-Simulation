import numpy as np

class customer:
    def __init__(self, time, processing_time=0) -> None:
        self.time = time
        if processing_time>0:
            self.processing_time = processing_time
        else:
            self.processing_time = 0


mean = 4
standard_deviation = 9
timer = 0


customers = [customer(timer, np.random.normal(mean,standard_deviation))]

for i in range(1, 11):
    t = 0
    random = np.random.rand()
    if random >= 0.39 and random < 0.72:
        t = 1
    elif random >= 0.72 and random < 0.91:
        t = 2
    elif random >= 0.91:
        t = 3

    customers.append(customer(t, np.random.normal(mean,standard_deviation)))

print(customers)