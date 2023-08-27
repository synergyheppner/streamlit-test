import streamlit as st
from bigtree import DAGNode, dag_to_dot, dict_to_dag, dag_iterator, dataframe_to_dag
import pandas as pd

#   n01 = DAGNode.from_dict({"name": "s1", "info": "source"})
#   n02 = DAGNode.from_dict({"name": "s2", "info": "source"})
#   n03 = DAGNode.from_dict({"name": "t1", "info": "temp"})
#   n04 = DAGNode.from_dict({"name": "t2", "info": "temp"})
#   n05 = DAGNode.from_dict({"name": "mytable", "info": "target"})

#   n03.parents=[n01,n02]
#   n04.parents=[n01,n03]
#   n05.parents=[n04]  

#   dag_graph = dag_to_dot(n01)

#    relation_dict = {
#    "n01": {"name": "s1", "info": "source"},
#    "n02": {"name": "s2", "info": "source"},
#    "n03": {"name": "t1", "info": "temp", "parents": ["n01","n02"]},
#    "n04": {"name": "t2", "info": "temp", "parents": ["n01","n03"]},
#    "n05": {"name": "mytable", "info": "target", "parents": ["n04"]},
#    }

#    dagr = dict_to_dag(relation_dict, parent_key="parents")

path_data = pd.DataFrame([
   ["n01", None, "s1", "source"],
   ["n02", None, "s2", "source"],
   ["n03", "n01", "t1", "temp"],
   ["n03", "n02", "t1", "temp"],
   ["n04", "n01", "t2", "temp"],
   ["n04", "n03", "t2", "temp"],
   ["n05", "n04", "mytable", "target"],
],
   columns=["child", "parent", "name", "info"]
)
dagr = dataframe_to_dag(path_data)
#print(dagr.describe())
#print(dagr.get_attr("info"))
dag_graph = dag_to_dot(dagr)

graphdag = dag_graph.to_string()
#print(graphdag)


# Create a graphlib graph object
st.graphviz_chart(graphdag)

# voir https://docs.streamlit.io/library/api-reference/charts/st.graphviz_chart

# rankdir "TB" "LR" "BT" "RL"