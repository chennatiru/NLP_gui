import json
import sys

sample_questions=[]
i=0
with open('commonsense_qa/train_rand_split.jsonl') as json_file:
  
  for line in json_file.read().split('\n'):
    if(line!=''):
        if(i<=5):
            
            i=i+1
            qapiece = json.loads(line)
            # q_text = qapiece['question']['stem']
            actual_answer = qapiece['answerKey']
            qa_texts = [qapiece['question']['stem']]
            for j in range(5):
                a_text = qapiece['question']['choices'][j]['text']
                a_option = qapiece['question']['choices'][j]['label']
                qa_texts.append(a_text)
            sample_questions.append(qa_texts)
        else:
            break
d = {
    "key_f":sample_questions
  }
print(json.dumps(d))