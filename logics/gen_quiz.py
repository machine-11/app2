from crewai_tools import  FileReadTool
from crewai import Agent, Task, Crew
import json, os, random

from pathlib import Path

FOLDER = 'data/new'
FOLDER = 'data/new'
##pick a file from a folder 
def random_file():

    # Current script directory
    current_directory = Path(__file__).resolve()
    # Parent directory
    parent_directory = current_directory.parent


    # # Get the directory of the current script
    # base_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(parent_directory, FOLDER )


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
        
## gen mcq based on the file
def gen_quiz():

    file_path = random_file() 
    print( "FILEPATH", file_path)

    tool_read = FileReadTool( file_path=file_path,  encoding="cp437", errors='ignore') ## 


    agent_examiner = Agent(
        role='Examiner from HDB',
        goal=f'To design quiz to improve learners'' understanding of important policy and steps related to process of buying new flats',
        backstory='You are an experienced quiz setter  and your skilles in designing comprehensive quiz to test learners'' understanding of documents are unparallel',
        verbose=True,
        allow_delegation=False,
        # memory = True,       
    )


    task_setquiz= Task(
       description="come up with 10 multiple choice questions to test understanding of  policy and steps related to process of buying new flats covered in the file provided.\
        to support your answer. do extract sufficient information from the document as explanation ",
        tools=[tool_read],
        agent= agent_examiner ,
        expected_output=''' The questions should not be repeated between runs. Give list of multiple choice questions in json format as below , do not incluse any preamble or "json" \
            
        [
            {
            "question": "xxx",
            "options": [
                "x",
                "x",
                "x,
                "x"
            ],
            "answer": "x",
            "explanation": "x"
            },
         
        ...
        ]    '''
    )
    crew = Crew(
        agents=[agent_examiner],
        tasks=[task_setquiz ]
    )

    crew.kickoff()

    task_output =   task_setquiz.output
    # print(f"Task Description: {task_output.description}")
    # print(f"Task Summary: {task_output.summary}")
    # print(f"Raw Output: {task_output.raw}")

    # if task_output.json_dict:
    #     print(f"JSON Output: {json.dumps(task_output.json_dict, indent=2)}")
    # if task_output.pydantic:
    #     print(f"Pydantic Output: {task_output.pydantic}")

    try:
        o = json.loads(task_output.raw ) 
    except:
        o = gen_quiz()
    return o

  

if __name__ == "__main__":
    # print(random_file() )
    gen_quiz()
