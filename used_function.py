# file one.py
def func():
    print("func() in used_function.py")

print("top-level in used_function.py")

if __name__ == "__main__":
    print("used_function.py is being run directly")
else:
    print("used_function.py is being imported into another module")