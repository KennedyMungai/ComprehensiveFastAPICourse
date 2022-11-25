select product_name,
    price
FROM products
WHERE inventory >= 0
    AND price > 859663
    OR inventory > 10
ORDER BY product_name;