import math

def generate(seed, m, a, c, count):
    results = []
    current = seed
    for i in range(count):
        current = (a*current + c)%m
        results.append(current/m)
    
    return results


g1 = generate(13,100,23,43,100)
g2 = generate(17,99,27,47,100)

final = []
for i in range(100):
    final.append(abs(abs(g1[i]-g2[i])%100-1))

final_alt = [ '%.3f' % elem for elem in final ]
print(final_alt)

d = 0.294
dlist = []
final.sort()
for i in range(20):
    dlist.append((i+1)/20-final[i])
    dlist.append(final[i]-i/20)

dmax = max(dlist)
#Here D- and D+ are in the same list as dlist which simplifies calculations
print(f'D is {dmax} and D-alpha is {d}, thus H0 is {dmax<=d}')

#chi square
x_alpha = 30.1
observations = []
index = 0
interval = 0.05
counter = 0

while interval<=1:
    if final[index]<interval:
        counter+=1
        index +=1
    else:
        interval+=0.05
        observations.append(counter)
        counter = 0

x = 0
for observation in observations:
    x += pow(5-observation,2)/5

print(f'X is {x} and X-alpha is {x_alpha}, thus H0 is {x<=x_alpha}')

large_m = 12
sigma = math.sqrt(13*large_m+7)/(12*(large_m+1))
ro = 0
i = 3
m = 7
for k in range(large_m+1):
    ro += final[i+k*m]*final[i+(k+1)*m]

ro /= large_m+1
ro -= 0.25
print(f'Z0 with i=3 is {ro/sigma}')
print(f'ro is {ro} and sigma is {sigma} thus hypothesis is {abs(ro/sigma)<=0.97778}')


ro = 0
i = 7
for k in range(large_m+1):
    ro += final[i+k*m]*final[i+(k+1)*m]

ro /= large_m+1
ro -= 0.25
print(f'Z0  with i=7 is {ro/sigma}')
print(f'ro is {ro} and sigma is {sigma} thus hypothesis is {abs(ro/sigma)<=0.97778}')