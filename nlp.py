import json


d = {
    "key_f":[]
  }
c=0
with open('nlp_que_small.jsonl') as json_file:
  
  for line in json_file.read().split('\n'):
    ekpiece = json.loads(line)
    # print(ekpiece["question"]["stem"])
    c+=1
    answer_key = ekpiece["answerKey"]
    ans = [c,ekpiece["question"]["stem"]]
    for a in ekpiece["question"]["choices"]:
    
      ans.append(a["text"])
    d["key_f"].append(ans)


print(json.dumps(d))