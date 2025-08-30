
---

#### 📄 `update.md`
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
