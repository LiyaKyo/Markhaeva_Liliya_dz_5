def odd_nums(max_num: int):
    """
    :param max_num: максимальное число генератора
    :return: генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
    """
    for num in range(1, max_num + 1, 2):
        yield num


odds = odd_nums(15)
print(*odds)