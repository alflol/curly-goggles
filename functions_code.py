print(1%7)
print(int(6/7))


def readable_timedelta(days):
    weeks = days//7
    day = days%7
    return "{} week(s) and {} day(s).".format(weeks, day)

print(readable_timedelta(14))


egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()