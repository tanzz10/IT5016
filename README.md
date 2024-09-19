# IT5016

class Movie:
    def __init__(self, title, genre, year):
        # Initialize a movie with title, genre, year, and availability status
        self.title = title
        self.genre = genre
        self.year = year
        self.available = True  # Default availability status is True

  def mark_as_rented(self):
        # Mark the movie as rented (not available)
        self.available = False

  def mark_as_available(self):
        # Mark the movie as available for renting
        self.available = True

  def __str__(self):
        # String representation of the movie object
        return f"{self.title} ({self.year}) - {self.genre} - {'Available' if self.available else 'Rented'}"
    
class Customer:
    def __init__(self, name):
        # Initialize a customer with a name and an empty list of rented movies
        self.name = name
        self.rented_movies = []

  def rent_movie(self, movie):
        # Allow customer to rent a movie if it is available
        if movie.available:
            movie.mark_as_rented()  # Mark movie as rented
            self.rented_movies.append(movie)  # Add movie to customer's rented list
            print(f"{self.name} rented {movie.title}")
        else:
            print(f"{movie.title} is not available")

  def return_movie(self, movie):
        # Allow customer to return a rented movie
        if movie in self.rented_movies:
            movie.mark_as_available()  # Mark movie as available again
            self.rented_movies.remove(movie)  # Remove from rented list
            print(f"{self.name} returned {movie.title}")
        else:
            print(f"{self.name} did not rent {movie.title}")

  def list_rented_movies(self):
        # List all movies currently rented by the customer
        if self.rented_movies:
            print(f"{self.name}'s Rented Movies:")
            for movie in self.rented_movies:
                print(movie)  # Print each rented movie
        else:
            print(f"{self.name} has no rented movies")
        
class RentalStore:
    def __init__(self):
        # Initialize the rental store with an empty list of movies
        self.movies = []

  def add_movie(self, movie):
        # Add a movie to the store's collection
        self.movies.append(movie)

  def list_movies(self):
        # List all available movies in the store
        if self.movies:
            print("Available Movies:")
            for movie in self.movies:
                print(movie)  # Print each movie
        else:
            print("No movies available")

  def find_movie(self, title):
        # Search for a movie by title (case insensitive)
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie  # Return the found movie
        return None  # Return None if not found
    
def menu():
    # Display the main menu options for the movie rental system
    print("\nMovie Rental System Menu")
    print("1. List Available Movies")
    print("2. Rent a Movie")
    print("3. Return a Movie")
    print("4. List Rented Movies")
    print("5. Add a Movie to Store")
    print("6. Exit")

def main():
    # Initialize the store and pre-add some movies
    store = RentalStore()
    store.add_movie(Movie("Inception", "Sci-Fi", 2010))
    store.add_movie(Movie("The Matrix", "Action", 1999))
    store.add_movie(Movie("The Godfather", "Crime", 1972))

  # Initialize customers with a dictionary for easy access
  customers = {
        "Alice": Customer("Alice"),
        "Bob": Customer("Bob")
    }

   while True:
        menu()  # Display menu options
        choice = input("Enter your choice:").strip()

  if choice == "1":
            store.list_movies()  # List all available movies
        elif choice == "2":
            # Handle renting a movie
            customer_name = input("Enter your name:").strip()
            movie_title = input("Enter movie title to rent:").strip()
            customer = customers.get(customer_name)  # Retrieve customer by name
            movie = store.find_movie(movie_title)  # Find movie in store
            if customer and movie:
                customer.rent_movie(movie)  # Rent the movie if found
            elif not customer:
                print("Customer not found")  # Handle customer not found
            elif not movie:
                print("Movie not found")  # Handle movie not found
        elif choice == "3":
            # Handle returning a movie
            customer_name = input("Enter your name:").strip()
            movie_title = input("Enter movie title to return:").strip()
            customer = customers.get(customer_name)
            movie = store.find_movie(movie_title)
            if customer and movie:
                customer.return_movie(movie)  # Return the movie if found
            elif not customer:
                print("Customer not found")
            elif not movie:
                print("Movie not found")
        elif choice == "4":
            # List rented movies for a specific customer
            customer_name = input("Enter your name:").strip()
            customer = customers.get(customer_name)
            if customer:
                customer.list_rented_movies()  # List the customer's rented movies
            else:
                print("Customer not found")
        elif choice == "5":
            # Add a new movie to the rental store
            title = input("Enter movie title:").strip()
            genre = input("Enter movie genre:").strip()
            year = int(input("Enter movie year:"))  # Corrected to not strip for int conversion
            store.add_movie(Movie(title, genre, year))
            print(f"Movie '{title}' added to the store")
        elif choice == "6":
            print("Exiting...")  # Exit the program
            break
        else:
            print("Invalid choice, please try again")  # Handle invalid input

if __name__ == "__main__":
    main()  # Start the program


The Program Principals from the Code.

KISS (Keep It Simple, Stupid)
Analysis: The code is structured in a straightforward manner. Each class has a clear purpose: Movie handles movie attributes, Customer manages customer interactions, and RentalStore organizes the rental process. Methods are named descriptively, making it easy to understand their functionality without excessive complexity.

DRY (Don't Repeat Yourself)
Analysis: The code adheres to the DRY principle by avoiding code duplication. For instance, the rent_movie and return_movie methods in the Customer class encapsulate all logic related to renting and returning movies without repeating similar logic in multiple places.

Open/Closed Principle
Analysis: The code is not entirely open/closed since the RentalStore class directly manages its collection of movies. If you want to change how movies are handled (like adding a new feature), you might need to modify the existing class. A better approach would be to abstract movie handling into a separate class or use an interface.

Composition > Inheritance
Analysis: The code uses composition effectively. Instead of creating subclasses of Customer or Movie, it creates instances of these classes. This approach allows for greater flexibility and easier maintenance, as the behavior of these classes can be modified independently without affecting each other

Single Responsibility Principle
Analysis: Each class has a single responsibility. Movie is responsible for movie details and availability, Customer handles customer-related actions (like renting and returning), and RentalStore manages the collection of movies and their availability. This clarity improves maintainability and readability.

Separation of Concerns
Analysis: The separation of concerns is evident in the structure. Each class is focused on its own responsibilities, and the main application logic resides in the main() function. This organization prevents different parts of the code from interfering with one another, enhancing clarity.

Refactor, Refactor, Refactor
Analysis: While the code is relatively clean, there’s always room for refactoring. For example, the movie search functionality could be encapsulated within the RentalStore to improve separation and maintainability. Regular refactoring will help adapt the code as new features are added.

Clean Code > Clever Code
Analysis: The code emphasizes clean code principles by using clear naming conventions and straightforward logic. Instead of implementing clever shortcuts or complex structures, it opts for readability and maintainability, making it easier for future developers (or the original developer) to understand and modify.
