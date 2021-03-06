import json
import time
AUX=0
def get_full_data():
    with open('logNaveSbornia.txt', 'rb') as meu_json:
        return json.loads(meu_json.read())

def get_all_data():
    vet = []
    for i in get_full_data():
        infos = {
            'user': i['user'],
            'log': i['log'],
            'month': i['month'],
            'msg': i['msg']
        }
        vet.append(infos)
    return vet

def get_logs_of_month():
    vetor = [[], [], [], [], [], [], [], [], [], [], [], []]
    for i in get_full_data():
        infos = {
            'user': i['user'],
            'log': i['log'],
            'month': i['month'],
            'msg': i['msg']
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
    cont=0
    mes_atual=0
    for i in vetor:
        cont += len(i)
        if(cont > 1000000):
            global AUX
            AUX = cont
            return vetor[mes_atual]
        mes_atual+=1

def get_biggest_value(logs_to_order):
    biggest = 0
    for i in logs_to_order:
        if i.get('log') > biggest:
            biggest = i.get('log')
    return biggest

def selectionSort(inputArray, n):
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

def radixSort(inputArray):
    def _countingSortForRadix(inputLogsCount, placeValue):

        countArray = [0] * 10
        inputSize = len(inputLogsCount)
        for i in range(inputSize):
            placeElement = (inputLogsCount[i] // placeValue) % 10
            countArray[placeElement] += 1

        for i in range(1, 10):
            countArray[i] += countArray[i - 1]

        outputArray = [0] * inputSize
        i = inputSize - 1
        while i >= 0:
            currentEl = inputLogsCount[i]
            placeElement = (inputLogsCount[i] // placeValue) % 10
            countArray[placeElement] -= 1
            newPosition = countArray[placeElement]
            outputArray[newPosition] = currentEl
            i -= 1

        return outputArray

    def _radixSort(inputLogs):
        # Step 1 -> Find the maximum element in the input array
        maxEl = max(inputLogs)

        # Step 2 -> Find the number of digits in the `max` element
        D = 1
        while maxEl > 0:
            maxEl /= 10
            D += 1

        # Step 3 -> Initialize the place value to the least significant place
        placeVal = 1

        # Step 4
        outputArray = inputLogs
        while D > 0:
            outputArray = _countingSortForRadix(outputArray, placeVal)
            placeVal *= 10
            D -= 1

        return outputArray

    inputLogs = []
    for i in inputArray:
        inputLogs.append(i.get('log'))
    return _radixSort(inputLogs)


def countingSortStable(inputArray, maxElement):
    inputLogs = []
    for i in inputArray:
        inputLogs.append(i.get('log'))

    countArrayLength = maxElement+1
    countArray = [0] * countArrayLength

    for el in inputLogs:
        countArray[el] += 1

    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1]

    outputArray = [0] * len(inputLogs)
    i = len(inputLogs) - 1
    while i >= 0:
        currentEl = inputLogs[i]
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
            inputArray.append(i)
            i -= 1

    return inputArray


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
    
def insertionSort(A, n):
    is_array = A

    for i in range(1, n):
        key = is_array[i]
        j = i - 1
        while j > -1 and is_array[j].get('log') > key.get('log'):
            is_array[j + 1] = is_array[j]
            j = j -1
        is_array[j + 1] = key

    return is_array

def mergeSort(A):

    ms_array = A
    aux = [0] * len(A)
    
    def _merge(ms_array, aux, left, middle, right):
        for k in range(left, right + 1):
            aux[k] = ms_array[k]
        i = left
        j = middle + 1

        for k in range(left, right + 1):
            if i > middle:
                ms_array[k] = aux[j]
                j += 1
            elif j > right:
                ms_array[k] = aux[i]
                i += 1
            elif aux[j].get("log") < aux[i].get("log"):
                ms_array[k] = aux[j]
                j += 1
            else:
                ms_array[k] = aux[i]
                i += 1

    def _mergeSort(ms_array, aux, left, right):
        if right <= left:
            return
        middle = (left + right) // 2

        _mergeSort(ms_array, aux, left, middle)
        _mergeSort(ms_array, aux, middle + 1, right)
        _merge(ms_array, aux, left, middle, right)

    _mergeSort(ms_array, aux, 0, len(A) - 1)
    return ms_array

def interpolation_search(array, x):
    low = 0
    array_low = array[low][0].get("log")
    aux = 1
    while True:
        try:
            high = len(array) - aux
            array_high = array[high][0].get("log")
            break
        except Exception:
            aux += 1

    while (low <= high) and (x >= array_low) and (x <= array_high):
        if len(array[low]) == 0 or len(array[high]) == 0: continue
        array_low = array[low][0].get("log")
        array_high = array[high][0].get("log")
        pos = int(low + ((high - low) / (array_high - array_low)) * (x - array_low))
        if len(array[pos]) == 0: continue
        if array[pos][0].get("log") < x:
            low = pos+1

        elif array[pos][0].get("log") > x:
            high = pos-1

        else:
            return array[pos]

    return -1

def busca_binaria(valor, vetor):
    esquerda, direita = 0, len(vetor) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio][0].get("log") == valor:
            return vetor[meio]
        elif vetor[meio][0].get("log") > valor:
            direita = meio - 1
        else:  # A[meio] < item
            esquerda = meio + 1
    return -1

def hash_by_division(input_array):
    print("Criando o hash table...")
    hash_table = [[] for _ in range(104729)]

    def _hashing(keyvalue):
        return keyvalue % len(hash_table)

    def _insert(hash_table, keyvalue, value):
        i = _hashing(keyvalue)
        
        hash_table[i].append(value)
        return i

    for i in input_array:
        _insert(hash_table, i.get("log"), i)

    return hash_table

    

def heapSort(A):
    hs_array = A
    n = len(hs_array)

    def _heapify(hs_array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and hs_array[i].get('log') < hs_array[left].get('log'):
            largest = left

        if right < n and hs_array[largest].get('log') < hs_array[right].get('log'):
            largest = right
        
        if largest != i:
            aux = hs_array[i]
            hs_array[i] = hs_array[largest]
            hs_array[largest] = aux
            _heapify(hs_array, n, largest)

    for i in range( n // 2 - 1, -1, -1):
        _heapify(hs_array, n, i)

    for i in range(n - 1, 0, -1):
        aux = hs_array[i]
        hs_array[i] = hs_array[0]
        hs_array[0] = aux
        _heapify(hs_array, i, 0)
    
    return hs_array

def bubbleSort(A, n):
    change = True

    while(change == True):
        change = False
        for i in range(0, n - 1):
            if A[i].get('log') > A[i + 1].get('log'):
                aux = A[i]
                A[i] = A[i + 1]
                A[i + 1] = aux
                change = True

def display_hash(hash_table):
    if hash_table == -1:
        print("Valor n??o existe!")
        return
    for i in hash_table:
        print(i.get('user'), end=" ")
        print("-->", end=" ")
        print(i, end=" ")

        print()

def normalize_data(hash_table):
    for i in hash_table:
        if len(i) == 0:
            hash_table.remove(i)

    return hash_table


if __name__ == "__main__":
    vet_aux = []
    print("Lendo os logs da nave...")
    logs_to_order = get_logs_of_month()
    print("Leitura finalizada.")
    print("Qual algoritmo de ordena????o voc?? deseja usar?")
    print("--- N??o usam compara????o ---")
    print("1 - Counting Sort (Stable)")
    print("2 - Counting Sort")
    print("3 - Radix Sort")
    print("--- Usam compara????o ---")
    print("4 - Quick Sort")
    print("5 - Merge Sort")
    print("6 - Heap Sort")
    print("7 - Insertion Sort")
    print("8 - Selection Sort")
    print("9 - Bubble Sort (Iterative)")
    print("--- Buscas Todos Dados---")
    print("10 - Busca Bin??ria")
    print("11 - Busca por Intepola????o")
    print("--- Buscas Dados de Um Mes ---")
    print("12 - Busca Bin??ria")
    print("13 - Busca por Intepola????o")

    option = input()
    if option == "1":
        print("Ordenando os logs. Tempo estimado: 0.25s")
        start = time.time()
        orderedLogs = countingSortStable(logs_to_order, get_biggest_value(logs_to_order))
        end = time.time()
        print("Logs ordenados. Tempo de execu????o: " + str(end - start))
        print("Encontrando o(s) impostor(es)...")

        index_guilted = (1000000 - (AUX - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        for i in logs_to_order:
            if i.get('log') == log_guilted:
                vet_aux.append(i)

        print("O impostor ?? " + vet_aux.pop().get('user'))
        print("Adeus cidad??o sborniano! Que a paz o acompanhe.")

    elif option == "2":
        print("Ordenando os logs. Tempo estimado: 0.15s")
        start = time.time()
        orderedLogs = countingSort(logs_to_order, get_biggest_value(logs_to_order))
        end = time.time()
        print("Logs ordenados. Tempo de execu????o: " + str(end - start))
        print("Encontrando o(s) impostor(es)...")

        index_guilted = (1000000 - (AUX - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        for i in logs_to_order:
            if i.get('log') == log_guilted:
                print('Impostor encontrado: ', i.get('user'))
        print("Adeus cidad??o sborniano! Que a paz o acompanhe.")

    elif option == "3":
        print("Ordenando os logs. Tempo estimado: 0.15s")
        start = time.time()
        orderedLogs = radixSort(logs_to_order)
        end = time.time()
        print("Logs ordenados. Tempo de execu????o: " + str(end - start))
        print("Encontrando o(s) impostor(es)...")

        index_guilted = (1000000 - (AUX - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        for i in logs_to_order:
            if i.get('log') == log_guilted:
                vet_aux.append(i)

        print("O impostor ?? " + vet_aux.pop().get('user'))
        print("Adeus cidad??o sborniano! Que a paz o acompanhe.")

    elif option == "4":
        print("Ordenando os logs. Tempo estimado: 1.60s")
        start = time.time()
        orderedLogs = quickSort(logs_to_order, 0, len(logs_to_order) - 1)
        end = time.time()
        print("Logs ordenados. Tempo de execu????o: " + str(end - start))
        print("Encontrando o(s) impostor(es)...")

        index_guilted = (1000000 - (AUX - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        print('Impostor encontrado: ', log_guilted.get('user'))
        print("Adeus cidad??o sborniano! Que a paz o acompanhe.")

    elif option == "5":
        print("Ordenando os logs. Tempo estimado: 1.60s")
        start = time.time()
        orderedLogs = mergeSort(logs_to_order)
        end = time.time()
        print("Logs ordenados. Tempo de execu????o: " + str(end - start))
        print("Encontrando o(s) impostor(es)...")
        index_guilted = (1000000 - (AUX - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        print('Impostor encontrado: ', log_guilted.get('user'))
        print("Adeus cidad??o sborniano! Que a paz o acompanhe.")

    elif option == "6":
        print("Ordenando os logs. Tempo estimado: 3.60s")
        start = time.time()
        orderedLogs = heapSort(logs_to_order)
        end = time.time()
        print("Logs ordenados. Tempo de execu????o: " + str(end - start))
        print("Encontrando o(s) impostor(es)...")

        index_guilted = (1000000 - (AUX - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        print('Impostor encontrado: ', log_guilted.get('user'))
        print("Adeus cidad??o sborniano! Que a paz o acompanhe.")

    elif option == "7":
        print("Ordenando os logs. Tempo estimado: 4h")
        start = time.time()
        orderedLogs = insertionSort(logs_to_order, len(logs_to_order))
        end = time.time()
        print("Logs ordenados. Tempo de execu????o: " + str(end - start))
        print("Encontrando o(s) impostor(es)...")

        index_guilted = (1000000 - (AUX - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        print('Impostor encontrado: ', log_guilted.get('user'))
        print("Adeus cidad??o sborniano! Que a paz o acompanhe.")

    elif option == "8":
        print("Ordenando os logs. Tempo estimado: 4h")
        start = time.time()
        orderedLogs = selectionSort(logs_to_order, len(logs_to_order))
        end = time.time()
        print("Logs ordenados. Tempo de execu????o: " + str(end - start))
        print("Encontrando o(s) impostor(es)...")

        index_guilted = (1000000 - (AUX - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        print('Impostor encontrado: ', log_guilted.get('user'))
        print("Adeus cidad??o sborniano! Que a paz o acompanhe.")

    elif option == "9":
        print("Ordenando os logs. Tempo estimado: 23h")
        start = time.time()
        orderedLogs = bubbleSort(logs_to_order, len(logs_to_order))
        end = time.time()
        print("Logs ordenados. Tempo de execu????o: " + str(end - start))
        print("Encontrando o(s) impostor(es)...")

        index_guilted = (1000000 - (AUX - len(orderedLogs)))
        log_guilted = orderedLogs[index_guilted]
        print('Impostor encontrado: ', log_guilted.get('user'))
        print("Adeus cidad??o sborniano! Que a paz o acompanhe.")

    elif option == "10":
        print("Digite o n??mero do log de busca: ")
        x = int(input())

        start = time.time()
        hash_table = hash_by_division(get_all_data())
        end = time.time()
        print("Hash Table criado. Tempo de execu????o: " + str(end - start))

        print("A posicao encontrada foi: ")
        start = time.time()
        display_hash(busca_binaria(x, hash_table))
        end = time.time()
        print("Busca Bin??ria com tempo de execu????o de: " + str(end - start))

    elif option == "11":
        print("Digite o n??mero do log de busca: ")
        x = int(input())

        start = time.time()
        hash_table = hash_by_division(get_all_data())
        end = time.time()
        print("Hash Table criado. Tempo de execu????o: " + str(end - start))
        print("A posicao encontrada foi: ")
        start = time.time()
        display_hash(interpolation_search(hash_table,x))
        end = time.time()
        print("Busca Interpolada com tempo de execu????o de: " + str(end - start))

    elif option == "12":
        print("Digite o n??mero do log de busca: ")
        x = int(input())

        start = time.time()
        hash_table = hash_by_division(logs_to_order)
        end = time.time()
        print("Hash Table criado. Tempo de execu????o: " + str(end - start))
        hash_table = normalize_data(hash_table)
        print("A posicao encontrada foi: ")
        start = time.time()
        display_hash(busca_binaria(x, hash_table))
        end = time.time()
        print("Busca Bin??ria com tempo de execu????o de: " + str(end - start))

    elif option == "13":
        print("Digite o n??mero do log de busca: ")
        x = int(input())

        start = time.time()
        hash_table = hash_by_division(logs_to_order)
        end = time.time()
        print("Hash Table criado. Tempo de execu????o: " + str(end - start))

        print("A posicao encontrada foi: ")
        start = time.time()
        display_hash(interpolation_search(hash_table,x))
        end = time.time()
        print("Busca Interpolada com tempo de execu????o de: " + str(end - start))

    else:
        print('Op????o inv??lida!')


    
