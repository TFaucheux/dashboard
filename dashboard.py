# Imports
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import seaborn as sns
import matplotlib.pyplot as plt
import sys

# Sample data
data = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'category': ['A', 'A', 'B', 'B', 'C'],
    'sub_category': [1, 1, 2, 2, 3],
    'value': [10, 20, 15, 30, 25],
    'lat': [37.78, 37.79, 37.77, 37.76, 37.80],
    'lon': [-122.41, -122.42, -122.43, -122.44, -122.40]
})

# Global styling
PAGE_BG_COLOR = "#FFFFFF"
TEXT_COLOR = "#000000"
FONT_FAMILY = "Arial"

# Data loading
def load_data(filepath):
  df = pd.read_csv(filepath)
  return df

# Page layout
def set_page_config():
  st.set_page_config(page_title='My Report', page_icon='📊')

def add_custom_css():
  st.markdown(f"""
    <style>
      .reportview-container .main .block-container{{
          padding: 0rem 1rem;
      }}
      .reportview-container .main {{
          color: {TEXT_COLOR};
          background-color: {PAGE_BG_COLOR};
          font-family: {FONT_FAMILY};
      }}
      img {{
          max-width:100%
      }}
    </style>
  """, unsafe_allow_html=True)

def add_sidebar():
  st.sidebar.header('Parameters')
  metric = st.sidebar.selectbox('Metric', data.columns)
  return metric

def add_logo():
  st.image('logo.png', width=100)

def add_map():
  st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=data,
            get_position=['lon', 'lat'],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position=['lon', 'lat'],
            get_color='[200, 30, 0, 160]',
            get_radius=200
        )
    ]
  ))

# Content blocks
def add_overview():
  st.header('Overview')
  st.write('Summary...')

def add_kpi():
  c1, c2, c3 = st.columns(3)
  c1.metric('Revenue', '120M')
  c2.metric('Customers', '1.2M')
  c3.metric('Growth', '10%')

def add_charts(metric):
  fig, ax = plt.subplots()
  sns.barplot(data=data, x='sub_category', y=metric)
  st.pyplot(fig)

  fig, ax = plt.subplots()
  sns.lineplot(data=data, x='value', y=metric)
  st.pyplot(fig)

def add_matrix():
  cols = st.columns(3)
  for i in range(9):
    with cols[i%3]:
      st.metric(f'Box {i+1}', f'{np.random.randint(1000)}')

def add_details():
  st.header('Details')
  st.dataframe(data)

def add_analysis():
  st.header('Analysis')
  st.write('Deeper analysis...')

def add_download_csv():
  csv = data.to_csv(index=False).encode('utf-8')

  st.download_button(
      "Press to Download",
      csv,
      "report.csv",
      "text/csv",
      key='download-csv'
  )

def add_footer():
  st.markdown('___')
  st.markdown('Copyright Acme Inc. 2023 - Report generated on '+ str(pd.Timestamp.today().date()))

# Main script
def main():
  global data

  # Page layout
  set_page_config()
  add_custom_css()
  add_logo()
  add_map()

  # Get input
  metric = add_sidebar()

  # Content blocks
  add_overview()
  add_kpi()
  add_charts(metric)
  add_matrix()
  add_details()
  add_analysis()
  add_download_csv()

  # Footer
  add_footer()

if __name__ == '__main__':
  main()
