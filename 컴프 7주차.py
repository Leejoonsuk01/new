# Quiz 1
import random


def generate_lotto_numbers():
    result = []
    while len(result) < 6:
        num = random.randint(1, 45)
        if num not in result:
            result.append(num)
    return result


print(generate_lotto_numbers())


# Quiz 2
class Gugudan:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1, 10):
            print(f"{self.num} X {i} = {self.num * i}")


# Book 클래스: 책의 정보를 관리하고 대출/반납을 담당하는 클래스
class Book:
    def __init__(self, title, author, available=True):
        """
        책 클래스의 생성자
        :param title: 책의 제목
        :param author: 책의 저자
        :param available: 대출 가능 여부 (기본값: True)
        """
        self.title = title       # 책의 제목
        self.author = author     # 책의 저자
        self.available = available  # 책이 대출 가능한지 여부

    def borrow(self):
        """
        책을 대출하는 메서드
        책이 대출 가능하다면 대출 상태로 변경하고 메시지 출력
        책이 이미 대출 중이라면 대출 불가 메시지 출력
        """
        if self.available:
            self.available = False  # 대출 상태로 변경
            print(f"'{self.title}' 책이 대출되었습니다.")
        else:
            print(f"'{self.title}' 책은 현재 대출 중입니다.")

    def return_book(self):
        """
        책을 반납하는 메서드
        책이 대출 중이라면 반납 상태로 변경하고 메시지 출력
        책이 이미 반납 상태라면 반납 불가 메시지 출력
        """
        if not self.available:
            self.available = True  # 반납 상태로 변경
            print(f"'{self.title}' 책이 반납되었습니다.")
        else:
            print(f"'{self.title}' 책은 대출 상태가 아닙니다.")


# Library 클래스: 도서관 시스템을 관리하는 클래스
class Library:
    def __init__(self, name):
        """
        도서관 클래스의 생성자
        :param name: 도서관 이름
        """
        self.name = name    # 도서관 이름
        self.books = []     # 도서관에 있는 책 목록

    def add_book(self, book):
        """
        도서관에 책을 추가하는 메서드
        :param book: 추가할 책 (Book 객체)
        """
        self.books.append(book)  # 도서관 책 목록에 책 추가
        print(f"'{book.title}' 책이 도서관에 추가되었습니다.")

    def list_books(self):
        """
        도서관에 있는 모든 책 목록을 출력하는 메서드
        책의 제목, 저자, 대출 가능 여부를 함께 출력
        """
        print(f"\n'{self.name}' 도서관에 있는 책 목록:")
        for book in self.books:
            status = '대출 가능' if book.available else '대출 중'
            print(f"제목: {book.title}, 저자: {book.author}, 상태: {status}")
        print()  # 줄 바꿈


# 테스트 코드: 도서관과 책 객체를 생성하고 대출 및 반납 과정을 시뮬레이션
if __name__ == "__main__":
    # 도서관 객체 생성
    library = Library("중앙 도서관")

    # 책 객체 생성
    book1 = Book("1984", "조지 오웰")
    book2 = Book("앵무새 죽이기", "하퍼 리")
    book3 = Book("데미안", "헤르만 헤세")

    # 도서관에 책 추가
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # 도서관 책 목록 출력
    library.list_books()

    # 책 대출 테스트
    book1.borrow()
    library.list_books()  # 대출 후 상태 확인

    # 이미 대출된 책 대출 시도
    book1.borrow()

    # 책 반납 테스트
    book1.return_book()
    library.list_books()  # 반납 후 상태 확인

    # 반납된 책 다시 대출
    book1.borrow()
    library.list_books()