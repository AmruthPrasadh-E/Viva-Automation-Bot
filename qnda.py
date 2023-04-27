import random
import pyttsx3
from ans_key import *
from score_module import *


engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(txt):
    engine.say(txt)
    engine.runAndWait()

# Define a list of questions and their answers
question_bank = {

    # "Can you describe the steps you would take when assessing a patient's condition?":['patient', 'condition', 'information', 'symptoms', 'history', 'exam', 'signs', 'illness', 'injury', 'situation', 'tests', 'blood', 'work', 'imaging', 'scans', 'knowledge', 'diagnosis', 'treatment', 'plan'],
    # "Can you describe some common exercises or techniques you use to help patients with movement or daily tasks?":['exercises', 'techniques', 'patient', 'condition', 'goals', 'example', 'range', 'motion', 'exercises', 'strength', 'training', 'movement', 'patients', 'strategies', 'devices', 'tasks'],
    # "Can you explain the basics of medical ethics, and how they apply to your job in healthcare?":['ethics', 'set', 'principles', 'healthcare', 'professionals', 'decisions', 'interests', 'patients', 'principles', 'respect', 'autonomy', 'harm', 'beneficence', 'patient', 'interests', 'principles', 'job', 'care', 'patients']
    "What is a Stack?": ['stack', 'data', 'structure', 'collection', 'elements', 'order', 'Elements', 'end', 'stack'], 
    #"What is a postfix expression?": ['expression', 'operators', 'operands', 'postfix', 'expression', 'benefit', 'form', 'need', 'group', 'sub', 'expressions', 'parentheses', 'operator', 'precedence', 'expression', '+', 'b', 'ab+', 'postfix', 'notation'],
    "Define the tree data structure.":['tree', 'data', 'structure', 'nodes', 'edges', 'node', 'child', 'nodes', 'relationships', 'computer', 'science', 'data', 'way', 'search', 'insertion', 'operations'],
    "What is the capital of France?": ["capital", "France","Paris"],
    #"What is the highest mountain in the world?": ["highest","mountain", "world", "Mount", "Everest"],
    #"What is the smallest country in the world?": ["smallest","country", "world","Vatican","City"],
    # "What is the largest ocean in the world?": ["largest ocean", "world","Pacific","ocean"],
    # "Who painted the Mona Lisa?": ["painted", "Mona Lisa","Leonardo","da","vinci"],

    
    # "What is the currency of Japan?": ["currency", "Japan","Yen"],
    # "What is the most spoken language in the world?": ["most spoken language", "world","Chinese"],
    # "Who invented the telephone?": ["invented", "telephone", "Alexander","Grahambell"],
    # "What is the largest continent in the world?": ["largest continent", "world","Asia"]
}

# Set the number of questions to generate
i=1

# Shuffle the question bank
temp = list(question_bank.items())
random.shuffle(temp)
test = dict(temp)

# Print the randomly selected questions with answer keywords+
for k,v in test.items():
    print(f"Question {i}: {k}")
    talk(k)
    # time.sleep(5)   #insert test_audkey.py file
    keyword_extract()
    keys_in_A = return_keywords()   #returns list
    print(f"Answer key Phrases: '{v}'")
    kcount = Keyword_count(v, keys_in_A)
    kQ = len(v)

    score = candidate_score(kQ, kcount)
    print("Score for the Ans:", score)
    print()
    i = i+1