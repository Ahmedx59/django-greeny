products :
    name
    sku
    brand  * [name,image]
    images  *
    subtitle
    description
    tags  *
    price
    flag [new,sale,feature] 
    quantity
    reviews  *[user_is,product_id,rate[0:5],feedback,datetime]
    category  *[name,image]


order :
    code
    status [Received,Processed,Shipped,Delivered]
    order time
    delivery time
    total product
    address
    discount
    delivery fee 
    products
        name 
        image
        price 
        quantity
        brand


order_detail :
    order_id
    product_id
    price
    quantity
    total


user :
    address *
    name
    email
    image
    phone_number *
