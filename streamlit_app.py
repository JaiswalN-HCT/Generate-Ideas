import streamlit as st
import pandas as pd
import random
from random import sample
from string import digits

st.title('Generating ideas from random combinations')

trends_list = pd.read_excel("Innovation gen.xlsx", sheet_name='Trends', index_col=None, header=None)

sayings_list = pd.read_excel("Innovation gen.xlsx", sheet_name='Sayings', header=None)

skills_interests_list = pd.read_excel("Innovation gen.xlsx", sheet_name='Skills&Interests', header=None)

rand_trend = str(trends_list.sample(1, ignore_index=True))
rand_saying = str(sayings_list.sample(1, ignore_index=True))
rand_skill = str(skills_interests_list.sample(1, ignore_index=True))

#st.subheader("Combinations from provided list of ideas")
st.text("Use below phrases in any random order to create you own ideas\n")

# to remove numeric digits from string 
remove_digits = str.maketrans('', '', digits)

col1, col2, col3 = st.columns(3)
with col1: 
    # using translate and digits from above
    st.write(rand_trend.translate(remove_digits))

with col2:
    st.write("\t", rand_saying.translate(remove_digits))
    
with col3:
    st.write("\t", rand_skill.translate(remove_digits))

st.button("Refresh")