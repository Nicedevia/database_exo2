from models.model import User, Order, Product

def get_orders_with_product_info(session):


    query = session.query(Order.name_customer, Product.name, User.first_name, User.last_name, Product.price)

    query = query.join(User, Order.user_id == User.id)
    query = query.join(Product, Product.user_id == User.id)

    results = query.all()

    for result in results:
        customer_name = f"{result.first_name} {result.last_name}"
        product_name = result.name
        product_price = result.price
        print(f"Customer Name: {customer_name}, Product Name: {product_name}, Product Price: {product_price}")
