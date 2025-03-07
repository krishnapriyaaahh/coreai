import streamlit as st

# Define questions and survival impact
questions = [
    {
        "question": "You're home alone, and you hear a noise upstairs. What do you do?",
        "options": ["Investigate the noise", "Run outside", "Call a friend", "Hide under the bed"],
        "scores": [0, 10, 5, 2]
    },
    {
        "question": "You find a creepy diary in an abandoned house. Do you read it?",
        "options": ["Yes, what’s the worst that can happen?", "No, I leave immediately"],
        "scores": [0, 10]
    },
    {
        "question": "The villain is chasing you. Where do you hide?",
        "options": ["In a closet", "Under the bed", "Run into the forest", "Get into a car and drive away"],
        "scores": [2, 0, 5, 10]
    },
    {
        "question": "The power goes out. What do you use for light?",
        "options": ["A candle", "A flashlight", "My phone", "I stay in the dark"],
        "scores": [2, 10, 5, 0]
    }
]

# Streamlit UI
st.title("Would You Survive in a Thriller Movie? 🎬🔪")
st.write("Answer these questions and find out if you’d make it out alive!")

# Initialize session state
if "total_score" not in st.session_state:
    st.session_state.total_score = 0
if "answered" not in st.session_state:
    st.session_state.answered = [None] * len(questions)

# Loop through questions
for i, q in enumerate(questions):
    choice = st.radio(q["question"], q["options"], index=st.session_state.answered[i])
    
    if choice:
        st.session_state.answered[i] = q["options"].index(choice)
        st.session_state.total_score = sum(
            q["scores"][st.session_state.answered[j]] if st.session_state.answered[j] is not None else 0
            for j, q in enumerate(questions)
        )

# Show result only if all questions are answered
if None not in st.session_state.answered:
    st.subheader(f"Your Survival Score: {st.session_state.total_score}")

    if st.session_state.total_score >= 30:
        st.success("🎉 You survive! You're the final protagonist!")
    elif 15 <= st.session_state.total_score < 30:
        st.warning("😨 You barely make it. Maybe a sequel?")
    else:
        st.error("☠️ You're the first to die. Horror movies aren't for you.")

