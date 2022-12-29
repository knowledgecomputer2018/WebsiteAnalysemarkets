from models import Product

p1 = Product(
     product_id='223344',
     title='My First Project',
     description='A web development project.',
     price='Django',
     product_image='media/actual/actual.jpg',
     product_thumb='media/thump/thump.jpg'
 )
p1.save()
