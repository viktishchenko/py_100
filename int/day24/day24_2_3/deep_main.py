# Определяем пути к файлам
INPUT_NAMES_PATH = 'D:/pyAngela/day24_2_3/Input/Names/invited_names.txt'
INPUT_LETTER_PATH = 'D:/pyAngela/day24_2_3/Input/Letters/starting_letter.txt'
OUTPUT_DIR = 'D:/pyAngela/day24_2_3/Output/ReadyToSend/Deep/'

# Читаем шаблон письма один раз перед циклом
with open(INPUT_LETTER_PATH, 'r') as letter_file:
    letter_template = letter_file.readlines()

# Обрабатываем каждое имя
with open(INPUT_NAMES_PATH, 'r') as names_file:
    for name in names_file:
        name = name.strip()
        if not name:  # Пропускаем пустые строки
            continue
            
        # Создаем персонализированное письмо
        personalized_letter = []
        for line in letter_template:
            personalized_letter.append(line.replace('[name]', name))
        
        # Сохраняем письмо в файл
        output_path = f'{OUTPUT_DIR}letter_for_{name}.txt'
        with open(output_path, 'w') as output_file:
            output_file.writelines(personalized_letter)