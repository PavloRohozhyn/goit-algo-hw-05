def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return (iterations, arr[mid])  # Якщо елемент знайдено, повертаємо його як верхню межу
        
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    # Якщо не знайшли точне співпадіння, повертаємо верхню межу
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]
    
    return (iterations, upper_bound)

# Приклад використання:
arr = [1.1, 2.3, 3.5, 4.8, 5.9, 7.2, 8.6]
target = 4.0
result = binary_search(arr, target)
print(result)  # Виведе кількість ітерацій та найменший елемент >= 4.0

