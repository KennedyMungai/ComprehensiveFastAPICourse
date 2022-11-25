select product_name,
    price
FROM products
WHERE inventory >= 0
    AND price > 859663
ORDER BY product_name;