import json
f = open('Z:/MOCK-HCK/level0.json')
data = json.load(f)
visited= []

def giveNextMinNode(curr,lst) :
    c = 0  
    dist = 1000000
    node = 0
    for v in data['restaurants'][curr]['neighbourhood_distance']:
        if c not in lst and v < dist :
            dist =v
            node=c
        c+=1
    return node
def giveNextNeighbor(curr,lst) :
    c = 0  
    dist = 1000000
    node = 0
    for v in data['neighbourhoods'][curr]['distances']:
        if c not in lst and v < dist and v!=0 :
            dist =v
            node=c
        c+=1
    return node

def Algo() :
    start = giveNextMinNode('r0',[])
    visited.append(start)
    node="n"
    while True:
         temp = giveNextNeighbor(node+str(start),visited)
         visited.append(temp)
         #print(visited)
         if sorted(visited) == [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19] :
             break
         start = temp
    print("min-cost traversal thro : r0-->",visited,"-->ro")
        # Save the path to a new JSON file
    r = ['r0']
    for i in visited :
        r.append('n'+str(i))
    r.append('r0')
    result = {'v0': {'path': r}}
    with open('Z:/MOCK-HCK/level0_output.json', 'w') as result_file:
        json.dump(result, result_file)
Algo()