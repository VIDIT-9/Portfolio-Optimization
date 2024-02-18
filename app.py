import streamlit as st
import os
import pandas as pd
from PIL import Image
import pickle

with open('final_allocation.pkl', 'rb') as file:
    final_allocation = pickle.load(file)

with open('logo_list.pkl', 'rb') as logo:
    logo_list = pickle.load(logo)


st.title("Portfolio Optimization App")
st.markdown('''
**This app tries to find the optimal allocation of assets that aims to maximize returns while minimizing risk**
''')

user_input = st.number_input("Amount to invest:", min_value=500)


if st.button("Optimize") and user_input is not None:
    
    optimized_portfolio = final_allocation * user_input
    optimized_portfolio = pd.DataFrame(optimized_portfolio)


    image_width = 50
    image_height = 50
    num_columns = 5

    for i in range(2):
        st.write("")  
        row = st.columns(5) 
        for j in range(5):
            idx = i * 5 + j
            ticker = optimized_portfolio.index[idx]
            value = optimized_portfolio.iloc[idx, 0]

            image_path = os.path.join('logo', f'{ticker}.png')
            image = Image.open(image_path).resize((image_width, image_height))
            
            with row[j]:
                st.image(image, caption=f'{ticker}', use_column_width=True)
                st.write(f"Amount: {round(value)}")
                
