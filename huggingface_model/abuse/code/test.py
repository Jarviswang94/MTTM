import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Hate-speech-CNERG/bert-base-uncased-hatexplain")

model = AutoModelForSequenceClassification.from_pretrained("Hate-speech-CNERG/bert-base-uncased-hatexplain")

f = open('data/abuse/abuse.txt')
lines = f.readlines()
f.close()

lines_new = []
for line in lines:
  input = tokenizer(line, return_tensors="pt")
  output = torch.argmax(model(**input).logits[0]).item()
  if output == 2:
    print(line)
    lines_new.append(line)

f = open('data/abuse/abuse_filted.txt', 'w')
f.writelines(lines_new)
f.close()
