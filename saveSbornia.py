import json
cont = 0
def get_full_data():
    with open('logNaveSbornia.txt', 'rb') as meu_json:
        return json.loads(meu_json.read())

def get_logs_of_month():
    vetor = [[], [], [], [], [], [], [], [], [], [], [], []]
    for i in get_full_data():
        infos = {
            'user': i['user'],
            'log': i['log']
        }

        if i['month'] == 'January':
            vetor[0].append(infos)
        elif i['month'] == 'February':
            vetor[1].append(infos)
        elif i['month'] == 'March':
            vetor[2].append(infos)
        elif i['month'] == 'April':
            vetor[3].append(infos)
        elif i['month'] == 'May':
            vetor[4].append(infos)
        elif i['month'] == 'June':
            vetor[5].append(infos)
        elif i['month'] == 'July':
            vetor[6].append(infos)
        elif i['month'] == 'August':
            vetor[7].append(infos)
        elif i['month'] == 'September':
            vetor[8].append(infos)
        elif i['month'] == 'October':
            vetor[9].append(infos)
        elif i['month'] == 'November':
            vetor[10].append(infos)
        elif i['month'] == 'December':
            vetor[11].append(infos)
    global cont
    mes_atual=0
    for i in vetor:
        cont += len(i)
        print(str(cont) + ' - '+str(mes_atual))
        if(cont > 1000001):
            return vetor[mes_atual]
        mes_atual+=1

def get_biggest_value(logs_to_order):
    biggest = 0
    for i in logs_to_order:
        if i.get('log') > biggest:
            biggest = i.get('log')
    return biggest

def countingSort(inputArray, maxElement):

    countArrayLength = maxElement+1

    # Initialize the countArray with (max+1) zeros
    countArray = [0] * countArrayLength

    # Step 1 -> Traverse the inputArray and increase
    # the corresponding count for every element by 1
    for el in inputArray:
        countArray[el.get('log')] += 1

    # Step 2 -> For each element in the countArray,
    # sum up its value with the value of the previous
    # element, and then store that value
    # as the value of the current element
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1]

    # Step 3 -> Calculate element position
    # based on the countArray values
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i].get('log')
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray

logs_to_order = get_logs_of_month()

orderedLogs = countingSort(logs_to_order, get_biggest_value(logs_to_order))

index_guilted = (1000001 - (cont - len(orderedLogs)))

log_guilted = orderedLogs[index_guilted]

for i in get_logs_of_month():
    if i.get('log') == log_guilted:
        print(i.get('user'))