import streamlit as st
import pickle
import base64
import numpy as np
import pandas as pd

st.title('Water_potability')
ph=st.slider('Enter your ph-level',0.0,14.0,0.5)
chloro=st.slider('Enter choloromine',0.3,13.5,0.5)
hardness=st.slider('enter the hardness',47.43,323.0,0.5)
solid=st.slider('enter the solidity',320.0,61228.0,0.5)
Sulfate=st.slider('Enter the Sulfate',128.0,485.0,0.5)
Conductivity=st.slider('Conductivity of Water',181.5,755.0,0.5)
Organic_carbon=st.slider('Organic_content',2.5,29.0,0.5)
Trihal=st.slider('Enter the trihalomethanes',0.7,124.0,0.5)
turbid=st.slider('Enter the Turbidity',1.45,6.8)


with open('transform_Chloramines.pkl','rb')as file:
    Chloramin_ts=pickle.load(file)
with open('transform_Conductivity.pkl','rb')as file:
    Conductivity_ts=pickle.load(file)
with open('transform_Hardness.pkl','rb')as file:
    hardness_ts=pickle.load(file)
with open('transform_Organic_carbon.pkl','rb')as file:
    orgcarb_ts=pickle.load(file)
with open('transform_ph.pkl','rb')as file:
    ph_ts=pickle.load(file)
with open('transform_Solids.pkl','rb')as file:
    Solid_ts=pickle.load(file)
with open('transform_Sulfate.pkl','rb')as file:
    sulphate_ts=pickle.load(file)
with open('transform_Trihalomethanes.pkl','rb')as file:
    trihal_ts=pickle.load(file)
with open('transform_Turbidity.pkl','rb')as file:
    turbidity_ts=pickle.load(file)
    
with open('model_svc.pkl','rb')as file:
    model=pickle.load(file)

    
ph=ph_ts.transform(pd.DataFrame([ph]))
# st.write(ph[0])
Hardness=hardness_ts.transform(pd.DataFrame([hardness]))
chloramine=Chloramin_ts.transform(pd.DataFrame([chloro]))
Conductivity=Conductivity_ts.transform(pd.DataFrame([Conductivity]))
organic_carbon=orgcarb_ts.transform(pd.DataFrame([Organic_carbon]))
Solids=Solid_ts.transform(pd.DataFrame([solid]))
sulphate=sulphate_ts.transform(pd.DataFrame([Sulfate]))
trihalomethanes=trihal_ts.transform(pd.DataFrame([Trihal]))
turbidity=turbidity_ts.transform(pd.DataFrame([turbid]))

data=pd.DataFrame({'ph':ph[0],'Hardness':Hardness[0],'Solids':Solids[0],'Chloramines':chloramine[0],'Sulfate':sulphate[0],
                   'Conductivity':Conductivity[0],'Organic_carbon':organic_carbon[0],'Trihalomethanes':trihalomethanes[0],
                  'Turbidity':turbidity[0]})
# st.write(data)

prediction=model.predict(data)
# st.write(prediction)
if st.button('Prediction'):
    if prediction==0:
        st.error('Not potable')
    else:
        st.success('Potable')   
