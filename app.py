import streamlit as st

def main():
    #config for the app
    st.set_page_config(page_title="Chat with PDF")

    # setting conversation list in the session_state to keep chat history
    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    st.header("Chat with PDF")
    #sidebar for uploading the file
    with st.sidebar:
        st.subheader("Your documents")
        uploaded_docs = st.file_uploader("Upload or Drop your pdfs here", accept_multiple_files=True, type="pdf")
        st.button("Process")
    # display the conversation
    for message in st.session_state.conversation:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # getting the user input
    user_question = st.chat_input("What would you like to know?")
    # display the user question in the container
    if user_question:
        with st.chat_message("user"):
            st.markdown(user_question)
        # save the message to session chat history
        st.session_state.conversation.append({"role":"user","content": user_question})

        response = f"Your question: {user_question}"

        # display the assistant message
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.conversation.append({"role": "assistant", "content": response})

if __name__=="__main__":
    main()