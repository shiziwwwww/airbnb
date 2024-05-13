# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

import numpy as np 
import pandas as pd 
import matplotlib as plt
import seaborn as sns
import streamlit as st
st.title('My first app')
st.write("Here's our first app with Streamlit")
data = pd.read_csv("C:/Users/jingy/Desktop/M2.4/cph_airbnb_listings.csv")
data.head()

# Group the data by neighborhood and find the index of the minimum price in each neighborhood
min_price_index = data.groupby('neighbourhood')['price'].idxmin()

# Use the index to retrieve the corresponding name
min_price_listings = data.loc[min_price_index, ['neighbourhood', 'name', 'price']]
print(min_price_listings)
merged_data = pd.merge(min_price_listings, data, on='name', how='inner')
print(merged_data)
price_min_nights_reviews = merged_data[['price_x', 'minimum_nights', 'number_of_reviews', 'reviews_per_month','number_of_reviews_ltm']]
correlation_matrix = price_min_nights_reviews.corr()
# 绘制热图，并标出数据值
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Price, Minimum Nights, and Reviews')
plt.show()
st.pyplot(plt)
