import streamlit as st
st.title("BMI Calculator")
height=st.number_input("Enter your height (in meters): ",format="%.2f")
weight=st.number_input("enter your weight (in kgs): ",format="%.1f")

if st.button("Calculate BMI"):
    if height>0 and weight>0:
        bmi=weight/(height**2)
        st.write(f"### Your BMI is **{bmi:.2f}**")  
        if bmi<18.5:
            st.warning("You are underweight.")
        elif 18.5<=bmi<24.9:
            st.success("You are in the normal range.")
        elif 25<=bmi<29.9:
            st.info("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid values for height and weight")