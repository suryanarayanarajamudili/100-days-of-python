
import random
import streamlit as st

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

st.title("✊ Rock, Paper, Scissors!")
st.write("Welcome to the childhood game. Let's get nostalgic!")

# Store scores between button clicks
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0

# Let the player choose
user_choice = st.radio(
    "What do you choose?",
    [0, 1, 2],
    format_func=lambda x: choices[x],
    horizontal=True
)

if st.button("Play!"):
    computer_choice = random.randint(0, 2)

    st.subheader(f"Your choice: {choices[user_choice]}")
    st.code(game_images[user_choice])

    st.subheader(f"Rocky: {choices[computer_choice]}")
    st.code(game_images[computer_choice])

    if user_choice == computer_choice:
        st.info("It's a draw!")

    elif (
        (user_choice == 0 and computer_choice == 2)
        or (user_choice == 1 and computer_choice == 0)
        or (user_choice == 2 and computer_choice == 1)
    ):
        st.success("You win! 🎉")
        st.session_state.user_score += 1

    else:
        st.error("You lose!")

    if user_choice != computer_choice:
        if (
            (computer_choice == 0 and user_choice == 2)
            or (computer_choice == 1 and user_choice == 0)
            or (computer_choice == 2 and user_choice == 1)
        ):
            st.session_state.computer_score += 1

st.subheader("Scoreboard")
st.write("Your wins:", st.session_state.user_score)
st.write("Computer wins:", st.session_state.computer_score)

if st.button("Reset scores"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.rerun()
