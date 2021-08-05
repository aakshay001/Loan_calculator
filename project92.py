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
tenure = st.number_input("Tenure(in months)", value=12, step=1)
roi = st.number_input("Rate of Interest", value=7.0, step=0.1)
m = st.number_input("Outstanding Months", value=0, step=1)

st.write("Principal Amount: ",p)
st.write("Tenure: ",tenure,"Months")
st.write("Rate of Interest: ",roi,"%")
st.write("Outstanding Months: ",m,"Months")

option = st.selectbox("Enter Your Choice",("Calculate EMI","Outstanding Balance"))
if st.button("Calculate"):
	if option == "Calculate EMI":
		emi = calculate_emi(p,tenure/12,roi)
                st.write("Calculated EMI is: ",emi)
		
	elif option ==  "Outstanding Balance":
		balance = calculate_outstanding_balance(p,tenure/12,roi,m)
	        st.write("Outstanding Balance: ",balance)
		
	


	


