from fastapi import FastAPI, Query
from typing import List, Optional, Dict
from pydantic import BaseModel, Field

app = FastAPI(title="Book Search API")

books_db = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee",
        "publisher": "J. B. Lippincott & Co.", "year": "1960"},
    {"title": "1984", "author": "George Orwell",
        "publisher": "Secker & Warburg", "year": "1949"},
    {"title": "Pride and Prejudice", "author": "Jane Austen",
        "publisher": "T. Egerton", "year": "1813"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald",
        "publisher": "Charles Scribner's Sons", "year": "1925"},
    {"title": "The Catcher in the Rye", "author": "J. D. Salinger",
        "publisher": "Little, Brown and Company", "year": "1951"},
    {"title": "The Lord of the Rings", "author": "J. R. R. Tolkien",
        "publisher": "Allen & Unwin", "year": "1954"},
    {"title": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling", "publisher": "Bloomsbury", "year": "1997"},
    {"title": "The Hobbit", "author": "J. R. R. Tolkien",
        "publisher": "George Allen & Unwin", "year": "1937"},
    {"title": "Animal Farm", "author": "George Orwell",
        "publisher": "Secker & Warburg", "year": "1945"},
    {"title": "Brave New World", "author": "Aldous Huxley",
        "publisher": "Chatto & Windus", "year": "1932"},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury",
        "publisher": "Ballantine Books", "year": "1953"},
    {"title": "The Alchemist", "author": "Paulo Coelho",
        "publisher": "HarperTorch", "year": "1988"},
    {"title": "The Da Vinci Code", "author": "Dan Brown",
        "publisher": "Doubleday", "year": "2003"},
    {"title": "The Hunger Games", "author": "Suzanne Collins",
        "publisher": "Scholastic Press", "year": "2008"},
    {"title": "The Fault in Our Stars", "author": "John Green",
        "publisher": "Dutton Books", "year": "2012"},
    {"title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari", "publisher": "Harper", "year": "2011"},
    {"title": "Educated", "author": "Tara Westover",
        "publisher": "Random House", "year": "2018"},
    {"title": "Atomic Habits", "author": "James Clear",
        "publisher": "Avery", "year": "2018"},
    {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman",
        "publisher": "Farrar, Straus and Giroux", "year": "2011"},
    {"title": "The Power of Habit", "author": "Charles Duhigg",
        "publisher": "Random House", "year": "2012"},
    {"title": "Clean Code", "author": "Robert C. Martin",
        "publisher": "Prentice Hall", "year": "2008"},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt, David Thomas",
        "publisher": "Addison-Wesley", "year": "1999"},
    {"title": "Fluent Python", "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media", "year": "2015"},
    {"title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann", "publisher": "O'Reilly Media", "year": "2017"},
    {"title": "Introduction to Algorithms", "author": "Thomas H. Cormen et al.",
        "publisher": "MIT Press", "year": "2009"},
    {"title": "Python Crash Course", "author": "Eric Matthes",
        "publisher": "No Starch Press", "year": "2015"},
    {"title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson", "publisher": "Harper", "year": "2016"},
    {"title": "Dune", "author": "Frank Herbert",
        "publisher": "Chilton Books", "year": "1965"},
    {"title": "Project Hail Mary", "author": "Andy Weir",
        "publisher": "Ballantine Books", "year": "2021"},
    {"title": "The Midnight Library", "author": "Matt Haig",
        "publisher": "Canongate Books", "year": "2020"},
    {"title": "Where the Crawdads Sing", "author": "Delia Owens",
        "publisher": "G.P. Putnam's Sons", "year": "2018"},
    {"title": "The Silent Patient", "author": "Alex Michaelides",
        "publisher": "Celadon Books", "year": "2019"},
    {"title": "The Seven Husbands of Evelyn Hugo",
        "author": "Taylor Jenkins Reid", "publisher": "Atria Books", "year": "2017"},
    {"title": "Normal People", "author": "Sally Rooney",
        "publisher": "Hogarth", "year": "2018"},
    {"title": "Becoming", "author": "Michelle Obama",
        "publisher": "Crown", "year": "2018"},
    {"title": "The Body Keeps the Score", "author": "Bessel van der Kolk",
        "publisher": "Penguin Books", "year": "2014"},
    {"title": "How to Win Friends and Influence People",
        "author": "Dale Carnegie", "publisher": "Simon & Schuster", "year": "1936"},
    {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl",
        "publisher": "Beacon Press", "year": "1946"},
    {"title": "The Four Agreements", "author": "Don Miguel Ruiz",
        "publisher": "Amber-Allen Publishing", "year": "1997"},
    {"title": "Rich Dad Poor Dad", "author": "Robert T. Kiyosaki",
        "publisher": "Plata Publishing", "year": "1997"},
    {"title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey", "publisher": "Free Press", "year": "1989"},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill",
        "publisher": "Ralston Society", "year": "1937"},
    {"title": "The Power of Now", "author": "Eckhart Tolle",
        "publisher": "New World Library", "year": "1997"},
    {"title": "The Road Less Traveled", "author": "M. Scott Peck",
        "publisher": "Simon & Schuster", "year": "1978"},
    {"title": "The Gifts of Imperfection", "author": "Brené Brown",
        "publisher": "Hazelden Publishing", "year": "2010"},
    {"title": "Daring Greatly", "author": "Brené Brown",
        "publisher": "Gotham Books", "year": "2012"},
    {"title": "Mindset: The New Psychology of Success",
        "author": "Carol S. Dweck", "publisher": "Random House", "year": "2006"},
    {"title": "Grit: The Power of Passion and Perseverance",
        "author": "Angela Duckworth", "publisher": "Scribner", "year": "2016"},
    {"title": "The Miracle Morning", "author": "Hal Elrod",
        "publisher": "Miracle Morning Publishing", "year": "2012"},
    {"title": "The ONE Thing", "author": "Gary Keller",
        "publisher": "Bard Press", "year": "2013"},
    {"title": "Essentialism: The Disciplined Pursuit of Less",
        "author": "Greg McKeown", "publisher": "Crown Business", "year": "2014"},
    {"title": "Python Crash Course 2nd Edition", "author": "Eric Matthes",
        "publisher": "No Starch Press", "year": "2019"},
    {"title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart", "publisher": "No Starch Press", "year": "2015"},
    {"title": "Fluent Python 2nd Edition", "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media", "year": "2022"},
    {"title": "Python for Data Analysis 3rd Edition",
        "author": "Wes McKinney", "publisher": "O'Reilly Media", "year": "2022"},
    {"title": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
        "author": "Aurélien Géron", "publisher": "O'Reilly Media", "year": "2022"},
    {"title": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "author": "Robert C. Martin", "publisher": "Prentice Hall", "year": "2008"},
    {"title": "The Pragmatic Programmer 20th Anniversary Edition",
        "author": "David Thomas, Andrew Hunt", "publisher": "Addison-Wesley", "year": "2019"},
    {"title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann", "publisher": "O'Reilly Media", "year": "2017"},
    {"title": "Introduction to Algorithms 4th Edition",
        "author": "Thomas H. Cormen et al.", "publisher": "MIT Press", "year": "2022"},
    {"title": "Grokking Algorithms", "author": "Aditya Bhargava",
        "publisher": "Manning Publications", "year": "2016"},
    {"title": "Deep Learning", "author": "Ian Goodfellow et al.",
        "publisher": "MIT Press", "year": "2016"},
    {"title": "Artificial Intelligence: A Modern Approach 4th Edition",
        "author": "Stuart Russell, Peter Norvig", "publisher": "Pearson", "year": "2020"},
    {"title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari", "publisher": "Harper", "year": "2015"},
    {"title": "Homo Deus: A Brief History of Tomorrow",
        "author": "Yuval Noah Harari", "publisher": "Harper", "year": "2017"},
    {"title": "21 Lessons for the 21st Century", "author": "Yuval Noah Harari",
        "publisher": "Spiegel & Grau", "year": "2018"},
    {"title": "Atomic Habits", "author": "James Clear",
        "publisher": "Avery", "year": "2018"},
    {"title": "The Psychology of Money", "author": "Morgan Housel",
        "publisher": "Harriman House", "year": "2020"},
    {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman",
        "publisher": "Farrar, Straus and Giroux", "year": "2011"},
    {"title": "Influence: The Psychology of Persuasion",
        "author": "Robert B. Cialdini", "publisher": "Harper Business", "year": "2006"},
    {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl",
        "publisher": "Beacon Press", "year": "2006"},
    {"title": "The Power of Habit", "author": "Charles Duhigg",
        "publisher": "Random House", "year": "2012"},
    {"title": "How to Win Friends and Influence People",
        "author": "Dale Carnegie", "publisher": "Simon & Schuster", "year": "1936"},
    {"title": "Mindset: The New Psychology of Success",
        "author": "Carol S. Dweck", "publisher": "Random House", "year": "2006"},
    {"title": "Grit: The Power of Passion and Perseverance",
        "author": "Angela Duckworth", "publisher": "Scribner", "year": "2016"},
    {"title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson", "publisher": "Harper", "year": "2016"},
    {"title": "Dune", "author": "Frank Herbert",
        "publisher": "Chilton Books", "year": "1965"},
    {"title": "Project Hail Mary", "author": "Andy Weir",
        "publisher": "Ballantine Books", "year": "2021"},
    {"title": "The Midnight Library", "author": "Matt Haig",
        "publisher": "Canongate Books", "year": "2020"},
    {"title": "Where the Crawdads Sing", "author": "Delia Owens",
        "publisher": "G.P. Putnam's Sons", "year": "2018"},
    {"title": "The Silent Patient", "author": "Alex Michaelides",
        "publisher": "Celadon Books", "year": "2019"},
    {"title": "The Seven Husbands of Evelyn Hugo",
        "author": "Taylor Jenkins Reid", "publisher": "Atria Books", "year": "2017"},
]


class Book(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    author: str
    publisher: str
    year: str = Field(description="first published year")


@app.get("/books/search", response_model=List[Dict[str, str]])
async def search_books(q: Optional[str] = Query(None,  max_length=100, min_length=3),
                       page: int = Query(1, ge=1),
                       size: int = Query(10, ge=1, le=50)):
    if not q:
        return books_db

    q = q.lower().strip()
    results = []

    for book in books_db:
        if (q in book["title"].lower() or
           q in book["author"].lower() or
           q in book["publisher"].lower()):
            results.append(book)

    skip = (page-1)*size
    paginated_results = results[skip: skip+size]

    return paginated_results


@app.post("/books/add", response_model=Book)
async def add_books(book: Book):
    book_dict = dict(book)
    books_db.append(book_dict)
    return book
