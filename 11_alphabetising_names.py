PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'}, {
              'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}]

# mylist = sorted(PEOPLE, key=lambda l: l['first'])


def alphabetize_names(x):
    # x.sort(key=lambda l: l['last'])
    x.sort(key=lambda l: l['first'])
    return x


print(alphabetize_names(PEOPLE))
