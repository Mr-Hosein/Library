import logging
from datetime import datetime


logging.basicConfig(filename = 'log_file.log' , level = logging.INFO)
logger = logging.getLogger()


# class Book:
#     def __init__(self, title: str, author: str, is_borrowed: bool = False):
#             self.title = title
#             self.author = author
#             self.is_borrowed = is_borrowed

#     def show_detail(self):
#         status = "amanat dade shode" if self.is_borrowed else "mojood hast"
#         return f"{self.title} - {self.author} - {status}"
        
#     def change_loan_status(self, status: bool):
#         self.is_borrowed = status
    

class Library:

    def __init__(self, list_books: list):
            self.list_books = list_books
    
    def search_by_name(self, name: str) -> list:
        name = name.lower()
        found = [book for book in self.list_books if name in book.title.lower()]
        return found

    def loan_book(self,  book: Book) -> bool:
        if book.is_borrowed:
            return False
        book.change_loan_status(True)
        logger.info(f"Book borrowed: {book.title} at {datetime.now()}")
        return True

    def return_book(self, book: Book) -> bool:
        if not book.is_borrowed:
            return False
        book.change_loan_status(False)
        logger.info(f"Book returned: {book.title} at {datetime.now()}")
        return True
    


def main():

    sample_books = [
        Book("Asare Morakab", "Ali Ahmadi"),
        Book("Pedare Pooldar, Pedare Faghir", "Robert Kiyosaki"),
        Book("Ghaleye Heyvanat", "George Orwell")
    ]

    library = Library(sample_books)

    while True:
        choice = input("1. namayeshe hamaye ketabha\n" \
                        "2. search\n" \
                        "3. amanat ketab\n" \
                        "4. bazgardandane ketab\n" \
                        "5. Exit\n-->")
        
        if choice == "1":
            print("🔴" * 30)
            print("liste hamaye ketabha:")
            for index , book in enumerate(library.list_books, 1):
                print(f"{index}- {book.show_detail()}")
                
            print("🔴" * 30)
        
        elif choice == "2":
            query = input("name bakhshi az name kamele ketab ra vared konid: ").strip()
            results = library.search_by_name(query)
            if not results:
                print("hich ketabi peida nashod.")

            else:
                print("🔴" * 30)
                print(f"{len(results)} ketab peida shod:")
                for index, book in enumerate(results, 1):
                    print(f"{index}. {book.show_detail()}")
                print("🔴" * 30)

        elif choice == "3":
            print("🔴" * 30)
            query = input("name ketabi ke mikhahid be emant begirid ra vard konid: ").strip()
            results = library.search_by_name(query)
            if not results:
                print("ketabi ba in nam peida nashod!")
                continue
            elif len(results) > 1:
                print("ketab peida shod shomareye ketab ra vared konid:")
                for index, book in enumerate(results, 1):
                    print(f"{index}. {book.show_detail()}")
                try:
                    sel = int(input("shomareye ketab: "))
                    if sel < 1 or sel > len(results):
                        print("shomareye namoatabar ast! ❌")
                        continue
                    book = results[sel - 1]
                except ValueError:
                    print("voroodi namoatabar ast! ❌")
                    continue
            else:
                book = results[0]

            if book.is_borrowed:
                print("in ketab be amanat dade shode.")
                print("🔴" * 30)
            else:
                confirm = input(f"aya motmaen hastid ke mikhahid ketab  '{book.title}' ra be amanat begirid? (y/n): ").strip().lower()
                if confirm == 'y':
                    success = library.loan_book(book)
                    if success:
                        print("ketab ba movafaghiat be amanat gerefte shod.")
                        print("🔴" * 30)
                    else:
                        print("khata amanat gereftane ketab. ❌")
                else:
                    print("amaliat laghv shod! ❌")
        

        elif choice == "4":
            print("🔴" * 30)
            query = input("name ketabi ke mikhahid bazgardanid ra vared konid: ").strip()
            results = library.search_by_name(query)
            if not results:
                print("ketabi ba in nam peida nashod!")
                continue
            elif len(results) > 1:
                print("ketab peida shod shomareye ketab ra vared konid:")
                for idx, book in enumerate(results, 1):
                    print(f"{idx}. {book.show_detail()}")
                try:
                    sel = int(input("shomareye ketab: "))
                    if sel < 1 or sel > len(results):
                        print("shomareye namoatabar ast! ❌")
                        continue
                    book = results[sel - 1]
                except ValueError:
                    print("voroodi namoatabar ast! ❌")
                    continue
            else:
                book = results[0]

            if not book.is_borrowed:
                print("in ketab dar hal hazer amanat dade nashode ast!")
            else:
                confirm = input(f"aya motmaen hastid ke mikhahid ketabe '{book.title}' ra bazgardanid? (y/n): ").strip().lower()
                if confirm == 'y':
                    success = library.return_book(book)
                    if success:
                        print("ketab ba movafaghiat bazgardande shod.")
                        print("🔴" * 30)
                    else:
                        print("khata dar bazgardandane ketab! ❌")
                else:
                    print("amaliat laghv shod! ❌")
    
        elif choice == "5":
            print("khorooj az barname khodahafez!👋")
            break

        else:
            print("gozineye namoatabar lotfan mojadadan talash konid!")



if __name__ == "__main__":
    logger.info(f"Library system started at {datetime.now()}")
    main()
