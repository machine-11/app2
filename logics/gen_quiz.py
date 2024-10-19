import json, os, random

def random_file():

    # Specify the directory
    directory = 'data\\new'  # Replace with your directory path

    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Check if there are any files in the directory
    if files:
        # Randomly select a file
        selected_file = random.choice(files)
        print(f'Selected file: {selected_file}')
        return os.path.join(directory , selected_file)
    else:
        print('No files found in the directory.')


def gen_quiz():
  
    file_path = random_file() 
    
    #load json
    with open(file_path , 'r',encoding='utf-8', errors='ignore') as f:
        o = json.load(f ) 

    print(len(o))
    #pick 10 q
    q = random.sample(o, random.randint(10, 10))
    print(len(q))
    return(q)


if __name__ == "__main__":

    print( gen_quiz() )