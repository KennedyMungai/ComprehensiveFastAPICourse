select id,
    product_name,
    price
FROM products
WHERE id in (1, 2, 3)
ORDER BY id;