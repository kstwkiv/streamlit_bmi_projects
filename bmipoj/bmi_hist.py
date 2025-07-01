import streamlit as st
import matplotlib.pyplot as plt

st.title("BMI calculation with history")
if 'bmi_history' not in st.session_state:
    st.session_state.bmi_history=[]

height_cm=st.number_input("Enetr your height in cm: ")
weight_kg=st.number_input("Enter your weight in kgs: ")


if st.button("Check BMI"):
    if height_cm>0 and weight_kg>0:
        height_m=height_cm/100
        bmi=weight_kg/(height_m**2)
        st.write(f"Your BMI is **{bmi:.2f}**")

        st.session_state.bmi_history.append({
            'height (cm)':height_cm,
            'weight (kg)':weight_kg,
            'BMI': round(bmi,2)
        })
        if bmi<18.5:
            category="Underweight"
            color="Orange"
            st.warning("You are underweight.")
        elif 18.5<=bmi<24.9:
            category="Normal"
            color="Green"
            st.success("You are in the normal range.")
        elif 25<=bmi<29.9:
            category="Overweight"
            color="blue"
            st.info("You are overweight.")
        else:
            category="Obese"
            color="red"
            st.error("You are obese.")

        categories=["Underweight","Normal","Overweight","Obese"]
        values=[18.4,24.9,29.9,40]
        bar_colors=['Orange','Green','blue','red']
        fig,ax=plt.subplots()
        bars=ax.bar(categories,values,color=bar_colors)

        ax.axhline(bmi,color=color,linestyle='--',label=f"Your BMI: {bmi:.2f}")
        ax.legend()
        ax.set_ylabel("BMI value")
        ax.set_title("BMI categories and Values")

        st.pyplot(fig)
    else:
        st.error("Please enter valid values for height and weight")

if st.session_state.bmi_history:
    st.subheader("BMI Calculation History")
    st.dataframe(st.session_state.bmi_history)

    st.line_chart([entry['BMI'] for entry in st.session_state.bmi_history])