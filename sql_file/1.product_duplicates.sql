INSERT INTO public.product_duplicates (title, created_at, updated_at)
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
	)

SELECT
	p.title,
	max(p.created_at) created_at,
	max(p.updated_at) updated_at
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
GROUP BY 1;