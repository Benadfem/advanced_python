def main():
    lax_coordinates = (33.9428, -118.408056)
    city, year, pp, chq, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
    travelers_ids = [('USA', '31195855'),('BRA', 'CE342567'), ('ESP', 'XDA205856') ]

    for passport in sorted(travelers_ids):
        print('%s/%s' %passport)
    # pick the country in the tuple alone. 
    for country, _ in travelers_ids:
        print(country)

if __name__ == '__main__':
    main()