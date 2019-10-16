import ramen
from collections import Counter

def main():
    ramen.init()

    print('----MOST COMMON COUNTRY----')
    print()
    country_list = ramen.most_common_country(5)
    print(country_list)

    print()
    print('----revert----')
    print()
    data = ramen.revert(country_list)
    for s in data[0:5]:
    	print(s)


    print()
    print('----HIGEST RATED----')
    print()
    top_5 = ramen.top_rated()
    for s in top_5[:20]:
    	print(s)

    print()
    print('----LOWEST RATED----')
    print()
    low_5 = ramen.lowest_rated()
    for s in low_5[:5]:
    	print(s)

    print()
    print('----LOWEST RATED----')
    print()
    top_10 = ramen.top_ten()
    print(top_10)
    # sorted_ = sorted(data.items(), key=lambda x: x[1], reverse=True)



if __name__ == '__main__':
    main()
    