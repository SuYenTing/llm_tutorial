# LangChain搭配streamlit範例
# 程式執行指令 `streamlit run chat_app.py``
import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain.memory import ConversationBufferMemory

# 初始化模型
@st.cache_resource
def get_model():
    return init_chat_model("gemma3:1b", model_provider="ollama")

llm = get_model()

# 初始化記憶體
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="history",
    )

# 對話函式
def ask(input_text):
    memory = st.session_state.memory
    history = memory.chat_memory.messages
    messages = history + [HumanMessage(content=input_text)]
    response = llm.invoke(messages)
    memory.chat_memory.add_user_message(input_text)
    memory.chat_memory.add_ai_message(response.content)
    return response.content

# Streamlit 介面
st.title("💬 LangChain + Ollama Chatbot")

# 顯示對話歷史
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for i, (user, bot) in enumerate(st.session_state.chat_history):
    st.markdown(f"**🧑 你:** {user}")
    st.markdown(f"**🤖 AI:** {bot}")

# 輸入框
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("請輸入你的訊息：", key="input")
    submitted = st.form_submit_button("送出")
    if submitted and user_input:
        response = ask(user_input)
        st.session_state.chat_history.append((user_input, response))
        st.rerun()
