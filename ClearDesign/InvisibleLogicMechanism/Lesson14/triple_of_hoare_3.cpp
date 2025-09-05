#include <vector>
#include <iostream>

using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high]; 
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

//Доказательство:
// Предусловие для quickSort(arr, low, high): 

// Тройка для partition:
// { low ≤ high }
// pi = partition(arr, low, high);
// { 
//   low ≤ pi ≤ high ∧
//   (∀k ∈ [low, pi]) arr[k] ≤ arr[pi] ∧
//   (∀k ∈ [pi+1, high]) arr[k] > arr[pi] ∧
//   perm(arr_initial, arr_final, low, high)
// }
// Тройка для quickSort:
// { 0 ≤ low ≤ high < arr.size() }
// quickSort(arr, low, high);
// { 
//   sorted(arr, low, high) ∧
//   perm(arr_initial, arr_final, low, high) ∧
//   unchanged(arr, [0..low-1] ∪ [high+1..size-1])
// }
// Тройка для рекурсивных вызовов:
// { sorted(arr, low, pi-1) ∧ sorted(arr, pi+1, high) ∧
//   ∀i∈[low,pi-1], j∈[pi+1,high]: arr[i] ≤ arr[pi] ≤ arr[j] }
// → { sorted(arr, low, high) }

// На каждом шаге массив разбивается на меньшие подмассивы.
// Размеры подмассивов строго уменьшаются.
// Базовый случай (low >= high) всегда достигается.
// Алгоритм завершается,
// При завершении постусловие выполняется,
// → quickSort полностью корректен относительно заданных пред- и постусловий. 
