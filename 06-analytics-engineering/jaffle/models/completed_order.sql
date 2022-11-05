SELECT 
    o.id 
    , o.order_date
    , o.status
    , c.first_name
    , c.last_name 
FROM {{source('jaffle','jaffle_shop_orders')}} as o
JOIN {{source('jaffle','jaffle_shop_customers')}} as c
on
    o.user_id = c.id
WHERE status = 'completed' 