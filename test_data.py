import django
import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from products.models import Brand , Product , ProductReview , Category , ProductImages
from faker import Faker



def brand_data(n):
    faker = Faker()   # name = ['milka','m&m','galaxy''bazoka','adidas']
    for x in range(n):
        Brand.objects.create(
        name = faker.name(),
        image =f'/brands/prand{random.randint(0,11)}.jpg'
    )   
    print (f'sucsful creat {n} ')

def category_data(n):
    faker = Faker()
    for x in range(n):
        Category.objects.create(
            name = faker.name(),
            image = f'categories/category{random.randint(0,5)}.jpg'
            
        )
    print(f'sucsful creat {n} ')


# print(category_count)
def product_data(n):
    faker = Faker()
    category_count = Category.objects.all().count()
    brand_count = Brand.objects.all().count()
    for x in range(n):
        Product.objects.create(
            name = faker.name(),
            img = f'product_img/p({random.randint(0,6)}).jpg',
            subtitle = faker.sentence(),
            sku = random.randint(10000,99999),
            desc = faker.sentence(),
            price = round(random.uniform(10.99,99.99),2),
            flag = random.choice(['New','Feature','Sale']),
            quantity = random.randint(0,100),
            brand = Brand.objects.get(id = random.randint(1,brand_count)),
            category = Category.objects.get(id = random.randint(1,category_count))

        )
    print(f'successful create {n} ')



category_data(10)
brand_data(10)
product_data(10)
