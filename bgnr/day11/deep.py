import random
from os import system
import art

# Константы
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
BLACKJACK = 21
DEALER_MIN = 17

def clear_screen():
    """Очищает консоль для разных ОС"""
    system('cls' if system == 'nt' else 'clear')

def deal_card(quantity=1):
    """Раздает указанное количество случайных карт"""
    return [random.choice(CARDS) for _ in range(quantity)]

def calculate_score(cards):
    """Вычисляет сумму очков с учетом правил для туза"""
    if sum(cards) == BLACKJACK and len(cards) == 2:
        return 0  # Blackjack (туз + 10)
    
    if 11 in cards and sum(cards) > BLACKJACK:
        cards.remove(11)
        cards.append(1)  # Заменяем туз с 11 на 1
    
    return sum(cards)

def compare(user_score, dealer_score):
    """Сравнивает результаты игрока и дилера"""
    if user_score == dealer_score:
        return "Ничья! 🙃"
    elif dealer_score == 0:
        return "Дилер сделал Blackjack! Вы проиграли 😱"
    elif user_score == 0:
        return "Blackjack! Вы выиграли! 😎"
    elif user_score > BLACKJACK:
        return "Вы перебрали. Вы проиграли 😭"
    elif dealer_score > BLACKJACK:
        return "Дилер перебрал. Вы выиграли! 😁"
    elif user_score > dealer_score:
        return "Вы выиграли! 😃"
    else:
        return "Вы проиграли 😤"

def play_game():
    """Основная функция игры"""
    print(art.logo)
    
    user_cards = deal_card(2)
    dealer_cards = deal_card(2)
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        
        print(f"    Ваши карты: {user_cards}, текущий счет: {user_score}")
        print(f"    Первая карта дилера: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > BLACKJACK:
            game_over = True
        else:
            another_card = input("Хотите взять еще карту? 'y' - да, 'n' - нет: ").lower()
            if another_card == 'y':
                user_cards.extend(deal_card())
            else:
                game_over = True

    # Ход дилера
    while dealer_score != 0 and dealer_score < DEALER_MIN:
        dealer_cards.extend(deal_card())
        dealer_score = calculate_score(dealer_cards)

    # Вывод результатов
    print(f"\n    Ваши финальные карты: {user_cards}, финальный счет: {user_score}")
    print(f"    Карты дилера: {dealer_cards}, финальный счет: {dealer_score}")
    print(compare(user_score, dealer_score))

def main():
    """Главный цикл программы"""
    while True:
        play_game()
        restart = input("\nХотите сыграть еще раз? 'y' - да, 'n' - нет: ").lower()
        if restart != 'y':
            print("Спасибо за игру! До свидания!")
            break
        clear_screen()

if __name__ == "__main__":
    main()