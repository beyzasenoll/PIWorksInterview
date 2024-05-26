WITH CountryMedians AS (
    SELECT
        country,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) AS median_vaccination
    FROM
        vaccination_stats
    WHERE
        daily_vaccinations IS NOT NULL
    GROUP BY
        country
),
CountryMediansWithDefault AS (
    SELECT
        country,
        COALESCE(median_vaccination, 0) AS median_vaccination
    FROM
        CountryMedians
    UNION
    SELECT
        DISTINCT country,
        0 AS median_vaccination
    FROM
        vaccination_stats
    WHERE
        country NOT IN (SELECT country FROM CountryMedians)
)

UPDATE
    vaccination_stats
SET
    daily_vaccinations = COALESCE(v.daily_vaccinations, m.median_vaccination)
FROM
    CountryMediansWithDefault m
WHERE
    vaccination_stats.country = m.country
    AND vaccination_stats.daily_vaccinations IS NULL;
