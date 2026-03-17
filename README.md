# 🧠 AI Student Assistant

A Streamlit-based AI app that helps students with **chatting, translation, and Python code generation**.  
Perfect for learning, homework help, and coding practice.

---

## Features

- **AI Chat:** Ask questions and get answers from an AI model.  
- **Translator:** Translate text between multiple languages (English, Hindi, Tamil, French).  
- **Python Code Generator:** Describe Python code you want, and get clean, ready-to-use code.  

---

## Demo

Here are screenshots of the AI Student Assistant app:

![Chat Tab](images/screenshot1.png)  
*AI Chat feature*

![Translator Tab](images/screenshot3.png)  
*Translator feature*

![Code Generator Tab](images/screenshot2.png)  
*Python Code Generator feature*

---

## How to Use

> **Note:** Visitors cannot run the app directly on GitHub.  
> To see it live, the project should be deployed on **Streamlit Cloud** or **Hugging Face Spaces**.

1. You can browse the code files (`app.py`, notebooks) to see how it works.  
2. Check the screenshots above to understand each feature.  

---

## Folder Structure


AI_assistant_Notebook/
│
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── README.md # This file
├── images/ # Screenshots of the app
│ ├── screenshot1.png
│ ├── screenshot2.png
│ └── screenshot3.png
└── notebooks/ # Jupyter notebooks for testing
└── ai_student_assistant.ipynb


---

## Dependencies (for local use)

- `streamlit`
- `transformers`
- `torch`
- `deep-translator`

Install all with:

```bash
pip install -r requirements.txt
