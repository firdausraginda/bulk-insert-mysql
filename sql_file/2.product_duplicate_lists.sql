INSERT INTO public.product_duplicate_lists (product_duplicate_id, external_id, product_id, deleted_at, created_at, updated_at)
WITH
	duplicate_products AS (
		SELECT 
			external_product_code,
			gender, 
			category,
			count(*)
		FROM public.products
		GROUP BY 1,2,3
		HAVING COUNT(*) > 1
	),
    duplicate_products_info AS (
    SELECT
        p.external_id,
        p.id AS product_id,
        p.title,
        p.deleted_at,
        p.created_at,
        p.updated_at
    FROM public.products p
    INNER JOIN (
        SELECT p.id
        FROM duplicate_products dp
        LEFT JOIN public.products p ON
            p.external_product_code = dp.external_product_code
            AND p.gender = dp.gender
            AND p.category = dp.category
    )sub ON
        p.id = sub.id
    )

SELECT
    pd.id AS product_duplicate_id,
    dpi.external_id,
    dpi.product_id,
    dpi.deleted_at,
    dpi.created_at,
    dpi.updated_at
FROM duplicate_products_info dpi
LEFT JOIN public.product_duplicates pd ON
    dpi.title = pd.title
;