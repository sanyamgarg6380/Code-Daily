def nForest(n:int) ->None:
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

n=int(input("n="))
print(nForest(n))            