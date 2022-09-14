total = int(input())
books = []

for i in range(9):
    books.append(int(input()))

book = total - sum(books)

print(book)