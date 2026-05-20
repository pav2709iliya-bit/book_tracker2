import json
from datetime import datetime

def load_books():
    try:
        with open('books.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open('books.json', 'w') as f:
        json.dump(books, f, indent=4)

def main():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите пункт: ")

        if choice == '6':
            break
        elif choice == '1':
            print("Функция в разработке...")
        elif choice == '2':
            print("Функция в развитии...")
        elif choice == '3':
            print("Функция в развитии...")
        elif choice == '4':
            print("Функция в развитии...")
        elif choice == '5':
            print("Функция в развитии...")
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
