select product_name,
    price,
    created_at
FROM products
WHERE product_name not LIKE '%en%'
ORDER BY created_at DESC,
    product_name;