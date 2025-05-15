import streamlit as st
from src.defense.input_preprocessor import InputPreprocessor
from src.defense.output_filter import OutputFilter

# Initialize defense modules
preprocessor = InputPreprocessor()
filt = OutputFilter()

st.set_page_config(page_title="LLM Jailbreak Defense", layout="centered")
st.title("🛡️ LLM Jailbreak Defense Demo")

# User prompt input
user_input = st.text_area("Enter your prompt to the LLM:", height=150)

if st.button("Submit"):
    # Step 1: Sanitize input
    sanitized = preprocessor.sanitize_prompt(user_input)
    st.subheader("🔍 Sanitized Input")
    st.write(sanitized)

    # If blocked, stop here
    if "[BLOCKED PROMPT" in sanitized:
        st.warning("Prompt blocked due to unsafe content.")
    else:
        # Step 2: Simulated LLM response (placeholder for your model)
        # You can replace this with an actual call to your LLM
        llm_response = f"Simulated response for: {sanitized}"

        # Step 3: Filter the response
        safe_response = filt.filter_output(llm_response)

        st.subheader("💬 LLM Response (Filtered)")
        st.write(safe_response)
