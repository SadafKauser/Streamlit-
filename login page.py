

import streamlit as st
import datetime

# Function to check the login credentials
def check_credentials(username, password):
    return username == 'admin' and password == 'password'

# Main function for the Streamlit app
def main():
    st.title("Login Page")

    # Text input for username
    username = st.text_input("Username")

    # Password input for password
    password = st.text_input("Password", type='password')

    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Check if the user is already logged in
    if st.session_state.logged_in:
        st.success("Welcome, {}!".format(st.session_state.username))
        st.balloons()  # Display balloons upon successful login
        
        # Date input widget
        selected_date = st.date_input("Select a date", datetime.date.today())
        
        # Time input widget
        selected_time = st.time_input("Select a time", datetime.datetime.now().time())
        
        # Button to confirm the date and time selections
        if st.button("Submit Date and Time"):
            # Store selected date and time in session state
            st.session_state.selected_date = selected_date
            st.session_state.selected_time = selected_time

        # Display the selected date and time
        if 'selected_date' in st.session_state and 'selected_time' in st.session_state:
            st.write("Selected Date:", st.session_state.selected_date)
            st.write("Selected Time:", st.session_state.selected_time)

            # Checkbox to show/hide additional information
            show_info = st.checkbox("Show additional information")
            if show_info:
                st.write("I am enjoying doing streamlit.")

            # Slider to adjust text size
            text_size = st.slider("Adjust text size", 10, 50, 20)
            st.markdown(f"<p style='font-size:{text_size}px'>Selected Date: {st.session_state.selected_date}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size:{text_size}px'>Selected Time: {st.session_state.selected_time}</p>", unsafe_allow_html=True)
    else:
        # Login button
        if st.button("Login"):
            if check_credentials(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.experimental_rerun()  # Rerun to update the UI for logged in state
            else:
                st.error("Invalid username or password")

if __name__ == "__main__":
    main()
