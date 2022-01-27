import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('model_pickle.pkl','rb'))


def main():
  st.sidebar.header("Insurance Cost prediction")
  st.sidebar.text("This a Web app that tells you the predicted insurance costs.")
  st.sidebar.header("Just fill in the information below")
  st.sidebar.text("The AdaBoost regression Model was used.")



  age = st.slider("Input Your age", 0, 100)
  hypertension = st.slider("Input your if you have hypertesnsion with 0 for no and 1 for yed",0,1)
  heartdisease = st.slider("Input your if you have heartdisease with 0 for no and 1 for yes",0 ,1)
  sugar = st.slider("Put your average glucose level",150.0, 300.000)
  bmi = st.slider("Input your BMI",0.0,70.0)

  inputs = [[age,hypertension,heartdisease,sugar,bmi]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(float)
    st.success('The Your Insurance Costs will be{}'.format(updated_res))


if __name__ =='__main__':
  main()
