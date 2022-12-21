from sys import argv
from random import shuffle

class Question:
    def __init__(self, question, answer, subject, unit):
        self.question = question
        self.answer = answer
        self.subject = subject
        self.unit = unit
    
    def formatted_question(self):
        return f"{self.subject} - {self.question}"

def format_questions(lines):
    questions = []
    unit = ""
    subject = ""
    for line in lines:
        if line.strip() == "":
            continue
        elif line[0] == "*":
            unit = line[1:].strip()
        elif line[0] == "#":
            subject = line[1:].strip()
        else:
            try:
                q = line.split(": ", 1)
                questions.append(Question(q[0].strip(), q[1].strip(), subject, unit))
            except:
                print(f"Error: Could not format {line}")
    return questions

def question_loop(qs):
    num = len(qs)
    res = []
    for i in range(num):
        q = qs[i]
        print(f"({str(i+1)}/{str(num)}):", end=" ")
        input(q.formatted_question())
        print(q.answer)
        x = input()
        if x == 'q':
            break
        elif len(x) == 0:
            res.append(q)
    return res

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python study.py <filepath>")
        exit(1)
    
    lines = []
    for path in argv[1:]:    
        try:
            f = open(path, 'r')
        except:
            print(f"Could not find file '{path}'")
            exit(1)
        lines += f.readlines()
    qs = format_questions(lines)

    running = True
    while running:
        shuffle(qs)
        qs = question_loop(qs)

        if len(qs) == 0:
            print("All questions complete, aborting")
            running = False
        else:
            x = ''
            while x != "y" and x != "n":
                x = input("Shuffle and try again? (y/n):  ")
