import os
import csv
from collections import namedtuple, Counter
from typing import List

data = []
Record = namedtuple('Record', ['Review', 'Brand', 'Variety_Style', 'Country', 'Stars', 'Top_Ten'])


def init():
    base_file = os.path.dirname(__file__)
    filename = os.path.join(base_file, 'data', 'ramen_ratings.csv')

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for line in reader:
            record = parse_row(line)
            data.append(record)

def parse_row(row):
    try:
        row['Stars'] = float(row['Stars'])
    except ValueError:
        row['Stars'] = 0.0
    except Exception as x:
        print(x)

    record = Record(Review = row.get('Review'), 
                    Brand = row.get('Brand'), 
                    Variety_Style = row.get('Variety Style'),
                    Country = row.get('Country'),
                    Stars = row.get('Stars'),
                    Top_Ten = row.get('Top_ten'))

    return record


# Record(Review='2580', Brand='New Touch', Variety_Style=None, Country='Japan', Stars=3.75, Top_Ten=None)
def most_common_country(n=0):
    country = list(r.Country for r in data)
    country = Counter(country)

    country_list = [c[0] for c in country.most_common(n)]

    return country_list

def revert(country_list) -> List[Record]:
    return [d for d in data if d.Country not in country_list]



def top_rated():
    return sorted(data, key=lambda s: s.Stars, reverse=True)

def lowest_rated():
    return sorted(data, key=lambda s: s.Stars)

def top_ten():
    return [[r for r in d] for d in data if d.Top_Ten is not None]

most_common_country()
