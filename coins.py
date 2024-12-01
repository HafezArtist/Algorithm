n, m = map(int,input().split())   #n is the amount of coins we have. m is the amount of the money that we have.
c = [int(i) for i in input().split()]   #c is an array to keep the coin values.
s = [float('INF')] * (m + 1)   #s is a list where we keep the amount of coins we use from 0 t money + 1.
s[0] = 0

#why inf? cause we want to find the minimum and it's obvious that it always must be a large number to be easy to find the minimum.

for i in range(1, m + 1):  #i is the value we want to pay. iterating from 1 to the money we have(we're finding all ways.)
    for j in range(n):   #j is the coin we want to use. iterating in the number of moneys.
        if c[j] <= i:   #first coin value, second coin value, third coin value and...
            k = i - c[j]   #k is: This represents the remaining amount after using the coin c[j].
            if s[k] + 1 < s[i]:   #The algorithm then checks if using the coin c[j] results in a smaller number of coins than the current minimum stored in s[i].
                s[i] = s[k] + 1   #If so, it updates s[i] to s[k] + 1 (the number of coins needed to make k plus one more coin)



print(s)


# what does this algorithm do? it's a way to find the best way we can pay an amount of money with some coins.