from datetime import datetime, timedelta
from typing import List, Optional

from faker import Faker
from fastapi import APIRouter
from pydantic import BaseModel
import random


crawl_routers = APIRouter()
fake = Faker("vi_VN")


class EcommerceItem(BaseModel):
    user_id: int
    platform: str
    order_id: str
    user_name: str
    product_name: str
    category: str
    price: float
    status: str
    purchase_date: datetime
    delivery_address: str


class EcommerceHistoryResponse(BaseModel):
    source: str
    total: int
    data: List[EcommerceItem]


@crawl_routers.get("/ecommerce/history", response_model=EcommerceHistoryResponse)
def ecommerce_history(count: int = 5) -> EcommerceHistoryResponse:
    platforms = ["Shopee", "Tiki", "Amazon"]
    categories = ["Điện thoại", "Laptop", "Thời trang", "Gia dụng", "Đồ chơi", "Sách", "Thực phẩm"]

    data: List[EcommerceItem] = []
    for _ in range(count):
        platform = random.choice(platforms)
        item = EcommerceItem(
            user_id=random.randint(1, 200),
            platform=platform,
            order_id=fake.uuid4(),
            user_name=fake.name(),
            product_name=fake.word().capitalize() + " " + random.choice(["Pro", "Lite", "Plus"]),
            category=random.choice(categories),
            price=round(random.uniform(100_000, 10_000_000), 0),
            status=random.choice(["Đã giao", "Đang giao", "Đã hủy"]),
            purchase_date=(datetime.now() - timedelta(days=random.randint(1, 365))),
            delivery_address=fake.address(),
        )
        data.append(item)
    return EcommerceHistoryResponse(source="ecommerce", total=count, data=data)


class SocialPostItem(BaseModel):
    user_id: int
    platform: str
    post_id: str
    username: str
    content: str
    hashtags: List[str]
    likes: int
    comments: int
    shares: int
    posted_at: datetime


class SocialPostsResponse(BaseModel):
    source: str
    total: int
    data: List[SocialPostItem]


@crawl_routers.get("/social/posts", response_model=SocialPostsResponse)
def social_posts(count: int = 5) -> SocialPostsResponse:
    platforms = ["Twitter", "Facebook"]
    hashtags = ["#travel", "#food", "#tech", "#music", "#fitness", "#life", "#fun"]

    data: List[SocialPostItem] = []
    for _ in range(count):
        platform = random.choice(platforms)
        content = fake.sentence(nb_words=random.randint(6, 20))
        post = SocialPostItem(
            user_id=random.randint(1, 200),
            platform=platform,
            post_id=fake.uuid4(),
            username=fake.user_name(),
            content=content,
            hashtags=random.sample(hashtags, random.randint(1, 3)),
            likes=random.randint(0, 10000),
            comments=random.randint(0, 2000),
            shares=random.randint(0, 500),
            posted_at=(datetime.now() - timedelta(hours=random.randint(1, 720))),
        )
        data.append(post)
    return SocialPostsResponse(source="social", total=count, data=data)


class BankTransactionItem(BaseModel):
    user_id: int
    bank: str
    transaction_id: str
    account_name: str
    account_number: str
    type: str
    amount: str
    merchant: Optional[str]
    timestamp: datetime
    status: str
    balance_after: float


class BankTransactionsResponse(BaseModel):
    source: str
    total: int
    data: List[BankTransactionItem]


@crawl_routers.get("/bank/transactions", response_model=BankTransactionsResponse)
def bank_transactions(count: int = 5) -> BankTransactionsResponse:
    banks = ["Vietcombank", "Techcombank", "MB Bank", "ACB", "TPBank"]
    transaction_types = ["Chuyển khoản", "Nhận tiền", "Thanh toán", "Rút tiền"]
    merchants = ["ShopeePay", "Tiki", "Grab", "Vinmart", "Circle K", "CGV", "Highlands Coffee"]

    data: List[BankTransactionItem] = []
    for _ in range(count):
        txn_type = random.choice(transaction_types)
        amount_value = round(random.uniform(50_000, 50_000_000), 0)
        amount_str = f"+{amount_value}" if txn_type == "Nhận tiền" else f"{amount_value}"
        transaction = BankTransactionItem(
            user_id=random.randint(1, 200),
            bank=random.choice(banks),
            transaction_id=fake.uuid4(),
            account_name=fake.name(),
            account_number=f"{random.randint(100000000, 999999999)}",
            type=txn_type,
            amount=amount_str,
            merchant=random.choice(merchants) if txn_type == "Thanh toán" else None,
            timestamp=(datetime.now() - timedelta(minutes=random.randint(1, 60 * 24 * 30))),
            status=random.choice(["Thành công", "Thất bại", "Đang xử lý"]),
            balance_after=round(random.uniform(1_000_000, 100_000_000), 0),
        )
        data.append(transaction)
    return BankTransactionsResponse(source="bank", total=count, data=data)