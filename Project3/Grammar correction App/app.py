import torch
from transformers import BertTokenizer, BertForMaskedLM
import streamlit as st

# Loading the fine-tuned model and tokenizer 
output_dir = "fine_tuned_bert_model"
model = BertForMaskedLM.from_pretrained(output_dir)
tokenizer = BertTokenizer.from_pretrained(output_dir)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def correct_sentence(input_sentence):
    # Tokenize input sentence
    tokenized_input = tokenizer(input_sentence, return_tensors='pt', padding=True, truncation=True)
    tokenized_input = {key: value.to(device) for key, value in tokenized_input.items()}
    outputs = model(**tokenized_input)
    predicted_ids = torch.argmax(outputs.logits[0], dim=-1)
    predicted_sentence = tokenizer.decode(predicted_ids, skip_special_tokens=True)
    predicted_sentence = '. '.join(map(str.capitalize, predicted_sentence.split('. ')))
    return predicted_sentence

st.title("Grammar Correction")

user_input = st.text_area("Enter a sentence to correct")

if st.button("Correct"):
    if user_input.strip():
        corrected_sentence = correct_sentence(user_input)
        st.write("Corrected Sentence:", corrected_sentence)
    else:
        st.write("Please enter a sentence for correction")
