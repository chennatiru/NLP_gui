import json
import sys
# import os
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"


# num_input = int(sys.argv[1])

d={
  "asd":[]
}
i = 0

with open('commonsense_qa/dev_rand_split.jsonl') as json_file:

  for line in json_file.read().split('\n'):
      if(line != ''):
          i = i+1
          # if(i == num_input):
          qapiece = json.loads(line)
          q_text = qapiece['question']['stem']
          actual_answer = qapiece['answerKey']
          qa_texts = [q_text]
          for j in range(5):
              a_text = qapiece['question']['choices'][j]['text']
            # a_option = qapiece['question']['choices'][i]['label']
            # if(a_option==answer):
            #   train_labels.append(i)
              qa_texts.append(a_text)
          d["asd"].append(qa_texts)
print(json.dumps(d))


# import numpy as np
# import torch
# import pickle

# from sklearn.externals import joblib
# model= torch.load('cmsqa.pkl', map_location=lambda storage, location: storage)

# num_input = 4

# from transformers import XLNetTokenizer
# tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')

# i=0
# with open('cmsqa.jsonl') as json_file:
  
#   for line in json_file.read().split('\n'):
#     if(line!=''):
#     	i=i+1
#     	if(i==num_input):
# 		      qapiece = json.loads(line)
# 		      q_text = qapiece['question']['stem']
# 		      actual_answer = qapiece['answerKey']
# 		      qa_texts = []
# 		      for i in range(5):
# 		        a_text = qapiece['question']['choices'][i]['text']
# 		        a_option = qapiece['question']['choices'][i]['label']
# 		        # if(a_option==answer):
# 		        #   train_labels.append(i)
# 		        qa_texts.append((q_text, a_text))
# 		        break

# inputs=[]
# attentions=[]
# token_types=[]
# max_seq_length = 128
# for s in qa_texts:
#   q_tokens = tokenizer.tokenize(s[0])
#   a_tokens = tokenizer.tokenize(s[1])
#   qa_tokens = q_tokens+['<s>']+a_tokens+['<s>', '</s>']
#   t = [0]*(len(q_tokens)+1)+[1]*(len(a_tokens)+2)
#   qa_ids = []
#   a = []
#   for token in qa_tokens:
#     id = tokenizer._convert_token_to_id(token)
#     qa_ids.append(id)
#     a.append(1)
#   a = a + [0]*(max_seq_length - len(a))
#   t = t + [0]*(max_seq_length - len(t))
#   qa_ids = qa_ids + [0]*(max_seq_length - len(qa_ids))
#   inputs.append(qa_ids)
#   attentions.append(a)
#   token_types.append(t)
# # device=torch.device('cpu')
# # model = torch.load('cmsqa.pkl', map_location=)
# model.eval()
# model_output = model(input_ids=inputs, attention_mask=attentions, token_type_ids=token_types)
# logits = model_output[0]
# num_output= np.argmax(logits, axis=1).flatten()
# predicted_answer = qa_texts[num_output][1]
# print(predicted_answer, actual_answer)
