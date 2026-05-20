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
def add_book():
    books = load_books()
    author = input("Автор: ")
    title = input("Название: ")

    # Проверка на дубликаты
    for book in books:
        if book['author'] == author and book['title'] == title:
            print("Эта книга уже есть в списке!")
            return

    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть от 1 до 5!")
        except ValueError:
            print("Введите число!")

    date = input("Дата прочтения (например, 2024-05-20): ")

    new_book = {
        'author': author,
        'title': title,
        'rating': rating,
        'date': date
    }

    books.append(new_book)
    save_books(books)
    print("Книга добавлена!")

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
             add_book()
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
