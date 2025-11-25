import sqlite3

# -----------------------------
# Database Initialization
# -----------------------------
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT,
    year INTEGER,
    rating REAL,
    status TEXT
)
''')
conn.commit()


# -----------------------------
# Functions
# -----------------------------
def add_movie():
    title = input("Enter title: ")
    category = input("Enter category/genre: ")
    year = int(input("Enter release year: "))
    rating = float(input("Enter rating (1-10): "))
    status = input("Enter status (Watched/Wishlist): ")

    cursor.execute("INSERT INTO movies (title, category, year, rating, status) VALUES (?, ?, ?, ?, ?)",
                   (title, category, year, rating, status))
    conn.commit()
    print("\nMovie added successfully!\n")


def view_all():
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()

    print("\n---- All Movies/Anime ----")
    for r in rows:
        print(r)
    print()


def search_by_category():
    category = input("Enter category: ")
    cursor.execute("SELECT * FROM movies WHERE category LIKE ?", ('%' + category + '%',))
    rows = cursor.fetchall()

    print(f"\n---- Results in Category '{category}' ----")
    for r in rows:
        print(r)
    print()


def sort_by_rating():
    cursor.execute("SELECT * FROM movies ORDER BY rating DESC")
    rows = cursor.fetchall()

    print("\n---- Sorted by Rating (High to Low) ----")
    for r in rows:
        print(r)
    print()


def sort_by_year():
    cursor.execute("SELECT * FROM movies ORDER BY year DESC")
    rows = cursor.fetchall()

    print("\n---- Sorted by Year (Latest First) ----")
    for r in rows:
        print(r)
    print()


def view_status_list():
    status = input("Enter status to view (Watched/Wishlist): ")
    cursor.execute("SELECT * FROM movies WHERE status = ?", (status,))
    rows = cursor.fetchall()

    print(f"\n---- {status} List ----")
    for r in rows:
        print(r)
    print()


def delete_movie():
    movie_id = int(input("Enter movie ID to delete: "))
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()
    print("\nMovie deleted successfully!\n")


# -----------------------------
# Menu / Main Program
# -----------------------------
while True:
    print("""
========== Movie/Anime Recommendation List ==========
1. Add Movie/Anime
2. View All Entries
3. Search by Category
4. Sort by Rating
5. Sort by Year
6. View Watched/Wishlist List
7. Delete Movie
8. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_by_category()
    elif choice == "4":
        sort_by_rating()
    elif choice == "5":
        sort_by_year()
    elif choice == "6":
        view_status_list()
    elif choice == "7":
        delete_movie()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again!")
