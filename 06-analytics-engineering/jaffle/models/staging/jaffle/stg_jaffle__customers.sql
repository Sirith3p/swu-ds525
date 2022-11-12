-- CTE => common table expression

with 


source as (
    SELECT * FROM {{source('jaffle','jaffle_shop_customers')}}
)
, final as (
    SELECT 
        id
        , first_name ||' '|| last_name as name --ยุบรวม column 
        -- , last_name
    FROM source
)

SELECT
    *
FROM final