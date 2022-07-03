import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("housingprice.pkl", 'rb'))

st.title("Housing Price Prediction")
st.subheader("""You can predict how much your house will sell for!

By providing the following information""")

#Getting input from user
Area = st.number_input('Enter Housing Area(SQft)')
st.write('Area : ',Area)
Bedrooms = st.number_input('Enter no of Bedrooms')
st.write('Bedrooms :', Bedrooms)
bathrooms = st.number_input('Enter no of Bathrooms')
st.write('Bathrooms :', bathrooms)
stories = st.number_input('Enter no of Stories')
st.write('Stories :', stories)
mainroad = st.selectbox('Near the Mainroad or not ?',('Yes','No'))
st.write('Your option : ', mainroad)
guestroom = st.selectbox('Does it have a Guestroom ?',('Yes','No'))
st.write('Guestroom : ', guestroom)
basement = st.selectbox('Does it have a Basement ?',('Yes','No'))
st.write('Basement : ', basement)
hotwaterheating = st.selectbox('Does it have Hot Water Heating Facility ?',('Yes','No'))
st.write('Hot Water Heating Facility : ', hotwaterheating)
airconditioning = st.selectbox('Does it have Air Conditioning Facility ?',('Yes','No'))
st.write('Air Conditioning Facility : ', airconditioning)
parking = st.number_input('Enter no of Parking')
st.write('Parking spots :', parking)
prefarea = st.selectbox('Does it have PrefArea ?',('Yes','No'))
st.write('PrefArea : ', prefarea)
furnishing = st.selectbox('Is it Furnished ?',('Furnished','Semi-Furnished','Unfurnished'))
st.write('Furnished Status : ', furnishing)

def texttobin(x):
    if x == 'Yes':
        return 1
    else: 
        return 0
    
def texttobins(x):
    if x == 'Furnished':
        return 0
    elif x == 'Semi-Furnished': 
        return 1
    else:
        return 2

mainroad = texttobin(mainroad)
guestroom = texttobin(guestroom)
basement = texttobin(basement)
hotwaterheating = texttobin(hotwaterheating)
airconditioning = texttobin(airconditioning)
parking = texttobin(parking)
prefarea = texttobin(prefarea)
furnishing = texttobins(furnishing)


#result
if st.button("Predict"):
    if Area or Bedrooms or bathrooms or stories or parking > 0.0:
        result=model.predict([[Area,Bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishing]])
        result=np.round(result)
        st.success('The output is {}'.format(result))
    else:
        st.error("""Insufficient Data For Prediction""")
    

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://static.vecteezy.com/system/resources/previews/001/264/276/large_2x/wooden-houses-on-dark-background-free-photo.jpg");
             background-attachment: fixed;
             background-size: contain
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
        

