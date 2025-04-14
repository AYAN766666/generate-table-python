import streamlit as st


# Custom CSS using selectors


st.markdown("""
    <style>
        /* Title (st.title) */
        h1 {
            background: linear-gradient(to right, #00b4db, #0083b0);
            -webkit-background-clip: text;
            color: transparent;
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            padding: 10px;
        }

        /* Header (st.header) */
        h2 {
            background: linear-gradient(to right, #ff9068, #fd746c);
            -webkit-background-clip: text;
            color: transparent;
            font-size: 28px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 20px;
        }

        /* Text input field */
        .stTextInput > div > div > input {
            font-size: 18px;
            padding: 10px;
            border: 2px dashed #ff7eb3;
            border-radius: 12px;
            background-color: #fff0f5;
            color: #4b0082;
            box-shadow: 2px 2px 8px rgba(255, 126, 179, 0.3);
        }

        /* Table output (colorful lines) */
        .stMarkdown > div {
            background: linear-gradient(to right, #d9a7c7, #fffcdc);
            padding: 15px;
            border-radius: 12px;
            font-family: 'Courier New', monospace;
            font-size: 20px;
            color: #3e3e3e;
            margin-top: 20px;
            line-height: 2;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }

        /* Styling each line in the table */
        .stMarkdown > div > p:nth-child(odd) {
            color: #ff1493;
            font-weight: bold;
        }

        .stMarkdown > div > p:nth-child(even) {
            color: #007acc;
            font-weight: bold;
        }

        /* Error message styling */
        .stAlert {
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            color: white;
            padding: 14px;
            border-left: 6px solid #8b0000;
            border-radius: 8px;
            font-weight: bold;
            box-shadow: 2px 2px 12px rgba(255, 126, 179, 0.3);
        }
    </style>
""", unsafe_allow_html=True)



try:
    st.title("Welcome to Number Tabile App")
    st.header("🔠 Type a Number, Get the Tale")
    name = st.text_input("Enter Your Number")  # Input for number
    
    if name:  # Check if the user has entered something
        name = int(name)  # Convert to integer
    
    for i in range(1, 11):  # Corrected range from 1 to 10
        st.write(f"{i} x {name} = {i * name}")
except ValueError:
    st.error("❌ Please enter a valid integer!")