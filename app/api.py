from datetime import datetime, timedelta

from faker import Faker
from fastapi import APIRouter
import random


crawl_routers = APIRouter()
fake = Faker("vi_VN")


@crawl_routers.get("/ecommerce/history")
def ecommerce_history(count: int = 5):
    platforms = ["Shopee", "Tiki", "Amazon"]
    categories = ["Điện thoại", "Laptop", "Thời trang", "Gia dụng", "Đồ chơi", "Sách", "Thực phẩm"]

    data = []
    for _ in range(count):
        platform = random.choice(platforms)
        item = {
            "platform": platform,
            "order_id": fake.uuid4(),
            "user_name": fake.name(),
            "product_name": fake.word().capitalize() + " " + random.choice(["Pro", "Lite", "Plus"]),
            "category": random.choice(categories),
            "price": round(random.uniform(100_000, 10_000_000), 0),
            "status": random.choice(["Đã giao", "Đang giao", "Đã hủy"]),
            "purchase_date": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat(),
            "delivery_address": fake.address()
        }
        data.append(item)
    return {"source": "ecommerce", "total": count, "data": data}


@crawl_routers.get("/social/posts")
def social_posts(count: int = 5):
    platforms = ["Twitter", "Facebook"]
    hashtags = ["#travel", "#food", "#tech", "#music", "#fitness", "#life", "#fun"]

    data = []
    for _ in range(count):
        platform = random.choice(platforms)
        content = fake.sentence(nb_words=random.randint(6, 20))
        post = {
            "platform": platform,
            "post_id": fake.uuid4(),
            "username": fake.user_name(),
            "content": content,
            "hashtags": random.sample(hashtags, random.randint(1, 3)),
            "likes": random.randint(0, 10000),
            "comments": random.randint(0, 2000),
            "shares": random.randint(0, 500),
            "posted_at": (datetime.now() - timedelta(hours=random.randint(1, 720))).isoformat()
        }
        data.append(post)
    return {"source": "social", "total": count, "data": data}


@crawl_routers.get("/bank/transactions")
def bank_transactions(count: int = 5):
    banks = ["Vietcombank", "Techcombank", "MB Bank", "ACB", "TPBank"]
    transaction_types = ["Chuyển khoản", "Nhận tiền", "Thanh toán", "Rút tiền"]
    merchants = ["ShopeePay", "Tiki", "Grab", "Vinmart", "Circle K", "CGV", "Highlands Coffee"]

    data = []
    for _ in range(count):
        txn_type = random.choice(transaction_types)
        amount = round(random.uniform(50_000, 50_000_000), 0)
        transaction = {
            "bank": random.choice(banks),
            "transaction_id": fake.uuid4(),
            "account_name": fake.name(),
            "account_number": f"{random.randint(100000000, 999999999)}",
            "type": txn_type,
            "amount": amount if txn_type != "Nhận tiền" else f"+{amount}",
            "merchant": random.choice(merchants) if txn_type == "Thanh toán" else None,
            "timestamp": (datetime.now() - timedelta(minutes=random.randint(1, 60 * 24 * 30))).isoformat(),
            "status": random.choice(["Thành công", "Thất bại", "Đang xử lý"]),
            "balance_after": round(random.uniform(1_000_000, 100_000_000), 0)
        }
        data.append(transaction)
    return {"source": "bank", "total": count, "data": data}