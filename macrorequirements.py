import streamlit as st

params=[]
def calcparams(bw,cldeficit):
    mcl=round(bw*30,2)
    flcl=round(mcl-cldeficit,2)
    pi=round(bw*1.5,2)
    cai=pi
    caipi=round((cai*4)+(pi*4),2)
    fatcl=round(flcl-caipi,2)
    dfi=round(fatcl/9,2)
    params.append(mcl)
    params.append(flcl)
    params.append(pi)
    params.append(cai)
    params.append(caipi)
    params.append(fatcl)
    params.append(dfi)
    


st.write("Enter your Body Weight & Calorie deficit target")
c1,c2= st.columns(2,vertical_alignment="bottom")
bw=int(c1.number_input(label="",key="bw",value=75))
c2.write("Kg")
st.write("")
c3,c4= st.columns(2,vertical_alignment="bottom")
cldeficit=int(c3.number_input(label="",value=500))
c4.write("Calories")

if st.button("Calculate",on_click=calcparams(bw,cldeficit)):
    st.write("Based on Calorie deficit of "+str(cldeficit)+" Your intake should be as follows:")
    st.write("Maintenance Calories:- "+str(params[0]))
    st.write("Fat Loss Calories:- "+str(params[1]))
    st.write("Protein Intake:- "+str(params[2])+" gms")
    st.write("Carbs Intake:- "+str(params[3])+" gms")
    st.write("Total of Protein & Carb Calorie Intake:- "+str(params[4]))
    st.write("Fat Intake Calories:- "+str(params[5]))
    st.write("Daily Fat Intake:- "+str(params[6])+" gms")