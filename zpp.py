# Custom CSS for the slider
st.markdown(
    """
    <style>
    .stSlider > div {
        background-color: #FFFFFF;  /* Background color of the slider */
    }
    .stSlider input[type="range"] {
        -webkit-appearance: none;
        width: 100%;
        height: 15px;
        background: #ddd;  /* Slider track color */
        border-radius: 5px;
    }
    .stSlider input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 25px;
        height: 25px;
        border-radius: 50%;
        background: #FF6347;  /* Thumb color */
        cursor: pointer;
    }
    .stSlider input[type="range"]::-moz-range-thumb {
        width: 25px;
        height: 25px;
        border-radius: 50%;
        background: #FF6347;  /* Thumb color */
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)
'''
# Set custom styles
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;  /* Light background */
        color: #000000;  /* Text color */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #333333;  /* Header colors */
    }
    .stLabel {
        color: #000000;  /* Change label color to black */
        font-size: 18px;  /* Increase font size for input labels */
        font-weight: bold;  /* Make labels bold */
    }
    </style>
    """,
    unsafe_allow_html=True
)
'''