select product_name,
    price,
    inventory
FROM products
WHERE product_name LIKE 'TV%';