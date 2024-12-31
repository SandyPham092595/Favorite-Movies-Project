# Favorite Movies Project

# Project Requirements

# 1. Functions:
# Organize the program using functions to keep the code clean, modular, and reusable.
# Functions should handle specic tasks such as adding a movie, removing a movie, and displaying the list of movies.

# 2. User Input:
# Allow the user to input their favorite movies and interact with the program by adding, removing, and viewing movies.
# Use the input() function to gather data and guide the flow of the program based on user responses.

# 3. Data Management:
# Use a dictionary to store movie information, with movie titles as the keys and their details (e.g., genre, rating) as the values.

# 4. Conditionals:
# Implement if statements to handle dierent operations based on the user’s input, such as adding, viewing, or removing movies.

print("Welcome to the Movie Theatre!")

# Create a dictionary to store movie information.
movies = {}

# Function to add a movie.
def add_movie():
    title = input("What's the name of the movie?: ")
    genre = input("What genre is it?: ")
    rating = input("How is the film rated? (out of 10): ")
    movies[title] = {"genre": genre, "rating": rating}
    print(f"{title} has been added to your favorite movies list.")

# Function to remove a movie.
def remove_movie():
    title = input("Enter the movie title to remove: ")
    if title in movies:
        del movies[title]
        print(f"{title} has been removed from your favorite movies list.")
    else:
        print(f"{title} is not in your favorite movies list.")

# Function to display the list of movies.
def display_movies():
    if movies:
        print("Your favorite movies list:")
        for title, details in movies.items():
            print(f"Title: {title}, Genre: {details['genre']}, Rating: {details['rating']}")
    else:
        print("Your favorite movies list is empty.")

# Main program loop.
while True:
    print("\nMenu:")
    print("1. Add a movie")
    print("2. Remove a movie")
    print("3. Display movies")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        remove_movie()
    elif choice == "3":
        display_movies()
    elif choice == "4":
        print("Enjoy watching your favorite movies! Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

# https://github.com/SandyPham092595/Favorite-Movies-Project.git