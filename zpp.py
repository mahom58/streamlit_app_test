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