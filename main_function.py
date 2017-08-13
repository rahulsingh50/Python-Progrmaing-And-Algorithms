# Why you use the if __name__ == main  line

# file two.py
import used_function
print("top-level in main_function.py")
used_function.func()

if __name__ == "__main__":
    print("main_function.py is being run directly")
else:
    print("main_function.py is being imported into another module")