def odd_nums(max_num: int):
    """
    :param max_num: максимальное число генератора
    :return: генератор нечётных чисел от 1 до n (включительно), не используя ключевое слово yield
    """
    gen = (num for num in range(1, max_num + 1, 2))
    return gen


odds = odd_nums(15)
print(*odds)
