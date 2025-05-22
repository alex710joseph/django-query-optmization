# django-query-optmization

This is a small demo django app that demonstrates how to use select_related and prefetch to optimize django queries.

1. select_related
    - As you can see from the models.py, there is only one customer associated to each order. Whereas it is possible for multiple orders to have the same customer. Hence this is a many-to-one relationship.
    - The order table has a foreign key reference on the customer table using customer id, ie - we can get the customer for that order based on the customer id found in the order row.
    - Now intially in our render template, we are iterating through all the orders and displaying the customer info as well as the order date.
    - But here occurs the classic N+1 queries problem. This is because even though we do just order.objects.all() - we assume it to be one query - internally to display customer info for each order, django does N more queries to get the customer info from the customer table using the customer id found in each order.
    - To solve this, all we need to do logically, is use one single query that joins to the customer table using the foreign key, ie - the customer id. And this is exactly what the select_related achieves.