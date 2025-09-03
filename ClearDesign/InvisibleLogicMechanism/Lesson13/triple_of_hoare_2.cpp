#include <iostream>
#include <vector>


double findMax(std::vector<double> arr) {
	double max = 0;
	for(const double& num : arr) {
		if(num > max) max = num;
	}
	return max;
}

// Доказательство корректности:
//{arr.length > 0} findMax(arr) {result = max(arr)}
// 1. Докажем корректность функции findMax
// Инвариант цикла: max = maximum(arr[0..i-1]) ∧ 1 ≤ i ≤ arr.length
// На каждой итерации цикла переменная max содержит максимально значение элемента массива
// от 0 до i-1
// 1. Первая итерация (инициализация)
// max = arr[0]
// i = 1 -> инвариант выполняется
// Предположим: max = maximum(arr[0..k-1]) и 1 ≤ k ≤ arr.length
// На k-й итерации сравниваем arr[k] с текущим max
// Если arr[k] > max, то обновляем: max = arr[k]
// Теперь max = maximum(arr[0..k])
// Увеличиваем i = k + 1
// Инвариант сохраняется: max = maximum(arr[0..(k+1)-1])
// Цикл завершается, когда i = arr.length
// Из инварианта: max = maximum(arr[0..arr.length-1])
// Это означает: max = maximum(arr) - что и требовалось доказать
// Постусловие выполняется
