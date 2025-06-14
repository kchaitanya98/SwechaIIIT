# import streamlit as st
# from transformers import pipeline

# # Configure Streamlit theme
# st.set_page_config(
#     page_title="AgriChat Assistant",
#     page_icon="🌱",
#     layout="wide"
# )

# # Title and subtitle
# st.title("🌾 AgriChat Assistant")
# st.markdown("Your friendly AI assistant for agriculture-related questions.")

# # Load the model
# @st.cache_resource
# def load_chatbot():
#     return pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")

# chatbot = load_chatbot()

# # Chat Interface
# user_input = st.text_input("Ask me anything about agriculture...", "")

# if user_input:
#     with st.spinner("Thinking..."):
#         response = chatbot(f"<s>[INST] {user_input} [/INST]")[0]['generated_text']
#         st.success(response.split("[/INST]")[-1].strip())










import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="Agri Assistant", layout="wide")
st.title("🌾 Agri Assistant Chat")

st.markdown("Interact with your intelligent agriculture assistant powered by Hugging Face.")

# Embed the chatbot using iframe
chat_url = "https://hf.co/chat/assistant/684d3d8bd0429a815fad8079"
components.iframe(chat_url, height=800, scrolling=True)


st.markdown("Not Working ? check in below..")

st.markdown(
    f"""
    <div style="text-align: center; margin-top: 3rem;">
        <a href="{chat_url}" target="_blank">
            <button style="
                background-color: #228B22;
                color: white;
                padding: 14px 30px;
                font-size: 18px;
                border: none;
                border-radius: 8px;
                cursor: pointer;">
                🌿 Launch AgriChat Assistant
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)