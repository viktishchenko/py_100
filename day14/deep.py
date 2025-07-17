import py_art
import game_data
import random
import os

SCORE = 0
DATA_A = {}
DATA_B = {}
GAME_OVER = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_data(g_data):
    """Выбирает 2 случайных профиля из данных"""
    global DATA_A, DATA_B
    DATA_A, DATA_B = random.sample(g_data, 2)

def compare_data(user_choice):
    """Сравнивает количество подписчиков и возвращает True, если ответ верный"""
    a_followers = int(DATA_A['follower_count'])
    b_followers = int(DATA_B['follower_count'])
    
    if a_followers == b_followers:
        return None  # Ничья
    return (a_followers > b_followers and user_choice == 'a') or (b_followers > a_followers and user_choice == 'b')

# Основной цикл игры
while not GAME_OVER:
    clear_screen()
    print(py_art.logo)
    
    if SCORE > 0:
        print(f'Your score: {SCORE}')
    
    get_random_data(game_data.data)
    
    print(f'Compare A: {DATA_A["name"]}, a {DATA_A["description"]}, from {DATA_A["country"]}')
    print(py_art.vs)
    print(f'Compare B: {DATA_B["name"]}, a {DATA_B["description"]}, from {DATA_B["country"]}')
    
    # Проверка ввода
    while True:
        user_answer = input('Who has more followers? Type "A" or "B": ').lower()
        if user_answer in ('a', 'b'):
            break
        print('Invalid input! Try again.')
    
    # Проверка ответа
    is_correct = compare_data(user_answer)
    if is_correct is None:
        print("It's a tie! Both have the same followers.")
    elif is_correct:
        SCORE += 1
        print(f'You\'re right! Current score: {SCORE}.')
    else:
        print(f'Sorry, wrong answer. Final score: {SCORE}')
        GAME_OVER = True
    
    if not GAME_OVER:
        input('Press Enter to continue...')