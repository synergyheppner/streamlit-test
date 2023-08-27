import streamlit as st

# Create a graphlib graph object
st.graphviz_chart('''
    digraph {
    a [shape="ellipse" style="filled" fillcolor="#1f77b4"]
    b [shape="polygon" style="filled" fillcolor="#ff7f0e"]
    a -> b [fillcolor="#a6cee3" color="#1f78b4"]
}
''')

# voir https://docs.streamlit.io/library/api-reference/charts/st.graphviz_chart