import streamlit as st

def set_background_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f2f6;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    set_background_color()
    st.title("🌱 Growth Mindset Quiz 🎯")
    st.write("Answer these questions to see if you have a Growth Mindset or a Fixed Mindset!")
    
    # Quiz Questions
    questions = [
        ("When you face a tough problem, what do you do?", ["Give up", "Keep trying and learn from mistakes"]),
        ("Do you believe intelligence can grow with effort?", ["No, it stays the same", "Yes, effort makes a difference"]),
        ("How do you handle failure?", ["I avoid challenges to prevent failing", "I see failure as a way to learn"]),
        ("When learning something new, do you...?", ["Stick to what I know", "Try new things even if I struggle"]),
        ("Do you like feedback/criticism?", ["No, it makes me feel bad", "Yes, it helps me improve"])
    ]
    
    score = 0
    
    # Ask each question
    for question, options in questions:
        answer = st.radio(question, options)
        if answer == options[1]:
            score += 1  # Growth mindset answer
    
    # Show Result
    st.subheader("Your Growth Mindset Score: " + str(score) + "/5")
    
    if score == 5:
        st.success("🌟 Amazing! You have a strong Growth Mindset. Keep learning and improving!")
    elif score >= 3:
        st.info("😊 Good job! You are developing a Growth Mindset. Keep practicing!")
    else:
        st.warning("🚀 You can grow more! Start embracing challenges and learning from mistakes.")
        
    st.write("Remember, learning never stops. Keep challenging yourself!")

if __name__ == "__main__":
    main()
