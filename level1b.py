import json
f = open('Z:/MOCK-HCK/level1b.json')
data = json.load(f)

check  = [i for i in range(0,50)]
print(check)

visited= []
Paths = []
capacity  = data['vehicles']['v0']['capacity']
backup = capacity
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
    load= 0
   # print(lst)
    for v in data['neighbourhoods'][curr]['distances']:
        if c not in lst and v < dist and v!=0 :
          #  print(lst)
            dist =v
            node=c
            load  = data['neighbourhoods']['n'+str(c)]['order_quantity']
        c+=1

    return node,load
def Algo() :
    visited= []
    capacity =600
    amt= 0
    lst  = []
    while True  :
        if list(set(lst))==check :
            break
        start = giveNextMinNode('r0',lst)
        visited= []
        while True:  
            if list(set(lst))==check  :
                r = ['r0']
                for i in visited :
                    if i!=0 :
                      r.append('n'+str(i))
                r.append('r0')
                Paths.append(r)
                break
            for i in visited :
                lst.append(i)
            lst = list(set(lst))
            temp,amt = giveNextNeighbor('n'+str(start),lst)
            #print(temp,amt)
            if capacity >= amt:
                capacity-= amt 
                start  = temp
                visited.append(start)
            else :
                capacity = backup
                r = ['r0']
                for i in visited :
                    lst.append(i)
                    r.append('n'+str(i))
                lst = list(set(lst))
                r.append('r0')
                Paths.append(r)
                break
       # print(lst)
   # print(Paths)
    dicts= {}
    c=1
    for i in Paths  :
        k = "path"+str(c)
        c+=1
        dicts[k] = i
    result = {'v0': dicts}
    with open('Z:/MOCK-HCK/level1b_output.json', 'w') as result_file:
        json.dump(result, result_file)
Algo()