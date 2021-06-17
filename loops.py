for i in range(0,10):
    for j in range(2,3):
        if i % j == 0:
            break
    else:
        print(i)