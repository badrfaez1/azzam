import streamlit as st

# Custom CSS with enhanced animations
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Ubuntu:400,400i,700,700i');

    /* Base styles */
    *, *:before, *:after {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    /* Enhanced Heart styles */
    .heart {
        color: red;
        font-size: 80px;
        text-align: center;
        cursor: pointer;
        transition: transform 0.3s ease;
        animation: heartbeat 1.5s infinite;
    }

    .heart:hover {
        transform: scale(1.2);
    }

    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }

    /* Text styles */
    .text {
        font-size: 36px;
        text-align: center;
        color: #ffffff;
        margin: 20px 0;
        font-family: 'Ubuntu', sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* Enhanced Candle styles */
    .candle {
        width: 40px;
        height: 150px;
        position: relative;
        margin: 100px auto;  /* Increased top margin to accommodate flame */
        background: linear-gradient(#e48825, #e78e0e, #833c03, #4c1a03 50%, #1c0900);
        border-radius: 10px;
    }

    /* Enhanced Flame styles */
    .flame {
        width: 24px;
        height: 80px;
        position: absolute;
        left: 50%;
        transform-origin: 50% 100%;
        transform: translateX(-50%);
        bottom: calc(100% - 10px);  /* Adjusted to overlap slightly with candle */
        border-radius: 50% 50% 20% 20%;
        background: rgba(255, 255, 255, 0.95);
        background: linear-gradient(
            rgba(255, 255, 255, 0.95) 60%,
            rgba(255, 223, 136, 0.95) 80%,
            transparent 100%
        );
        animation: moveFlame 6s linear infinite, enlargeFlame 5s linear infinite;
        z-index: 2;  /* Ensure flame appears above glow */
    }

    /* Enhanced Glow styles */
    .glow {
        width: 26px;
        height: 60px;  /* Increased height */
        border-radius: 50% 50% 35% 35%;
        position: absolute;
        left: 50%;
        bottom: calc(100% - 15px);  /* Positioned relative to bottom of candle */
        transform: translateX(-50%);
        background: rgba(255, 147, 36, 0.4);
        box-shadow: 
            0 -40px 30px 0px rgba(255, 147, 36, 0.4),
            0 40px 50px 0px rgba(255, 147, 36, 0.4),
            inset 3px 0 2px 0 rgba(255, 147, 36, 0.3),
            inset -3px 0 2px 0 rgba(255, 147, 36, 0.3);
        animation: glowPulse 2s ease-in-out infinite;
        z-index: 1;  /* Below flame but above candle */
    }

    /* Names animation */
    .names {
        font-size: 24px;
        color: white;
        opacity: 0;
        transition: opacity 0.5s ease;
        margin-top: 20px;
    }

    .names.visible {
        opacity: 1;
    }

    /* Button styles */
    .stButton button {
        background: linear-gradient(45deg, #ff4b4b, #ff1c1c);
        color: white;
        font-size: 20px;
        padding: 15px 30px;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        transition: transform 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
    }

    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.4);
    }

    @keyframes moveFlame {
        0%, 100% { transform: translateX(-50%) rotate(-2deg); }
        50% { transform: translateX(-50%) rotate(2deg); }
    }

    @keyframes enlargeFlame {
        0%, 100% { height: 80px; width: 24px; }
        50% { height: 90px; width: 26px; }
    }

    @keyframes glowPulse {
        0%, 100% { opacity: 0.4; transform: translateX(-50%) scale(1); }
        50% { opacity: 0.6; transform: translateX(-50%) scale(1.1); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main_page():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.markdown(
            """
            <div class="candle">
                <div class="flame"></div>
                <div class="glow"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="heart" onclick="document.querySelector('.names').classList.toggle('visible')">❤️</div>
            <div class="names">Azzam + Wife</div>
            <div class="text">Azzam is looking for a wife</div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="candle">
                <div class="flame"></div>
                <div class="glow"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("Help Azzam Find His Wife! 💝"):
        st.session_state.page = "silly_questions"
        st.rerun()


def silly_questions():
    st.title("Help Azzam Find His Wife! 😊")
    st.write("Answer these silly questions to help Azzam:")

    q1 = st.radio("1. What qualities should Azzam look for in a wife?",
                  ["Piety and Good Character", "Strong Family Values", "Knowledge of Deen", "All of the above"])

    q2 = st.selectbox("2. What's most important for a blessed marriage?",
                      ["Mutual respect and understanding", "Strong Islamic foundation", "Family support", "Good communication"])

    q3 = st.text_input("3. What advice would you give for a successful Islamic marriage?")

    q4 = st.slider("4. How many children would you ask Allah to bless them with?", 0, 10, 2)

    if st.button("Submit Your Answers 💖"):
        st.balloons()
        st.success("Thanks for helping Azzam find love! 🎉")
        if st.button("Start Over 🔄"):
            st.session_state.page = "main_page"
            st.rerun()


# Page navigation
if "page" not in st.session_state:
    st.session_state.page = "main_page"

if st.session_state.page == "main_page":
    main_page()
elif st.session_state.page == "silly_questions":
    silly_questions()