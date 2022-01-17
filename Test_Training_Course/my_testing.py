import random as r

counter = 0
ok = 0
not_ok = 0
number_of_test = 1e5

while counter < number_of_test:
    try:
        assert sum([1, 1, round(1 + r.random()*2)]) == 4
        ok += 1
    except:
        not_ok += 1
    counter += 1

print("Number of test: ", counter, " passed: ", ok, " failed: ", not_ok)