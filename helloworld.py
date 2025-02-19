print("hello world")
print(1 + 2)
print(True)

def output_graph(x: int):
    for i in range(x):
        print("*", end="")

if __name__ == "__main__":
    output_graph(2)
    output_graph(3)
