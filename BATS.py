import os 
from random import sample, choice
import re

BATS_NONALPHA = "_-'1234567890" 
# non-alphabetic characters appearing in BATS dataset 
# these only appear in the answer set and never first; i.e. in line[1][1:]  

root = "./BATS_3.0"
loaded = False
files = {}
tags = {}

def load(path="./BATS_3.0"):
    global loaded, root, files, tags
    if loaded:
        return
    root = path
    for path_to, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith('.txt'):
                ID = filename[:3] ####### change if needed
                tag = re.search(r"\[(.*?)\]", filename)[1]
                files[tag] = os.path.join(path_to, filename)
                tags[ID] = tag
    loaded = True

def load_file(id_or_tag, return_first_only=True):
    """Format of the file: (<word>\t<analogy1>(/<analogy>)*\n)*"""
    if not loaded: raise Exception("Dataset not loaded.")
    if id_or_tag in tags:
        id_or_tag = tags[id_or_tag]

    with open(files[id_or_tag]) as stream:
        s = stream.readlines() # split into lines
    s = map(lambda ln : ln.split('\t'), s) # split each line by \t
    
    if return_first_only:
        return [ ( ln[0], ln[1].split('/')[0].strip() ) for ln in s]
    else:
        s = map
        return [ [ ln[0], [word.strip() for word in ln[1].split('/')] ] for ln in s]

def _examples_to_question(example, query_answer, first_only=True):
    return (tuple(example), query_answer[0]), query_answer[1]

def get_question(fid=None):
    if not loaded: raise Exception("Dataset not loaded.")
    if fid is None:
        fid = choice(list(files))
    return _examples_to_question(*sample(load_file(fid), 2))

def get_all_questions(fid=None):
    if not loaded: raise Exception("Dataset not loaded.")
    if fid is None:
        questions = []
        for fid in files:
            questions.extend(get_all_questions(fid))
        return questions
    else:
        examples = load_file(fid)
        questions = []
        while True:
            if len(examples) <= 1: break
            example_idx = choice(range(len(examples)))
            example = examples.pop(example_idx)
            question_idx = choice(range(len(examples)))
            question = examples.pop(question_idx)
            questions.append( _examples_to_question(example, question) )
        return questions

def print_tags():
    if not loaded:
        raise Exception("Dataset not loaded.")
    for ID, tag in tags.items():
        print(f"{ID}: {tag}")
