FILEPATH = 'todo.txt'

def get_todos(file_path = FILEPATH):
    """ takes one argument of a file path and returns a list of todos  """
    with open(file_path,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,file_path= FILEPATH,):
    """ takes two argument (data,file path) and writes data to the file  """
    with open(file_path,'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":

    print(get_todos())