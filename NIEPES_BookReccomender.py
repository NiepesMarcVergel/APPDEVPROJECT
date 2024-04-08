import random

 ##This will be use for making the class book that will help in the book reccomending function
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


##Will be later use for book reccomending functions
class BookRecommender: 
    def __init__(self, books):
        self.books = books

    def recommend_books_by_genre(self, preferred_genre, num_books=10):
        genre_books = [book for book in self.books if book.genre.lower() == preferred_genre.lower()]
        random_books = random.sample(genre_books, min(num_books, len(genre_books)))
        return random_books


##This is the function that will help in printing 10 books in a same genre
def search_through_genres(recommender):
    preferred_genre = input("Enter a genre to search for: ")
    recommended_books = recommender.recommend_books_by_genre(preferred_genre)
    
    if recommended_books:
        print(f"\nRecommended {preferred_genre.capitalize()} books:")
        for book in recommended_books:
            print(f"- {book.title} by {book.author}")
        
        while True:
            more_books = input("Do you want to see more books in this genre? (yes/no): ")
            if more_books.lower() == "yes":
                recommended_books = recommender.recommend_books_by_genre(preferred_genre, num_books=10)
                if recommended_books:
                    print(f"\nMore {preferred_genre.capitalize()} books:")
                    for book in recommended_books:
                        print(f"- {book.title} by {book.author}")
                else:
                    print("No more books available in this genre.")
                break
            elif more_books.lower() == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print(f"\nNo genre {preferred_genre.capitalize()} books is found.")


##This will be use for reccomending single books at a total randomness
def random_book(books):
    random_book = random.choice(books)
    print(f"\nRandom Book Recommendation:")
    print(f"- {random_book.title} by {random_book.author}")


##A checker for favorite listed books
def check_favorites(favorites):
    print("\nYour Favorites:")
    if favorites:
        for book in favorites:
            print(f"- {book.title} by {book.author}")
    else:
        print("Favorites empty.")


##Use for adding books to favorite list
def add_to_favorites(book, favorites):
    favorites.append(book)
    print(f"{book.title} by {book.author} added to favorites.")


##Use for removing books to favorite list
def remove_from_favorites(book_title, favorites):
    removed = False
    for book in favorites:
        if book.title.lower() == book_title.lower():
            favorites.remove(book)
            removed = True
            print(f"{book.title} by {book.author} removed from favorites.")
            break
    if not removed:
        print("Book not found in favorites.")


##A menu function inside a menu function, the faves function
def favorites_menu(books, favorites):
    while True:
        print("\nFavorites Menu:")
        print("1. Check Favorites")
        print("2. Add a Book to Favorites")
        print("3. Remove a Book from Favorites")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            check_favorites(favorites)
        elif choice == '2':
            book_title = input("Enter the title of the book you want to add to favorites: ")
            found = False
            for book in books:
                if book.title.lower() == book_title.lower():
                    add_to_favorites(book, favorites)
                    found = True
                    break
            if not found:
                print("Book not found.")
        elif choice == '3':
            book_title = input("Enter the title of the book you want to remove from favorites: ")
            remove_from_favorites(book_title, favorites)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


##Use if you want to add more book to the list
def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    new_book = Book(title, author, genre)
    books.append(new_book)
    print("Book has been added successfully!")


def main():
    ## The list of books that I have collected online having Romance, horror, fantasy, mystery and educational
    books = [
        Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
        Book("1984", "George Orwell", "Dystopian"),
        Book("Pride and Prejudice", "Jane Austen", "Romance"),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
        Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy"),
        Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"),
        Book("Outlander", "Diana Gabaldon", "Romance"),
        Book("The Notebook", "Nicholas Sparks", "Romance"),
        Book("Gone with the Wind", "Margaret Mitchell", "Romance"),
        Book("Jane Eyre", "Charlotte Brontë", "Romance"),
        Book("The Fault in Our Stars", "John Green","Romance"),
        Book("Me Before You", "Jojo Moyes", "Romance"),
        Book("Anna Karenina", "Leo Tolstoy", "Romance"),
        Book("The Time Traveler's Wife", "Audrey Niffenegger", "Romance"),
        Book("The Thorn Birds", "Colleen McCullough", "Romance"),
        Book("Romeo and Juliet", "William Shakespeare", "Romance"),
        Book("The Bridges of Madison County", "Robert James Waller", "Romance"),
        Book("Wuthering Heights", "Emily Brontë", "Romance"),
        Book("A Walk to Remember", "Nicholas Sparks", "Romance"),
        Book("The Princess Bride", "William Goldman", "Romance"),
        Book("Bridget Jones's Diary", "Helen Fielding", "Romance"),
        Book("Twilight", "Stephenie Meyer", "Romance"),
        Book("The Rosie Project", "Graeme Simsion", "Romance"),
        Book("The Hating Game", "Sally Thorne", "Romance"),
        Book("One Day", "David Nicholls", "Romance"),
        Book("Eleanor & Park", "Rainbow Rowell", "Romance"),
        Book("The Guernsey Literary and Potato Peel Pie Society", "Mary Ann Shaffer and Annie Barrows", "Romance"),
        Book("Can You Keep a Secret?", "Sophie Kinsella", "Romance"),
        Book("The Proposal", "Jasmine Guillory", "Romance"),
        Book("Crazy Rich Asians", "Kevin Kwan", "Romance"),
        Book("The Wedding Date", "Jasmine Guillory", "Romance"),
        Book("The Kiss Quotient", "Helen Hoang", "Romance"),
        Book("Attachments", "Rainbow Rowell", "Romance"),
        Book("Red, White & Royal Blue", "Casey McQuiston", "Romance"),
        Book("Dracula", "Bram Stoker", "Horror"),
        Book("Frankenstein", "Mary Shelley", "Horror"),
        Book("The Shining", "Stephen King", "Horror"),
        Book("It", "Stephen King", "Horror"),
        Book("The Exorcist", "William Peter Blatty", "Horror"),
        Book("The Haunting of Hill House", "Shirley Jackson", "Horror"),
        Book("Pet Sematary", "Stephen King", "Horror"),
        Book("The Silence of the Lambs", "Thomas Harris", "Horror"),
        Book("Psycho", "Robert Bloch", "Horror"),
        Book("The Turn of the Screw", "Henry James", "Horror"),
        Book("Interview with the Vampire", "Anne Rice", "Horror"),
        Book("American Psycho", "Bret Easton Ellis", "Horror"),
        Book("The Woman in Black", "Susan Hill", "Horror"),
        Book("Carrie", "Stephen King", "Horror"),
        Book("Misery", "Stephen King", "Horror"),
        Book("The Amityville Horror", "Jay Anson", "Horror"),
        Book("The Girl with All the Gifts", "M.R. Carey", "Horror"),
        Book("House of Leaves", "Mark Z. Danielewski", "Horror"),
        Book("Bird Box", "Josh Malerman", "Horror"),
        Book("The Omen", "David Seltzer", "Horror"),
        Book("World War Z", "Max Brooks", "Horror"),
        Book("Rosemary's Baby", "Ira Levin", "Horror"),
        Book("The Hellbound Heart", "Clive Barker", "Horror"),
        Book("The Ritual", "Adam Nevill", "Horror"),
        Book("The October Country", "Ray Bradbury", "Horror"),
        Book("Something Wicked This Way Comes", "Ray Bradbury", "Horror"),
        Book("We Have Always Lived in the Castle", "Shirley Jackson", "Horror"),
        Book("The Strange Case of Dr. Jekyll and Mr. Hyde", "Robert Louis Stevenson", "Horror"),
        Book("Hell House", "Richard Matheson", "Horror"),
        Book("The Ruins", "Scott Smith", "Horror"),
        Book("The Girl with the Dragon Tattoo", "Stieg Larsson", "Mystery"),
        Book("Gone Girl", "Gillian Flynn", "Mystery"),
        Book("The Da Vinci Code", "Dan Brown", "Mystery"),
        Book("The Hound of the Baskervilles", "Arthur Conan Doyle", "Mystery"),
        Book("The Cuckoo's Calling", "Robert Galbraith", "Mystery"),
        Book("And Then There Were None", "Agatha Christie", "Mystery"),
        Book("The Big Sleep", "Raymond Chandler", "Mystery"),
        Book("In the Woods", "Tana French", "Mystery"),
        Book("The No. 1 Ladies' Detective Agency", "Alexander McCall Smith", "Mystery"),
        Book("The Maltese Falcon", "Dashiell Hammett", "Mystery"),
        Book("The Silence of the Lambs", "Thomas Harris", "Mystery"),
        Book("The Secret History", "Donna Tartt", "Mystery"),
        Book("The Woman in White", "Wilkie Collins", "Mystery"),
        Book("The Lincoln Lawyer", "Michael Connelly", "Mystery"),
        Book("The Shadow of the Wind", "Carlos Ruiz Zafón", "Mystery"),
        Book("Sharp Objects", "Gillian Flynn", "Mystery"),
        Book("Rebecca", "Daphne du Maurier", "Mystery"),
        Book("Murder on the Orient Express", "Agatha Christie", "Mystery"),
        Book("The Snowman", "Jo Nesbø", "Mystery"),
        Book("The Adventures of Sherlock Holmes", "Arthur Conan Doyle", "Mystery"),
        Book("The Secret Place", "Tana French", "Mystery"),
        Book("Big Little Lies", "Liane Moriarty", "Mystery"),
        Book("The Name of the Rose", "Umberto Eco", "Mystery"),
        Book("The Spy Who Came in from the Cold", "John le Carré", "Mystery"),
        Book("The Talented Mr. Ripley", "Patricia Highsmith", "Mystery"),
        Book("Dark Places", "Gillian Flynn", "Mystery"),
        Book("The Secret History", "Donna Tartt", "Mystery"),
        Book("The Dry", "Jane Harper", "Mystery"),
        Book("The Reversal", "Michael Connelly", "Mystery"),
        Book("Before I Go to Sleep", "S.J. Watson", "Mystery"),
        Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy"),
        Book("Harry Potter series", "J.K. Rowling", "Fantasy"),
        Book("A Song of Ice and Fire series", "George R.R. Martin", "Fantasy"),
        Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
        Book("The Chronicles of Narnia", "C.S. Lewis", "Fantasy"),
        Book("Mistborn series", "Brandon Sanderson", "Fantasy"),
        Book("The Name of the Wind", "Patrick Rothfuss", "Fantasy"),
        Book("Wheel of Time series", "Robert Jordan and Brandon Sanderson", "Fantasy"),
        Book("His Dark Materials series", "Philip Pullman", "Fantasy"),
        Book("The Witcher series", "Andrzej Sapkowski", "Fantasy"),
        Book("The Stormlight Archive series", "Brandon Sanderson", "Fantasy"),
        Book("The Lies of Locke Lamora", "Scott Lynch", "Fantasy"),
        Book("The Kingkiller Chronicle series", "Patrick Rothfuss", "Fantasy"),
        Book("The Earthsea Cycle", "Ursula K. Le Guin", "Fantasy"),
        Book("The Magicians", "Lev Grossman", "Fantasy"),
        Book("The Riyria Revelations series", "Michael J. Sullivan", "Fantasy"),
        Book("Redwall series", "Brian Jacques", "Fantasy"),
        Book("The Broken Empire series", "Mark Lawrence", "Fantasy"),
        Book("The First Law series", "Joe Abercrombie", "Fantasy"),
        Book("The Black Prism", "Brent Weeks", "Fantasy"),
        Book("The Belgariad series", "David Eddings", "Fantasy"),
        Book("The Inheritance Cycle series", "Christopher Paolini", "Fantasy"),
        Book("The Farseer Trilogy", "Robin Hobb", "Fantasy"),
        Book("The Dresden Files series", "Jim Butcher", "Fantasy"),
        Book("The Lightbringer series", "Brent Weeks", "Fantasy"),
        Book("The Wheel of Time series", "Robert Jordan and Brandon Sanderson", "Fantasy"),
        Book("The Bartimaeus Trilogy", "Jonathan Stroud", "Fantasy"),
        Book("The Chronicles of Prydain", "Lloyd Alexander", "Fantasy"),
        Book("The Dark Tower series", "Stephen King", "Fantasy"),
        Book("The Sword of Truth series", "Terry Goodkind", "Fantasy"),
        Book("Thinking, Fast and Slow", "Daniel Kahneman", "Educational"),
        Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "Educational"),
        Book("Educated: A Memoir", "Tara Westover", "Educational"),
        Book("The Power of Habit: Why We Do What We Do in Life and Business", "Charles Duhigg", "Educational"),
        Book("How to Win Friends and Influence People", "Dale Carnegie", "Educational"),
        Book("The 7 Habits of Highly Effective People", "Stephen R. Covey", "Educational"),
        Book("The Four Agreements: A Practical Guide to Personal Freedom", "Don Miguel Ruiz", "Educational"),
        Book("Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones", "James Clear", "Educational"),
        Book("Quiet: The Power of Introverts in a World That Can't Stop Talking", "Susan Cain", "Educational"),
        Book("Blink: The Power of Thinking Without Thinking", "Malcolm Gladwell", "Educational"),
        Book("Drive: The Surprising Truth About What Motivates Us", "Daniel H. Pink", "Educational"),
        Book("The Immortal Life of Henrietta Lacks", "Rebecca Skloot", "Educational"),
        Book("The Elements of Style", "William Strunk Jr. and E.B. White", "Educational"),
        Book("Outliers: The Story of Success", "Malcolm Gladwell", "Educational"),
        Book("Man's Search for Meaning", "Viktor E. Frankl", "Educational"),
        Book("How to Read Literature Like a Professor: A Lively and Entertaining Guide to Reading Between the Lines", "Thomas C. Foster", "Educational"),
        Book("Born a Crime: Stories from a South African Childhood", "Trevor Noah", "Educational"),
        Book("The Tipping Point: How Little Things Can Make a Big Difference", "Malcolm Gladwell", "Educational"),
        Book("The Omnivore's Dilemma: A Natural History of Four Meals", "Michael Pollan", "Educational"),
        Book("The Art of Learning: An Inner Journey to Optimal Performance", "Josh Waitzkin", "Educational")
    ]
    

    ##The empty list for Favorites Functions
    favorites = []


    # Create a BookRecommender instance
    recommender = BookRecommender(books)


    while True:
        print("\nWelcome To String Books Recommender!")
        print("1. Recommend through Genres")
        print("2. Random Book")
        print("3. Favorites")
        print("4. Add Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            search_through_genres(recommender)
        elif choice == '2':
            random_book(books)
        elif choice == '3':
            favorites_menu(books, favorites)
        elif choice == '4':
            add_book(books)
        elif choice == '5':
            print("Now exiting String Books Recommender program. Thank you for trusting us!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()