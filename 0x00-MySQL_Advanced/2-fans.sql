-- an SQL script which ranks country origins of bands,
-- This is  ordered by the number of (non-unique) fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans desc;
