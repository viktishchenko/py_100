from datetime import date
import timeit

# Тест производительности
def test_strftime():
    return date.today().strftime('%Y%m%d')

def test_fstring():
    today = date.today()
    return f"{today.year}{today.month:02d}{today.day:02d}"

def test_join_split():
    return ''.join(str(date.today()).split('-'))

# Результаты (чем меньше тем лучше):
print("strftime:", timeit.timeit(test_strftime, number=100000))
print("f-string:", timeit.timeit(test_fstring, number=100000)) 
print("join/split:", timeit.timeit(test_join_split, number=100000))

# 1
# strftime: 0.6920794000616297
# f-string: 0.254097199998796
# join/split: 0.2890358999138698

# 2
# strftime: 0.6649126999545842
# f-string: 0.2568837000289932
# join/split: 0.293122399947606

#___________________________________

# from datetime import datetime

# now = datetime.now()

# formats = {
#     'YYYYMMDD': now.strftime('%Y%m%d'),          # 20250902
#     'YYYY-MM-DD': now.strftime('%Y-%m-%d'),      # 2025-09-02
#     'DD/MM/YYYY': now.strftime('%d/%m/%Y'),      # 02/09/2025
#     'YYYYMMDD_HHMMSS': now.strftime('%Y%m%d_%H%M%S'),  # 20250902_143015
#     'Человекочитаемый': now.strftime('%d %B %Y') # 02 September 2025
# }

# for name, value in formats.items():
#     print(f"{name}: {value}")