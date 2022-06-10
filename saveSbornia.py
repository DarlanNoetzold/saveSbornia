import json
import time
from functools import reduce


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

def selectonSort(inputArray, n):
    for i in range(0,n):
        less = i
        for j in range(i+1,n):
            if(inputArray[j].get('log') < inputArray[less].get('log')):
                less=j
            j = j+1
        aux = inputArray[i]
        inputArray[i] = inputArray[less]
        inputArray[less]=aux
    return inputArray

def countingSortStable(inputArray, maxElement):
    countArrayLength = maxElement+1
    countArray = [0] * countArrayLength

    for el in inputArray:
        countArray[el.get('log')] += 1

    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1]

    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i].get('log')
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray

def countingSort(inputArray, maxElement):
    countArrayLength = maxElement+1
    countArray = [0] * countArrayLength

    for el in inputArray:
        countArray[el.get('log')] += 1

    inputArray = []
    for i in countArray:
        while i >= 1:
            inputArray.append(i);
            i -= 1

    return inputArray


def radixSort(A):
    m = 0
    for item in A:
        m = max(m, item.get('log'))
    num_digits = len(str(m))

    for digit in range(0, num_digits):
        B = [[] for i in range(10)]
        for item in A:
            # num is the bucket number that the item will be put into
            num = item.get('log') // 10 ** (digit) % 10
            B[num].append(item.get('log'))
        A = reduce(lambda x, y: x + y, B)
    return A

def quickSort(A, start, end):
    qs_array = A

    def _partitionate(qs_array, p, r):
        pivot = qs_array[r]
        i = p - 1
        for j in range(p, r):
            if qs_array[j].get('log') <= pivot.get('log'):
                i = 1 + i
                aux = qs_array[i]
                qs_array[i] = qs_array[j]
                qs_array[j] = aux
        i = i + 1
        aux = qs_array[i]
        qs_array[i] = qs_array[r]
        qs_array[r] = aux
        return i

    def _quickSort(qs_array, start, end):
        if start <= end:
            partition = _partitionate(qs_array, start, end)
            _quickSort(qs_array, start, partition - 1)
            _quickSort(qs_array, partition + 1, end)
    
    _quickSort(qs_array, start, end)
    return qs_array
    


if __name__ == "__main__":
    print("Qual algoritmo de ordenacao você deseja usar?")
    print("1 - Counting Sort")
    print("2 - Selection Sort")
    print("3 - Counting Sort Stable")
    print("4 - Radix Sort in dev")
    print("5 - Quick Sort")
    option = input()

    logs_to_order = get_logs_of_month()

    if option == "1":
        start = time.time()
        orderedLogs = countingSort(logs_to_order, get_biggest_value(logs_to_order))
        end = time.time()
        print("Tempo de execução: " + str(end - start))

        index_guilted = (1000001 - (cont - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        for i in get_logs_of_month():
            if i.get('log') == log_guilted:
                print('Culpado: ', i.get('user'))
                
    elif option == "2":
        start = time.time()
        orderedLogs = selectonSort(logs_to_order, len(logs_to_order))
        end = time.time()
        print("Tempo de execução: " + str(end - start))

    elif option == "3":
        start = time.time()
        orderedLogs = countingSortStable(logs_to_order, get_biggest_value(logs_to_order))
        end = time.time()
        print("Tempo de execução: " + str(end - start))

        index_guilted = (1000001 - (cont - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        for i in get_logs_of_month():
            if i.get('log') == log_guilted:
                print('Culpado: ', i.get('user'))

    elif option == "4":
        start = time.time()
        orderedLogs = radixSort(logs_to_order)
        end = time.time()
        print("Tempo de execução: " + str(end - start))

    elif option == "5":
        start = time.time()
        orderedLogs = quickSort(logs_to_order, 0, len(logs_to_order) - 1)
        end = time.time()
        print("Tempo de execução: " + str(end - start))

        index_guilted = (1000001 - (cont - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        print('Culpado: ', log_guilted.get('user'))

    else:
        print('Opção inválida!')