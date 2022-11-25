select product_name,
    price,
    inventory
FROM products
WHERE product_name not LIKE '%en%'
ORDER BY price;