books = ["Python", "Java", "C++"]
copies = [2, 0, 3]
fees = [10, 20, 30]
available = [book for book, copy in zip(books, copies) if copy > 0]
print(available)
data={book:copy for book,copy in zip(books,copies)}
print(data)
fees = list(map(lambda fee:fee+5,fees))
print(fees)