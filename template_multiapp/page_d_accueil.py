import pandas as pd
import streamlit as st
import numpy as np
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode



############# FONCTION

def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.

    Args:
        df (pd.DataFrame]): Source dataframe

    Returns:
        dict: The selected row
    """

    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )


    options.configure_side_bar()
    options.configure_selection(selection_mode= "multiple",use_checkbox = True)
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED
    )

    return selection



# Configuration de la page
# parametre layout: wide ou centered
# parametre initial_sidebar_state: expanded, auto ou collapsed
st.set_page_config(
     page_title="Change le nom de la page dans l'onglet du navigateur",
     page_icon="👋",
     layout="wide",
     initial_sidebar_state="expanded"
 )


# Nom donnée à la page sur la barre de navigation
st.sidebar.markdown("# 	PAGE D'ACCEUIL ")

####################################################


# Titre de la page
st.title("PAGE D'ACCEUIL ")
st.write("Documentation et exemple de composants au lien suivant:")
st.write("https://docs.streamlit.io/library/get-started")

st.write("Contenu pour découvrir les objets de Streamlit")
st.write("https://www.youtube.com/watch?v=vIQQR_yq-8I&ab_channel=FaniloAndrianasolo")
st.write("https://www.youtube.com/watch?v=nnmBdpvN6u8&ab_channel=FaniloAndrianasolo")


# Declaration de variable pour stockage sur le session state
if "nom_variable" not in st.session_state:
     st.session_state.nom_variable = False

st.title("Ecrit un titre")
st.header("Ecrit un en-tete")
st.subheader("Ecrit un sous-en-tete")
st.write("Ecrit un texte")
st.markdown("Ecrit un texte au format markdown")

# Affichage de données
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
st.write('Format dataframe')
st.dataframe(df)

st.write('Format table')
st.table(df)

st.write("Example table interactive")
selection = aggrid_interactive_table(df=df)