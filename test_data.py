import os
import django
import random
import string
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from products.models import Product, ProductImages, productReview, Brand, category

# RANDOM_STR = lambda n: ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

def create_brands(n):
    faker = Faker()
    brands = ['Juhinah', 'El Mara3y', 'M&M', 'Galaxy', 'Pure', 'Azzrk']
    [Brand.objects.bulk_create(
            name = faker.name(),
            image = f'test_data/brands/brand{random.randint(1,4)}.png'     
        )
    for _ in range(n)]
    print(f'{n} Brand created successfully')

def create_category(n):
    for i in range(n):
        category.objects.create(
            name = f'ctg-{i}',
            image = f'test_data/ctg/ctg{random.randint(1,4)}.png' 
        )
    print(f'{n} Category created successfully')

brand_count = Brand.objects.all().count()
category_count = category.objects.all().count()
def create_products(n):
    flags = ['Sale', 'Feature', 'New']
    for i in range(n):
        Product.objects.create(
            name = f'product-{i}', 
            subtitle = f'best product in our website-{i}', 
            img = f'test_data/product/pdct{random.randint(1,31)}.png', 
            sku = random.randint(100000,900000), 
            desc = f'best product in our website {i} best product in our website-{i}', 
            price = round(random.uniform(10.99,100.99), 2), 
            flag = random.choice(flags), 
            quantitity = random.randint(1,20), 
            brand = Brand.objects.all()[random.randint(0,brand_count)], 
            category = category.objects.all()[random.randint(0,category_count)], 
        )
    print(f'{n} Product created successfully')

create_brands(3)
# create_category(1)


