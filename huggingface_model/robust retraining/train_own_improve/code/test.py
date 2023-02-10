import csv
csv_reader = csv.reader(open("./labeled_data.csv"))

texts = []
labels = []

for line in csv_reader:
	sent = line[-1]
	label = line[-2]
	if label not in ['1', '2']:
		continue
	texts.append(sent)
	#0:offensive 1:benign
	labels.append(int(label)-1)

from sklearn.model_selection import train_test_split
train_texts, test_texts, train_labels, test_labels = train_test_split(texts, labels, test_size=.1)
train_texts, val_texts, train_labels, val_labels = train_test_split(train_texts, train_labels, test_size=.33)


from transformers import DistilBertTokenizerFast
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

train_encodings = tokenizer(train_texts, truncation=True, padding=True)
val_encodings = tokenizer(val_texts, truncation=True, padding=True)
test_encodings = tokenizer(test_texts, truncation=True, padding=True)


import torch

class IMDbDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = IMDbDataset(train_encodings, train_labels)
val_dataset = IMDbDataset(val_encodings, val_labels)
test_dataset = IMDbDataset(test_encodings, test_labels)

from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("results/checkpoint-2000", num_labels=2)

from transformers import TrainingArguments

training_args = TrainingArguments("test_trainer")

from transformers import Trainer

trainer = Trainer(
    model=model, args=training_args, train_dataset=train_dataset, eval_dataset=test_dataset
)

import numpy as np
from datasets import load_metric

metric = load_metric("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics,
)
print(trainer.evaluate())

