import streamlit as st
import google.generativeai as genai


#configure your Gemini API Key
genai.configure(api_key="AIzaSyDABqHCmisrnk98UCRYiXL_xIcOZwwS_P4")

# Load the model
model=genai.GenerativeModel("gemini-2.5-flash-preview-04-17")


#Streamlit app layout
st.set_page_config(page_title="Gemini AI",layout="centered")


st.title("Gemini AI")
st.write("Ask any question and get a simple explanation!")

#User input
user_input=st.text_input("Enter your question:")


#Button to generate response
if st.button("Generate Answer"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response=model.generate_content(user_input)
                st.success("Here the answer:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error:{e}")
                
 # Display information about the model
st.write("Built model by Vamshikrishna!")


      
                
