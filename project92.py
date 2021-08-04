import streamlit as st

@st.cache()
def calculate_emi(p,n,r):
  n = n*12
  r = r/12
  emi = p*(r/100)*((1+(r/100))**n)/(((1+(r/100))**n)-1)
  return round(emi,3)

def calculate_outstanding_balance(p,n,r,m):
  n = n*12
  r = r/12
  R = (1+(r/100))
  balance = (p*(R**n - R**m))/((R**n) - 1)
  return round(balance,3)


st.title("EMI Calculator App")
p = st.number_input("Principal Amount", value=1000, step=1000)
tenure = st.slider("Tenure",1,30*12)
roi = st.slider("Rate of Interest",1,15)
m = st.slider("Outstanding Months",1,30*12)

st.write("Principal Amount: ",p)
st.write("Tenure: ",tenure,"Months")
st.write("Rate of Interest: ",roi,"%")
st.write("Outstanding Months: ",m,"Months")


if st.button("Calculate EMI"):
	emi = calculate_emi(p,tenure/12,roi)
	st.write("Calculated EMI is: ",emi)

elif st.button("Calculate Outstanding Balance"):
	balance = calculate_outstanding_balance(p,tenure/12,roi,m)
	st.write("Outstanding Balance: ",balance)

