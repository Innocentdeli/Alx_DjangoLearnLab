# Create a Book

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", year=1949)

book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>



---

### 📄 retrieve.md
```markdown
# Retrieve a Book

```python
from bookshelf.models import Book

# Retrieve the book by ID
retrieved_book = Book.objects.get(id=1)

retrieved_book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>



---

### 📄 update.md
```markdown
# Update a Book

```python
from bookshelf.models import Book

# Retrieve the book
retrieved_book = Book.objects.get(id=1)

# Update the title
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

retrieved_book
# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>



---

### 📄 delete.md
```markdown
# Delete a Book

```python
from bookshelf.models import Book

# Retrieve the book
retrieved_book = Book.objects.get(id=1)

# Delete the book
retrieved_book.delete()

# Check if it’s deleted
Book.objects.all()
# Expected Output:
# <QuerySet []>

