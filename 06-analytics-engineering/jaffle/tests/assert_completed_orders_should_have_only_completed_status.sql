SELECT
    status
FROM {{ref('completed_order')}}
WHERE status != 'completed'