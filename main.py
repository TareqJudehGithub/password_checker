def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


hello = "0123456789"
print(hello[:5])
print(hello[5:])

my_list = [num **2 for num in range(10) if num % 2 != 0]
print(my_list)

simple_dict = {"a": 1, "b": 2}
# instantiating a dict out of simple_dict:

my_dict1 = {k: v ** 2 for k, v in simple_dict.items()}
print(my_dict1)

# And adding only even items:
my_dict2 = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict2)
print("")

# create a dictionary, where values are key * 2
my_dict3 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict3)

my_dict4 = {num: item * 2 for num, item in simple_dict.items()}
print(my_dict4)