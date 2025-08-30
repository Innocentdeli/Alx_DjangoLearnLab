
---

#### 📄 `delete.md`
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
