import streamlit as st
from bigtree import DAGNode, dag_to_dot, dict_to_dag, dag_iterator

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

dag_graph = dag_to_dot(dagr)

graphdag = dag_graph.to_string()
print(graphdag)


# Create a graphlib graph object
st.graphviz_chart(graphdag)

# voir https://docs.streamlit.io/library/api-reference/charts/st.graphviz_chart

# rankdir "TB" "LR" "BT" "RL"