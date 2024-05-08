import random
import time

inicio_time = time.time()

# atribuição dos 1000 elementos no vetor usado pelo bubble sort
vetor_bubble = []
for i in range(0, 1000):
    vetor_bubble.append(random.randint(1, 1000))

# atribuição dos 1000 elementos no vetor usado pelo selection sort
vetor_selection = []
for i in range(0, 1000):
    vetor_selection.append(random.randint(1, 1000))

# atribuição dos 1000 elementos no vetor usado pelo insertion sort
vetor_insertion = []
for i in range(0, 1000):
    vetor_insertion.append(random.randint(1, 1000))


def bubble_sort(arr):
    # função com bubble
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def selection_sort(arr):
    # função com selection
    for i in range(len(arr)):
        idx_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx_min]:
                arr[j], arr[idx_min] = arr[idx_min], arr[j]
    return arr


def insertion_sort(arr):
    # função com insertion
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    return arr


# chamada da função bubble sort
print(bubble_sort(vetor_bubble))
bubble_time = time.time()
print("Tempo de execução do algoritmo bubble sort = {:.2f}s".format(bubble_time - inicio_time))

# chamada da função selection sort
print(selection_sort(vetor_selection))
selection_time = time.time()
print("Tempo de execução do algoritmo selection sort = {:.2f}s".format(selection_time - inicio_time))

# chamada da função insertion sort
print(insertion_sort(vetor_insertion))
insertion_time = time.time()
print("Tempo de execução do algoritmo insertion sort = {:.2f}s".format(insertion_time - inicio_time))
