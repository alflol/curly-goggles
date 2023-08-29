
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
count = 0
for line in headlines:
    line_lenght = len(line)
    if count+line_lenght < 140:
        news_ticker += line + " "
        count += len(line)+1
    else: # case above 140
        gap = count+line_lenght - 140
        print("gap:"+ str(gap))
        news_ticker += line[:len(line)-gap]
        break

print(news_ticker)
print(len(news_ticker))

print(count)
# write your loop here


def check_prime(n):
    result = '%d is prime number.'.fomat(n)
    for number in range(2,n):
        if n%number == 0:
            result = '%d is NOT a prime number.'.format(n)
            break
    print(result)

check_prime(7)
check_prime(6)
check_prime(4)
check_prime(3)
check_prime(1)
print()



