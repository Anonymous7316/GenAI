from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from streamlit import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# UI setup
st.header("Research Tool")
paper_name = st.selectbox(
    "Select a paper",
    (
        "Select a paper",
        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "Attention Is All You Need",
        "Generative Pre-trained Transformer 3 (GPT-3): Language Models are Few-Shot Learners",
        "RoBERTa: A Robustly Optimized BERT Pretraining Approach",
        "XLNet: Generalized Autoregressive Pretraining for Language Understanding",
        "ALBERT: A Lite BERT for Self-supervised Learning of Language Representations",
        "T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer",
        "ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators",
        "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter",
    )
)
style_type = st.selectbox(
    "Select a style",
    (
        "Select a style",
        "Technical with code examples",
        "Technical with mathematical explanations",
        "Technical with visualizations",
        "Technical with detailed explanations",
        "Conversational with examples",
        "Conversational with analogies",
        "Conversational with storytelling",
        "Descriptive",
    )
)
length = st.selectbox(
    "Select the length of the response",
    (
        "Select length",
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (5+ paragraphs)",
    )
)

# Define the prompt template
prompt_template = load_prompt("Prompts/templates/research_paper_summary_template.json")

prompt = prompt_template.invoke(
    dict(
        paper_input=paper_name,
        style_input=style_type,
        length_input=length,
    )
)

# Initialize the model
model = ChatOpenAI()

if st.button("Generate Summary"):
    result = model.invoke(prompt)
    st.write(result.content)