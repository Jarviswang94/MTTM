# MTTM Artifact

This is the artifact of paper MTTM: Metamorphic Testing for Textual Content Moderation Software.

Besides this zip file, we also build a demo page on http://ariselab.cse.cuhk.edu.hk/projects.html.

## Files Introduction
------
Our folder includes five folders: google, huawei, baidu, huggingface_model and pilot_study.

## google, huawei and baidu
These three folders contain the data, code and results for corresponding commercial software. 

In each folder, there are three sub-folders: 

* code

    including the code of calling API (`./[software]/code/call_aug.py`) and implement perturbation (`./[software]/code/augment.py`). 

    Since calling API need user name and password that contains personal information which may volent the double blind submission policy, we delete those kind of information. If reviewers are insterested to run our code, please go to API's websites (listed in our paper) to register. And then fill the missing token.

* data
    
    this folder contains different task folders that containing the data of original data（`./[software]/data/[task]/[task].txt`), the data that detected by commersial software (`./[software]/data/[task]/[task]_filted.txt`), the perturbed data (`./[software]/data/[task]/augmented/[perturb_method].txt`) and the perturbed data that can/cannot bypass the filter (`./[software]/data/[task]/result/[perturb_method].txt`).

* rules

    this folder contains different task folders that containing the perturbation dictionaries generated with differnet MRs. For example the substitution dictionary generated by char-level masking for google abuse detection is `./google/rules/char_mask.txt`.

## huggingface_model
This folder contains the data, code and results of the research model tested in our paper (`./huggingface_model/abuse/` and `./huggingface_model/spam/`). It also contains the code of training model and robust retraining model (`./huggingface_model/train_own/` and `./huggingface_model/train_own_improve/`, respectively)

## pilot_study

This folder contains the collection of our annotation to real world Internet users data (`./pilot_study/all.csv`).

## human_eval
This folder contains the code (`./human_eval/code/[question].py`) and results of human evaluation (`./human_eval/results/[dataset]/[perturb_method]/[question].txt`).


----
## Getting started

This instruction will let you run MTTM on your local machine for development and testing purposes.

### Prerequisites and Installing

1. Register and get the API token from the official website of commercial content moderation softwares.
2. python 3.6+
3. transformer. It can be installed using pip as follows:

    `pip install transformers`

### Run the code
This section explain how to run MTTM. 

You can  call google abuse detection with the following code:
    
` python ./google/code/call.py `

If you want to make word level perturbation to google abuse dataset, you can first edit `./google/code/word_augment.py` to set what kinds of perturbation you want and the address of the generated perturbed sentence. Then you can run the following code:

` python ./google/code/word_augment.py `

Then you can call API again to test the generated perturbed sentence by edit `./google/code/call_aug.py` to input the address of the generated perturbed sentence and then run the following code:

` python ./google/code/call_aug.py `



