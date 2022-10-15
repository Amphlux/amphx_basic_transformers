/*
amphx_basic_transformers
Super basic python transformer scripts using HuggingFace

Zero-Shot Text Classification
https://huggingface.co/facebook/bart-large-mnli
NLI-based Zero Shot Text Classification

Yin et al. proposed a method for using pre-trained NLI models as a ready-made zero-shot sequence classifiers. 
The method works by posing the sequence to be classified as the NLI premise and to construct a hypothesis 
from each candidate label. For example, if we want to evaluate whether a sequence belongs to the class "politics", 
we could construct a hypothesis of This text is about politics.. The probabilities for entailment and 
contradiction are then converted to label probabilities.

This method is surprisingly effective in many cases, particularly when used with larger pre-trained models 
like BART and Roberta. See this blog post for a more expansive introduction to this and other zero shot methods, 
and see the code snippets below for examples of using this model for zero-shot classification both with 
Hugging Face's built-in pipeline and with native Transformers/PyTorch code.
*/
