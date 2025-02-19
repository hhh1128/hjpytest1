print("is it?")
print("hello world")
print(1 + 2)
print(True)

def output_graph(x: int,y:int):
    for i in range(x):
        for i in range(y):
            print("*",end="")
        print("", end="\n")


if __name__ == "__main__":
    output_graph(2,3)

