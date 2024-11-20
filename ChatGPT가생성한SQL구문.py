import sqlite3
import random

class ElectronicsDB:
    def __init__(self, db_name="electronics.db"):
        """
        데이터베이스 초기화 및 연결
        :param db_name: 데이터베이스 파일 이름
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        전자제품 테이블 생성
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)
        self.conn.commit()

    def insert_product(self, product_name, price):
        """
        제품 데이터를 삽입
        :param product_name: 제품명
        :param price: 제품 가격
        """
        self.cursor.execute("""
            INSERT INTO products (product_name, price)
            VALUES (?, ?)
        """, (product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name=None, price=None):
        """
        제품 데이터를 수정
        :param product_id: 수정할 제품 ID
        :param product_name: 새 제품명 (옵션)
        :param price: 새 가격 (옵션)
        """
        if product_name:
            self.cursor.execute("""
                UPDATE products
                SET product_name = ?
                WHERE product_id = ?
            """, (product_name, product_id))
        if price is not None:
            self.cursor.execute("""
                UPDATE products
                SET price = ?
                WHERE product_id = ?
            """, (price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        """
        제품 데이터를 삭제
        :param product_id: 삭제할 제품 ID
        """
        self.cursor.execute("""
            DELETE FROM products
            WHERE product_id = ?
        """, (product_id,))
        self.conn.commit()

    def select_products(self, limit=10):
        """
        제품 데이터를 조회
        :param limit: 조회할 제품 수
        :return: 조회된 제품 데이터 리스트
        """
        self.cursor.execute("""
            SELECT * FROM products
            LIMIT ?
        """, (limit,))
        return self.cursor.fetchall()

    def close(self):
        """
        데이터베이스 연결 닫기
        """
        self.conn.close()


# 샘플 데이터 생성 및 테스트 실행
def generate_sample_data():
    """
    샘플 전자제품 데이터 생성
    """
    db = ElectronicsDB()
    product_names = [
        "Smartphone", "Laptop", "Tablet", "Smartwatch", "Camera",
        "Headphones", "TV", "Microwave", "Refrigerator", "Washing Machine"
    ]
    for i in range(100):
        name = f"{random.choice(product_names)} {random.randint(1, 100)}"
        price = round(random.uniform(50.0, 2000.0), 2)
        db.insert_product(name, price)

    # 일부 데이터 조회
    print("=== 샘플 데이터 조회 ===")
    products = db.select_products(limit=10)
    for product in products:
        print(product)

    # 데이터 수정 예제
    print("\n=== 제품 ID 1의 데이터 수정 ===")
    db.update_product(1, product_name="Updated Smartphone", price=999.99)
    print(db.select_products(limit=1))

    # 데이터 삭제 예제
    print("\n=== 제품 ID 2 삭제 ===")
    db.delete_product(2)
    products = db.select_products(limit=10)
    for product in products:
        print(product)

    # 데이터베이스 연결 닫기
    db.close()


# 실행
if __name__ == "__main__":
    generate_sample_data()
