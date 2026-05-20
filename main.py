import json
from datetime import datetime

def add_book():
    books = load_books()
    
    author = input("Введите автора: ")
    title = input("Введите название книги: ")
    
    # Проверка на дубликаты
    for book in books:
        if book['author'].lower() == author.lower() and book['title'].lower() == title.lower():
            print("Ошибка: Эта книга уже есть в списке!")
            return
    
    # Валидация оценки
    while True:
        try:
            rating = int(input("Введите оценку (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть от 1 до 5!")
        except ValueError:
            print("Пожалуйста, введите целое число!")
    
    date = input("Введите дату прочтения (опционально): ")
    if not date:
        date = "Не указана"
    
    new_book = {
        'author': author,
        'title': title,
        'rating': rating,
        'date': date
    }
    
    books.append(new_book)
    save_books(books)
    print(f"Книга '{title}' успешно добавлена!")

def load_books():
    try:
        with open('books.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open('books.json', 'w') as f:
        json.dump(books, f, indent=4)

def show_all_books():
    books = load_books()
    
    if not books:
        print("Список книг пуст!")
        return
    
    print("\nВсе прочитанные книги:")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} — {book['author']}")
        print(f"   Оценка: {book['rating']}/5")
        print(f"   Дата прочтения: {book['date']}")
        print("-" * 30)

def show_average_rating():
    books = load_books()
    
    if not books:
        print("Список книг пуст!")
        return
    
    total_rating = sum(book['rating'] for book in books)
    average = total_rating / len(books)
    
    print(f"\nСредняя оценка всех книг: {average:.2f}/5")
    print(f"Всего оценено книг: {len(books)}")

def show_author_stats():
    books = load_books()
    
    if not books:
        print("Список книг пуст!")
        return
    
    author_counts = {}
    author_ratings = {}
    
    for book in books:
        author = book['author']
        rating = book['rating']
        
        if author in author_counts:
            author_counts[author] += 1
            author_ratings[author].append(rating)
        else:
            author_counts[author] = 1
            author_ratings[author] = [rating]
    
    print("\nСтатистика по авторам:")
    print("-=" * 20)
    
    for author in sorted(author_counts.keys()):
        count = author_counts[author]
        ratings = author_ratings[author]
        avg_rating = sum(ratings) / len(ratings)
        
        print(f"{author}:")
        print(f"   Книг прочитано: {count}")
        print(f"   Средняя оценка: {avg_rating:.2f}/5")
        print(f"   Оценки: {', '.join(map(str, ratings))}")
        print()

def delete_book():
    books = load_books()
    
    if not books:
        print("Список книг пуст!")
        return
    
    print("\nТекущий список книг:")
    for i, book in enumerate(books):
        print(f"{i + 1}. {book['title']} — {book['author']} (оценка: {book['rating']})")
    
    while True:
        try:
            choice = int(input("\nВведите номер книги для удаления (0 для отмены): "))
            if choice == 0:
                print("Удаление отменено.")
                return
            elif 1 <= choice <= len(books):
                removed_book = books.pop(choice - 1)
                save_books(books)
                print(f"Книга '{removed_book['title']}' успешно удалена!")
                break
            else:
                print(f"Пожалуйста, введите число от 1 до {len(books)} или 0 для отмены.")
        except ValueError:
            print("Пожалуйста, введите целое число!")

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
            # Здесь должна быть функция добавления книги
            pass
        elif choice == '2':
            show_all_books()
        elif choice == '3':
            show_average_rating()
        elif choice == '4':
            show_author_stats
