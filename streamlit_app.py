import streamlit as st
from bigtree import DAGNode, dag_to_dot, dict_to_dag, dag_iterator, dataframe_to_dag
import pandas as pd
import pydot

graph = pydot.Dot("my_graph", graph_type="digraph", strict='true', rankdir="LR")

# Add nodes
my_node = pydot.Node("n01", label="s1\n(table)", style = "filled", fillcolor = "lightblue", color="blue", shape="underline")
graph.add_node(my_node)
my_node = pydot.Node("n02", label="s2\n(table)", style = "filled", fillcolor = "lightblue", color="blue", shape="underline")
graph.add_node(my_node)
my_node = pydot.Node("n03", label="v1\n(view)", style = "filled", fillcolor = "snow3", color="black", width=0.5, height=0.5, fontcolor="blue", fontsize="20", shape="underline")
graph.add_node(my_node)
my_node = pydot.Node("n04", label="v2\n(view)", style = "filled", fillcolor = "mistyrose3", color="black", shape="underline")
graph.add_node(my_node)
my_node = pydot.Node("n05", label="mytable\n(table)", style = "bold, filled", fillcolor = "#add188", shape="underline")
graph.add_node(my_node)

# Add edges
my_edge = pydot.Edge("n01", "n03", color="black")
graph.add_edge(my_edge)
my_edge = pydot.Edge("n02", "n03", color="black")
graph.add_edge(my_edge)
my_edge = pydot.Edge("n02", "n04", color="black")
graph.add_edge(my_edge)
my_edge = pydot.Edge("n03", "n04", color="black")
graph.add_edge(my_edge)
my_edge = pydot.Edge("n04", "n05", color="black")
graph.add_edge(my_edge)

graphdag = graph.to_string()
# graphdag = dag_graph.to_string()
#print(graphdag)

# Create a graphlib graph object
st.graphviz_chart(graphdag)

# voir https://docs.streamlit.io/library/api-reference/charts/st.graphviz_chart
# rankdir "TB" "LR" "BT" "RL"
# voir http://magjac.com/graphviz-visual-editor/
# pour les couleurs, voir https://graphviz.org/doc/info/colors.html
