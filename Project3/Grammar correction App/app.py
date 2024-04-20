import torch
from transformers import BertTokenizer, BertForMaskedLM
import streamlit as st

# Load the fine-tuned model and tokenizer from Google Drive
output_dir = "fine_tuned_bert_model"
model = BertForMaskedLM.from_pretrained(output_dir)
tokenizer = BertTokenizer.from_pretrained(output_dir)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define function for inference
def correct_sentence(input_sentence):
    # Tokenize input sentence
    tokenized_input = tokenizer(input_sentence, return_tensors='pt', padding=True, truncation=True)
    tokenized_input = {key: value.to(device) for key, value in tokenized_input.items()}

    # Perform inference
    outputs = model(**tokenized_input)
    predicted_ids = torch.argmax(outputs.logits[0], dim=-1)
    predicted_sentence = tokenizer.decode(predicted_ids, skip_special_tokens=True)

    # Capitalize the first letter of each sentence
    predicted_sentence = '. '.join(map(str.capitalize, predicted_sentence.split('. ')))

    return predicted_sentence

# Streamlit app
st.title("Grammar Correction")

# Input text area for user to enter a sentence
user_input = st.text_area("Enter a sentence to correct")

# Button to perform correction
if st.button("Correct"):
    if user_input.strip():
        corrected_sentence = correct_sentence(user_input)
        st.write("Corrected Sentence:", corrected_sentence)
    else:
        st.write("Please enter a sentence for correction")
