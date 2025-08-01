import random

# Список слов для угадывания
word_list = ['camel', 'baboon', 'aardvark']
chosen_word = random.choice(word_list)

print(f"Загаданное слово (для отладки): {chosen_word}")  # Можно убрать в финальной версии

game_over = False
correct_letters = []  # Храним угаданные буквы

# Создаем начальное состояние отображения (все буквы скрыты)
display = ['_' for _ in chosen_word]
print(' '.join(display))  # Выводим с пробелами для наглядности

while not game_over:
    guess = input("Угадайте букву: ").lower()
    
    # Проверяем, что введен ровно один символ и это буква
    if len(guess) != 1 or not guess.isalpha():
        print("Пожалуйста, введите одну букву!")
        continue
    
    # Если буква уже угадывалась ранее
    if guess in correct_letters:
        print("Вы уже угадывали эту букву!")
        continue
    
    # Проверяем, есть ли буква в слове
    if guess in chosen_word:
        correct_letters.append(guess)
        print(f"Буква '{guess}' есть в слове!")
        
        # Обновляем отображение
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = letter
    else:
        print(f"Буквы '{guess}' нет в слове. Попробуйте ещё!")
    
    # Выводим текущее состояние
    print(' '.join(display))
    
    # Проверяем, все ли буквы угаданы
    if '_' not in display:
        game_over = True
        print("Поздравляем! Вы угадали слово!")