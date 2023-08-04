import sys
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

# Load data from command line argument
data_file = sys.argv[1]
df = pd.read_csv(data_file)

# Set page configuration
st.set_page_config(page_title='My Dashboard', page_icon=':bar_chart:')

# Define functions to create charts
def generate_line_chart(df, x, y, title):
  chart = alt.Chart(df).mark_line().encode(
      x=x,
      y=y
  ).properties(
      width=600,
      height=400
  ).interactive()

  st.altair_chart(chart, use_container_width=True)

  st.markdown(f"**{title}**")

def generate_bar_chart(df, x, y, title):
  chart = alt.Chart(df).mark_bar().encode(
      x=x,
      y=y
  ).properties(
      width=600,
      height=400
  )

  st.altair_chart(chart, use_container_width=True)

  st.markdown(f"**{title}**")

def generate_map(df, lat, lon, metric):
  st.map(df[[lat, lon, metric]])

  st.markdown("## Regional Map")

# Add logo
st.image('logo.png')

# Add headline
st.title('My Interactive Dashboard')

# Line chart
generate_line_chart(df, 'date', 'revenue', 'Revenue Over Time')

# Bar chart
generate_bar_chart(df, 'product', 'sales', 'Sales by Product')

# Map
generate_map(df, 'lat', 'lon', 'sales')

# 9-box grid
cols = st.columns(3)
for i in range(9):
  with cols[i // 3]:
    fig, ax = plt.subplots()
    ax.plot(np.random.randn(20).cumsum(), '-o')
    st.pyplot(fig)

# Footer
st.markdown("""
---
Generated on %s
""" % pd.to_datetime('today').date())

st.download_button('Download PDF', data='...', file_name='report.pdf')
