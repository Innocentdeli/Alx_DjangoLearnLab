
---

#### 📄 `retrieve.md`
```markdown
# Retrieve a Book

```python
from bookshelf.models import Book

# Retrieve the book by ID
retrieved_book = Book.objects.get(id=1)

retrieved_book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>
