"""
Zero-Shot Text Classification
https://huggingface.co/facebook/bart-large-mnli
NLI-based Zero Shot Text Classification
"""

#load the zero-shot-classification pipeline
from transformers import pipeline
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

#create array named label_array
label_array = []
#request number of labels from user
array_n = int(input("Enter number of labels to use: \n"))
#request each label from user and put them into label_array
for i in range(0, array_n):
    labelname = input("Input label for use: \n")
    label_array.append(labelname)

#request a sequence to be zero shot classified
sequence_to_classify = input("Input a sequence/sentence to zero shot classify: \n")
#If more than one candidate label can be correct, pass multi_class=True to calculate each class independently
if str.upper(input("Do you want to use multi labeling? y/n \n")) == "Y":
    mlabelbool = True
else:
    mlabelbool = False

classifier(sequence_to_classify, label_array, multi_label=mlabelbool)
