print("is it?")
print("=hello world")
print(1 + 2)

def output_graph(x: int, y:int, c: str):
    for i in range(x):
        for j in range(y):
            print(c, end="")
        print()


if __name__ == "__main__":
    output_graph(2,3,"*")
    output_graph(4, 7, "0")
    output_graph(2, 3, "+")
