import json
import sys

num_input = int(sys.argv[1])

i=0
with open('commonsense_qa/dev_rand_predictions.txt') as text_file:
  
  for line in text_file.read().split('\n'):
    if(line!=''):
    	i=i+1
    	if(i==num_input):
            pred = json.loads(line)
            pred=int(pred)
            break
i=0
with open('commonsense_qa/dev_rand_split.jsonl') as json_file:
  
  for line in json_file.read().split('\n'):
    if(line!=''):
    	i=i+1
    	if(i==num_input):
            qapiece = json.loads(line)
            q_text = qapiece['question']['stem']
            actual_option = qapiece['answerKey']
            predicted_answer = qapiece['question']['choices'][pred]['text']
            opt = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}
            actual_answer = qapiece['question']['choices'][opt[actual_option]]['text']


d={
  "ans":[ actual_answer,predicted_answer]
}

print(json.dumps(d))