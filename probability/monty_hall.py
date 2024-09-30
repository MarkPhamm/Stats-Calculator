import streamlit as st
import random
import matplotlib.pyplot as plt
import time

def monty_hall_simulation(num_simulations):
    switch_wins = []
    stay_wins = []
    switch_count = 0
    stay_count = 0
    
    for i in range(num_simulations):
        # Set up the game
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)
        
        # Player's initial choice
        player_choice = random.randint(0, 2)
        
        # Monty opens a door
        monty_opens = next(i for i in range(3) if i != player_choice and doors[i] == 'goat')
        
        # Switch strategy
        switch_choice = next(i for i in range(3) if i != player_choice and i != monty_opens)
        
        # Count wins
        if doors[switch_choice] == 'car':
            switch_count += 1
        if doors[player_choice] == 'car':
            stay_count += 1
        
        switch_wins.append(switch_count / (i + 1))
        stay_wins.append(stay_count / (i + 1))
    
    return switch_wins, stay_wins

def main():
    st.title("Monty Hall Problem Simulation")
    
    st.write("""
    The Monty Hall problem is a famous probability puzzle. Here's how it works:

    1. There are three doors. Behind one door is a car, and behind the other two are goats.
    2. You pick a door, say door 1.
    3. The host, who knows what's behind the doors, opens another door, say door 3, which has a goat.
    4. The host then asks you: do you want to switch to door 2, or stay with door 1?

    The question is: Is it to your advantage to switch your choice?
    """)

    st.subheader("Simulation")
    num_simulations = 2500
    
    # Create a placeholder for the plot
    plot_placeholder = st.empty()
    
    # Create a button to run the simulation
    if st.button("Run Simulation"):
        switch_wins, stay_wins = monty_hall_simulation(num_simulations)
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(10, 6))
        line_switch, = ax.plot([], [], label='Switch')
        line_stay, = ax.plot([], [], label='Stay')
        ax.set_xlabel('Number of Simulations')
        ax.set_ylabel('Win Probability')
        ax.set_title('Monty Hall Simulation Results Over Time')
        ax.legend()
        ax.grid(True)
        ax.set_xlim(0, num_simulations)
        ax.set_ylim(0, 1)
        
        # Animate the plot
        for i in range(1, num_simulations + 1, 100):  # Update every 100 simulations
            line_switch.set_data(range(1, i + 1), switch_wins[:i])
            line_stay.set_data(range(1, i + 1), stay_wins[:i])
            plot_placeholder.pyplot(fig)
        
        st.write(f"After {num_simulations} simulations:")
        st.write(f"Switching won {switch_wins[-1]:.2%} of the time")
        st.write(f"Staying won {stay_wins[-1]:.2%} of the time")
        
        st.subheader("Explanation")
        st.write("""
        The simulation demonstrates that switching doors gives you a 2/3 chance of winning, while staying with your original choice gives you a 1/3 chance.

        Here's why:

        1. Initially, you have a 1/3 chance of choosing the car and a 2/3 chance of choosing a goat.
        2. If you chose a goat (2/3 chance), Monty will always open the other goat door, leaving the car behind the unopened door. Switching in this case wins.
        3. If you chose the car (1/3 chance), Monty opens either goat door, and switching in this case loses.

        Therefore:
        - Probability of winning by switching = Probability of initially choosing a goat = 2/3
        - Probability of winning by staying = Probability of initially choosing the car = 1/3

        This counterintuitive result is why the Monty Hall problem is so famous in probability theory.
        """)

if __name__ == "__main__":
    main()
