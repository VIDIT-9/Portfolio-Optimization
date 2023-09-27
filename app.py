
import streamlit as st
import pickle


with open('final_allocation.pkl', 'rb') as file:
    final_allocation = pickle.load(file)

with open('logo_list.pkl', 'rb') as logo:
    logo_list = pickle.load(logo)

st.title("Portfolio Optimization App")

st.markdown('''
**This app tries to find the optimal allocation of assets that aims to maximize returns while minimizing risk**
''')

user_input = st.number_input("Amount to invest: ", min_value=100)

if st.button("Optimize"):


    if user_input:

        optimized_portfolio = final_allocation * user_input

        image_width = 100
        image_height = 100
        num_columns = 5

        for i in range(0, len(logo_list), num_columns):
            row = logo_list[i:i + num_columns]
            row_values = optimized_portfolio.iloc[0,i:i + num_columns]
            
            columns = st.columns(num_columns)
            
            for j, ticker in enumerate(row):
                value = row_values[j]
                
                logo_url = f"https://logo.clearbit.com/{ticker}.com"
                
                with columns[j]:
                    st.image(logo_url, width=image_width, use_column_width=False, output_format="auto")
                    st.write(f"Amount: {round(value)}")