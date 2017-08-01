# * dict comprehensions
#   - builds a dict instance by producing k:v pairs from iterables

# %% Example 3:1 - Examples of dict comprehensions
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

country_code = {country: code for code, country in DIAL_CODES}
country_code

{code: country.upper() for country, code in country_code.items() if code < 66}
