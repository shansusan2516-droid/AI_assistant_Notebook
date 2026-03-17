import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from deep_translator import GoogleTranslator

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# ---------------- HELPER FUNCTIONS ----------------
def generate_response(prompt, max_length=200):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def translate_text(text, target_language="en"):
    return GoogleTranslator(source='auto', target=target_language).translate(text)

def generate_code(prompt):
    code_prompt = f"You are an expert Python developer. Generate clean Python code only.\n{prompt}"
    return generate_response(code_prompt)

# ---------------- UI ----------------
st.set_page_config(page_title="AI Student Assistant", layout="wide")
st.title("🧠 AI Student Assistant")

tab1, tab2, tab3 = st.tabs(["Chat", "Translator", "Code Generator"])

# -------- CHAT --------
with tab1:
    user_input = st.text_input("Ask something:")
    if st.button("Send"):
        if user_input:
            reply = generate_response(user_input)
            st.write(reply)

# -------- TRANSLATOR --------
with tab2:
    text_to_translate = st.text_area("Enter text:")
    target_lang = st.selectbox("Select language", ["en", "hi", "ta", "fr"])
    if st.button("Translate"):
        if text_to_translate:
            translated = translate_text(text_to_translate, target_lang)
            st.write(translated)

# -------- CODE GENERATOR --------
with tab3:
    code_prompt_input = st.text_area("Describe the Python code you want:")
    if st.button("Generate Code"):
        if code_prompt_input:
            code_output = generate_code(code_prompt_input)
            st.code(code_output, language="python")