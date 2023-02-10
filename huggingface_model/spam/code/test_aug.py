import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("mrm8488/bert-tiny-finetuned-sms-spam-detection")

model = AutoModelForSequenceClassification.from_pretrained("mrm8488/bert-tiny-finetuned-sms-spam-detection")

f = open('../data/augmented/sent_benign.txt')
lines = f.readlines()
f.close()

lines_new = []
for line in lines:
  input = tokenizer(line, return_tensors="pt")
  output = torch.argmax(model(**input).logits[0]).item()
  if output == 1:
    print(line)
    lines_new.append(line)

f = open('../data/fail/sent_benign.txt', 'w')
f.writelines(lines_new)
f.close()
