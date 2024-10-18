from typing import Optional, List, Dict

# Article class to represent an article
class Article:
    def __init__(self, id: int, title: str, content: str) -> None:
        self.id: int = id
        self.title: str = title
        self.content: str = content

    def get_id(self) -> int:
        """Returns the ID of the article."""
        return self.id

    def get_title(self) -> str:
        """Returns the title of the article."""
        return self.title

    def get_content(self) -> str:
        """Returns the content of the article."""
        return self.content

    def set_title(self, title: str) -> None:
        """Sets a new title for the article."""
        self.title = title

    def set_content(self, content: str) -> None:
        """Sets new content for the article."""
        self.content = content


# ArticleManager class to manage articles
class ArticleManager:
    def __init__(self) -> None:
        self.articles: Dict[int, Article] = {}
        self.next_id: int = 1  # Track the ID of the next article

    def create(self, title: str, content: str) -> Article:
        """Creates a new article and returns it."""
        article = Article(self.next_id, title, content)
        self.articles[self.next_id] = article
        self.next_id += 1
        return article

    def read(self, id: int) -> Optional[Article]:
        """Reads and returns an article by ID, or None if not found."""
        return self.articles.get(id)

    def update(self, id: int, title: str, content: str) -> bool:
        """Updates the article with the given ID and returns True if successful."""
        if id in self.articles:
            self.articles[id].set_title(title)
            self.articles[id].set_content(content)
            return True
        return False

    def delete(self, id: int) -> bool:
        """Deletes the article with the given ID and returns True if successful."""
        if id in self.articles:
            del self.articles[id]
            return True
        return False

    def get_all(self) -> List[Article]:
        """Returns a list of all articles."""
        return list(self.articles.values())


# Function to display the menu
def display_menu() -> str:
    print("\n=== Article Management ===")
    print("1. View all articles")
    print("2. View a single article")
    print("3. Create a new article")
    print("4. Update an article")
    print("5. Delete an article")
    print("0. Exit")
    choice = input("Please choose an option: ")
    return choice


# Function to read an integer input with a prompt
def read_integer(prompt: str) -> int:
    return int(input(prompt))


# Main function for interaction with the user
def main() -> None:
    manager = ArticleManager()

    while True:
        choice = display_menu()

        if choice == '1':  # View all articles
            articles = manager.get_all()
            if not articles:
                print("No articles available.")
            else:
                for article in articles:
                    print(f"ID: {article.get_id()}, Title: {article.get_title()}")

        elif choice == '2':  # View a single article
            id = read_integer("Enter the article ID: ")
            article = manager.read(id)
            if article:
                print(f"Title: {article.get_title()}")
                print(f"Content: {article.get_content()}")
            else:
                print("Article not found.")

        elif choice == '3':  # Create a new article
            title = input("Enter the article title: ")
            content = input("Enter the article content: ")
            manager.create(title, content)
            print("Article created successfully.")

        elif choice == '4':  # Update an article
            id = read_integer("Enter the ID of the article to update: ")
            if manager.read(id):
                new_title = input("Enter the new title: ")
                new_content = input("Enter the new content: ")
                manager.update(id, new_title, new_content)
                print("Article updated successfully.")
            else:
                print("Article not found.")

        elif choice == '5':  # Delete an article
            id = read_integer("Enter the ID of the article to delete: ")
            if manager.delete(id):
                print("Article deleted successfully.")
            else:
                print("Article not found.")

        elif choice == '0':  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Call the main function
if __name__ == "__main__":
    main()