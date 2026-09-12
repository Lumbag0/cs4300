FAVORITE_BOOKS = ["Star Wars: Thrawn", "Thrawn: Alliances", "Thrawn: Treason", "The Witcher: The Last Wish", 
                  "The Witcher: Season of Storms", "Star Wars: From a Certain Point of View"]

STUDENTS = {
    "Anakin Skywalker": 192837,
    "Obi-Wan Kenobi": 294389,
    "Mace Windu": 183018
}

def first_three_books(books:list) -> list:
    return books[:3]

def main():
    print(first_three_books(FAVORITE_BOOKS))

if __name__ == "__main__":
    main()