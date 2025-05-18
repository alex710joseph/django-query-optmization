from django.core.management.base import BaseCommand
from shop.models import Customer, Product, Order
from datetime import date

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        # Clear old data
        Order.objects.all().delete()
        Customer.objects.all().delete()
        Product.objects.all().delete()

        # Create Customers
        john = Customer.objects.create(name='John Jones', email='jj@xyz.com')
        daniel = Customer.objects.create(name='Daniel Cormier', email='dc@xyz.com')
        conor = Customer.objects.create(name='Conor McGregor', email='cm@xyz.com')

        # Create Products
        laptop = Product.objects.create(name='Laptop', price=1000)
        headphones = Product.objects.create(name='Headphones', price=50)
        phone = Product.objects.create(name='Smartphone', price=300)
        keyboard = Product.objects.create(name='Keyboard', price=25)
        mouse = Product.objects.create(name='keyboard', price=15)

        # Create Orders and assign products
        order1 = Order.objects.create(customer=john, order_date=date(2025, 5, 10))
        order1.products.set([laptop, headphones])

        order2 = Order.objects.create(customer=daniel, order_date=date(2025, 5, 12))
        order2.products.add(phone)

        order3 = Order.objects.create(customer=conor, order_date=date(2025, 5, 11))
        order3.products.set([laptop])

        order4 = Order.objects.create(customer=john, order_date=date(2025, 5, 13))
        order4.products.add(keyboard)

        order5 = Order.objects.create(customer=daniel, order_date=date(2025, 5, 13))
        order5.products.set([headphones, keyboard])

        order6 = Order.objects.create(customer=daniel, order_date=date(2025, 5, 16))
        order6.products.add(laptop)

        order7 = Order.objects.create(customer=john, order_date=date(2025, 5, 17))
        order7.products.set([mouse])

        order8 = Order.objects.create(customer=conor, order_date=date(2025, 5, 17))
        order8.products.add(phone)

        order9 = Order.objects.create(customer=conor, order_date=date(2025, 5, 19))
        order9.products.set([headphones])

        order10 = Order.objects.create(customer=conor, order_date=date(2025, 5, 20))
        order10.products.add(keyboard)

        order11 = Order.objects.create(customer=conor, order_date=date(2025, 5, 25))
        order11.products.set([mouse])

        print('Successfully seeded the database!')
