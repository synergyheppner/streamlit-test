import streamlit as st
from bigtree import DAGNode, dag_to_dot

n01 = DAGNode.from_dict({"name": "s1", "info": "source"})
n02 = DAGNode.from_dict({"name": "s2", "info": "source"})
n03 = DAGNode.from_dict({"name": "t1", "info": "temp"})
n04 = DAGNode.from_dict({"name": "t2", "info": "temp"})
n05 = DAGNode.from_dict({"name": "mytable", "info": "target"})

n03.parents=[n01,n02]
n04.parents=[n01,n03]
n05.parents=[n01,n04]  

dag_graph = dag_to_dot(n01)

print(dag_graph.to_string())

"""
# Create a graphlib graph object
st.graphviz_chart('''
    strict digraph G {
			rankdir=LR; 
			a [label=a];
   			b [label=b];
			c [label=c];
			d [label=d];
			e [label=e shape="ellipse" style="filled" fillcolor="#1f77b4"];
			d -> e;
			c -> d;
			a -> c;
			a -> d;
			b -> c;
}
''')
"""

# voir https://docs.streamlit.io/library/api-reference/charts/st.graphviz_chart

# rankdir "TB" "LR" "BT" "RL"