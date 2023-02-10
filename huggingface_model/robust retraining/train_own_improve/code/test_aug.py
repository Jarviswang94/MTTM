import csv

test_texts = []
test_labels = []

f = open('ft_local/sent_benign.txt')
lines = f.readlines()
f.close()

for line in lines:
    test_texts.append(line)
    test_labels.append(0)


from transformers import DistilBertTokenizerFast
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

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

test_dataset = IMDbDataset(test_encodings, test_labels)

from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("results_aug/checkpoint-2500", num_labels=2)

from transformers import TrainingArguments

training_args = TrainingArguments("test_trainer")

from transformers import Trainer

trainer = Trainer(
    model=model, args=training_args, train_dataset=test_dataset, eval_dataset=test_dataset
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
    train_dataset=test_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics,
)
print(trainer.evaluate())

