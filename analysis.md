products :
    name
    sku
    brand  * [name,image]
    images  *
    subtitle
    description
    tags  *packege
    price
    flag [new,sale,feature] 
    quantitity
    reviews  *[user_is,producr_id,rate[0:5],feedback,datetime]
    category  *[name,image]


order :
    status [recieved,processed,shiped,delivered]
    user
    id
    total items
    delivery time
    order time
    total
    sub_total 


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
