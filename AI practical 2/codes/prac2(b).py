# Implement the Recursive Best-First Search algorithm for the same problem.

import queue as Q 
from RMP import dict_gn 
from RMP import dict_hn 

start = 'Arad' 
goal = 'Bucharest' 
result = '' 

def get_fn(citystr): 
    cities = citystr.split(",") 
    hn = gn = 0 
    for ctr in range(0, len(cities)-1):
        gn = gn+dict_gn[cities[ctr]][cities[ctr+1]]
    hn = dict_hn[cities[len(cities)-1]]
    return(hn+gn) 

def printout(cityq): 
    for i in range(0, cityq.qsize()):
        print(cityq.queue[i]) 

def expand(cityq): 
    global result  
    tot, citystr, thiscity = cityq.get()
    nexttot = 999 
    if not cityq.empty(): 
        nexttot,nextcitystr,nextthiscity=cityq.queue[0]
    if thiscity == goal and tot < nexttot:
        result = citystr + "::" + str(tot) 
        return 
    print("\nExpaded city ---------", thiscity) 
    print("second best f(n)---------", nexttot) 
    tempq = Q.PriorityQueue() 
    for cty in dict_gn[thiscity]: 
        tempq.put((get_fn(citystr+','+cty), citystr+','+cty, cty)) 
    for ctr in range(1,3): 
        ctrtot, ctrcitystr ,ctrthiscity = tempq.get() 
        if ctrtot < nexttot: 
            cityq.put((ctrtot, ctrcitystr,ctrthiscity)) 
        else:  
            cityq.put((ctrtot, citystr, thiscity)) 
            break 
    printout(cityq) 
    expand(cityq) 
 
def main(): 
    cityq=Q.PriorityQueue() 
    thiscity=start 
    cityq.put((999, "NA", "NA")) 
    cityq.put((get_fn(start), start, thiscity)) 
    expand(cityq) 
    print("\n", result) 

main() 

'''In summary, A* is typically faster but memory-intensive, whereas RBFS sacrifices speed for better memory efficiency.'''