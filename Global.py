my_global_variable = 5

# You must always declare Global variables if you want them to be global
def my_function():
    global my_global_variable
    my_global_variable = 6
    print(f'my_global_variable inside the function {my_global_variable}')
    

print(f'my_global_variable outside the function before {my_global_variable}')
my_function()
print(f'my_global_variable outside the function after {my_global_variable}')

# what is the output?
# 5
# 6
# 6

