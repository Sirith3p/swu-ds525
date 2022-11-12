-- CTE => common table expression

with 

source as (
    SELECT * FROM {{source('jaffle','jaffle_shop_orders')}}
)
, final as (
    SELECT 
        id
        , user_id
        , order_date
        , status
    FROM source
)

SELECT
    *
FROM final