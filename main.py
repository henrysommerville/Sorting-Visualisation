import pygame
import random
from typing import Callable
import time

k = 0

def draw(win: pygame.display, arrays: list[int], height: int) -> None:
    win.fill((36, 36, 36))
    for i in range(len(arrays)):
        pygame.draw.line(win, (255, 255, 255), (i, height), (i, arrays[i]))
    pygame.display.flip()
    pygame.display.update()

    
def swap(index_one: int, index_two: int, arrays: list[int]) -> None:
    temp = arrays[index_one]
    arrays[index_one] = arrays[index_two]
    arrays[index_two] = temp

def bubble(win: pygame.display, arrays: list[int], height: int) -> None:
    global k
    if k < len(arrays):
        i = 0
        for i in range(len(arrays) - i - 1):
            a = arrays[i]
            b = arrays[i + 1]
            if b > a:
                swap(i, i + 1, arrays, False)
    
    draw(win, arrays, height)

    k += 1

def partition(arrays: list[int], start: int, end: int) -> None:
    pivot = arrays[end]
    pivot_index = start
    for i in range(start, end):
        if arrays[i] > pivot:
            swap(pivot_index, i, arrays)
            pivot_index += 1
    swap(pivot_index, end, arrays)
    return pivot_index


def quick_sort(win: pygame.display, arrays: list[int], \
        start: int, end: int, height: int) -> None:
    draw(win, arrays, height)
    if start >= end:
        return None
    index = partition(arrays, start, end)
    quick_sort(win, arrays, start, index - 1, height)
    quick_sort(win, arrays, index + 1, end, height)

def merge(arrays, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arrays[l + i]
 
    for j in range(0, n2):
        R[j] = arrays[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arrays[k] = L[i]
            i += 1
        else:
            arrays[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arrays[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arrays[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted

def merge_sort(arrays: list[int], l, r, win, height):
    draw(win, arrays, height)
    if l < r:
         # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
         # Sort first and second halves
        merge_sort(arrays, l, m, win, height)
        merge_sort(arrays, m+1, r, win, height)
        merge(arrays, l, m, r)
    draw(win, arrays, height)
    


def main():
    width = 900
    height = 600
    win = pygame.display.set_mode((width, height))
    run = True
    is_bubble = False
    is_quick_sort = False
    is_merge_sort = True
    arrays = []
    for i in range(width):
        arrays.append(random.randint(0, height))
    finished = False

    while run == True:
        global k
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if not finished:
            if is_bubble:
                bubble(win, arrays, height)
                finished = True
            if is_quick_sort:
                quick_sort(win, arrays, 0, len(arrays) - 1, height)
                finished = True
            if is_merge_sort:
                merge_sort(arrays, 0, len(arrays) - 1, win, height)
                finished = True

        pygame.display.update()
        

if __name__ == '__main__':
    main()