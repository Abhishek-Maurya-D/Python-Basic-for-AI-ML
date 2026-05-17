class Book():
    def __init__(self, title, author):
        self.title = title;
        self.author = author;
        self.list_of_reviews = [];

    def add_review(self, review):
        self.list_of_reviews.append(review);
    
    def count_review(self):
        print(f"The Total Number of review is : ",len(self.list_of_reviews))

    def display_all_reviews(self):
        print(f"Review for '{self.title}' by {self.author}:")
        if len(self.list_of_reviews) == 0:
            print("No Review Yet");
        else:
            for i, review in enumerate(self.list_of_reviews, 1):
                print(f"{i}.{review}")

book1 = Book("Harry Potter", "J. K. Rowling");
book1.add_review("Amazing Story!");
book1.add_review("Loved the Characters");

book1.count_review()
book1.display_all_reviews();