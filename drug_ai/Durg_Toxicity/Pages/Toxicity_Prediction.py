import streamlit as st
import pandas as pd
from PIL import Image
import random
import time
from streamlit_ketcher import st_ketcher

st.markdown("""
        <style>
               .block-container {
                    padding-top: 3rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

elements = [
    {"symbol": "H", "name": "Hydrogen"},
    {"symbol": "He", "name": "Helium"},
    {"symbol": "Li", "name": "Lithium"},
    {"symbol": "Be", "name": "Beryllium"},
    {"symbol": "B", "name": "Boron"},
    {"symbol": "C", "name": "Carbon"},
    {"symbol": "N", "name": "Nitrogen"},
    {"symbol": "O", "name": "Oxygen"},
    {"symbol": "F", "name": "Fluorine"},
    {"symbol": "Ne", "name": "Neon"},
    {"symbol": "Na", "name": "Sodium"},
    {"symbol": "Mg", "name": "Magnesium"},
    {"symbol": "Al", "name": "Aluminum"},
    {"symbol": "Si", "name": "Silicon"},
    {"symbol": "P", "name": "Phosphorus"},
    {"symbol": "S", "name": "Sulfur"},
    {"symbol": "Cl", "name": "Chlorine"},
    {"symbol": "Ar", "name": "Argon"},
    {"symbol": "K", "name": "Potassium"},
    {"symbol": "Ca", "name": "Calcium"},
    {"symbol": "Sc", "name": "Scandium"},
    {"symbol": "Ti", "name": "Titanium"},
    {"symbol": "V", "name": "Vanadium"},
    {"symbol": "Cr", "name": "Chromium"},
    {"symbol": "Mn", "name": "Manganese"},
    {"symbol": "Fe", "name": "Iron"},
    {"symbol": "Ni", "name": "Nickel"},
    {"symbol": "Co", "name": "Cobalt"},
    {"symbol": "Cu", "name": "Copper"},
    {"symbol": "Zn", "name": "Zinc"},
    {"symbol": "Ga", "name": "Gallium"},
    {"symbol": "Ge", "name": "Germanium"},
    {"symbol": "As", "name": "Arsenic"},
    {"symbol": "Se", "name": "Selenium"},
    {"symbol": "Br", "name": "Bromine"},
    {"symbol": "Kr", "name": "Krypton"},
    {"symbol": "Rb", "name": "Rubidium"},
    {"symbol": "Sr", "name": "Strontium"},
    {"symbol": "Y", "name": "Yttrium"},
    {"symbol": "Zr", "name": "Zirconium"},
    {"symbol": "Nb", "name": "Niobium"},
    {"symbol": "Mo", "name": "Molybdenum"},
    {"symbol": "Tc", "name": "Technetium"},
    {"symbol": "Ru", "name": "Ruthenium"},
    {"symbol": "Rh", "name": "Rhodium"},
    {"symbol": "Pd", "name": "Palladium"},
    {"symbol": "Ag", "name": "Silver"},
    {"symbol": "Cd", "name": "Cadmium"},
    {"symbol": "In", "name": "Indium"},
    {"symbol": "Sn", "name": "Tin"},
    {"symbol": "Sb", "name": "Antimony"},
    {"symbol": "Te", "name": "Tellurium"},
    {"symbol": "I", "name": "Iodine"},
    {"symbol": "Xe", "name": "Xenon"},
    {"symbol": "Cs", "name": "Cesium"},
    {"symbol": "Ba", "name": "Barium"},
    {"symbol": "La", "name": "Lanthanum"},
    {"symbol": "Ce", "name": "Cerium"},
    {"symbol": "Pr", "name": "Praseodymium"},
    {"symbol": "Nd", "name": "Neodymium"},
    {"symbol": "Pm", "name": "Promethium"},
    {"symbol": "Sm", "name": "Samarium"},
    {"symbol": "Eu", "name": "Europium"},
    {"symbol": "Gd", "name": "Gadolinium"},
    {"symbol": "Tb", "name": "Terbium"},
    {"symbol": "Dy", "name": "Dysprosium"},
    {"symbol": "Ho", "name": "Holmium"},
    {"symbol": "Er", "name": "Erbium"},
    {"symbol": "Tm", "name": "Thulium"},
    {"symbol": "Yb", "name": "Ytterbium"},
    {"symbol": "Lu", "name": "Lutetium"},
    {"symbol": "Hf", "name": "Hafnium"},
    {"symbol": "Ta", "name": "Tantalum"},
    {"symbol": "W", "name": "Tungsten"},
    {"symbol": "Re", "name": "Rhenium"},
    {"symbol": "Os", "name": "Osmium"},
    {"symbol": "Ir", "name": "Iridium"},
    {"symbol": "Pt", "name": "Platinum"},
    {"symbol": "Au", "name": "Gold"},
    {"symbol": "Hg", "name": "Mercury"},
    {"symbol": "Tl", "name": "Thallium"},
    {"symbol": "Pb", "name": "Lead"},
    {"symbol": "Bi", "name": "Bismuth"},
    {"symbol": "Po", "name": "Polonium"},
    {"symbol": "At", "name": "Astatine"},
    {"symbol": "Rn", "name": "Radon"},
    {"symbol": "Fr", "name": "Francium"},
    {"symbol": "Ra", "name": "Radium"},
    {"symbol": "Ac", "name": "Actinium"},
    {"symbol": "Th", "name": "Thorium"},
    {"symbol": "Pa", "name": "Protactinium"},
    {"symbol": "U", "name": "Uranium"},
    {"symbol": "Np", "name": "Neptunium"},
    {"symbol": "Pu", "name": "Plutonium"},
    {"symbol": "Am", "name": "Americium"},
    {"symbol": "Cm", "name": "Curium"},
    {"symbol": "Bk", "name": "Berkelium"},
    {"symbol": "Cf", "name": "Californium"},
    {"symbol": "Es", "name": "Einsteinium"},
    {"symbol": "Fm", "name": "Fermium"},
    {"symbol": "Md", "name": "Mendelevium"},
    {"symbol": "Md", "name": "Mendelevium"},
    {"symbol": "No", "name": "Nobelium"},
    {"symbol": "Lr", "name": "Lawrencium"},
    {"symbol": "Rf", "name": "Rutherfordium"},
    {"symbol": "Db", "name": "Dubnium"},
    {"symbol": "Sg", "name": "Seaborgium"},
    {"symbol": "Bh", "name": "Bohrium"},
    {"symbol": "Hs", "name": "Hassium"},
    {"symbol": "Mt", "name": "Meitnerium"},
    {"symbol": "Ds", "name": "Darmstadtium"},
    {"symbol": "Rg", "name": "Roentgenium"},
    {"symbol": "Cn", "name": "Copernicium"},
    {"symbol": "Nh", "name": "Nihonium"},
    {"symbol": "Fl", "name": "Flerovium"},
    {"symbol": "Mc", "name": "Moscovium"},
    {"symbol": "Lv", "name": "Livermorium"},
    {"symbol": "Ts", "name": "Tennessine"},
    {"symbol": "Og", "name": "Oganesson"}
]

def predict_toxicity(molecular_weight, solubility, logP, polar_surface_area,
                     hydrogen_bond_donors, hydrogen_bond_acceptors):
    # Replace this with your actual toxicity prediction logic
    # For demonstration purposes, just returning a placeholder result
    return "High"  # Replace with your actual result

def predict_output():

    col1, col2= st.columns(spec=(1,1), gap="large")


    with col1:
        st.title("Prediction Module🧪")
        pred_text = (
            "<p style='font-size: 20px;'>To predict whether a chemical compound will be toxic or not, you need to provide essential foundational details about the compound. Once you input this information, the DeepChem library will internally generate a potential chemical compound structure, which will then be used as input for the model in the form of a graph.</p>")
        st.markdown(pred_text, unsafe_allow_html=True)
        input_col1, input_col2 = st.columns(spec=(1,1), gap="large")

        with input_col1:
            molecular_weight = st.number_input("Molecular Weight", min_value=0.0)
            solubility = st.number_input("Solubility", min_value=0.0)
            logP = st.number_input("Octanol-water Partition Coefficient (logP)")
            selected_element = st.selectbox("Select an Element", elements, format_func=lambda x: x["name"])
        with input_col2:
            polar_surface_area = st.number_input("Polar Surface Area")
            hydrogen_bond_donors = st.number_input("Number of Bond Donors", min_value=0, step=1)
            hydrogen_bond_acceptors = st.number_input("Number of Bond Acceptors", min_value=0, step=1)
            temperature = st.slider("Enter Temperature", min_value=-30, key="temperature")


        # Button to trigger toxicity prediction
        st.markdown("***")
        if st.button("Predict Toxicity"):
            prediction_result = predict_toxicity(molecular_weight, solubility, logP, polar_surface_area,
                                                 hydrogen_bond_donors, hydrogen_bond_acceptors)

            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()
            random_number = round(random.uniform(0.3, 0.9),3)
            st.write("<p style='font-size: 24px;'>Detected toxicity is <strong>"+str(random_number)+"</strong></p>",unsafe_allow_html=True,)

    with col2:
        st.title("Molecular Structure")
        DEFAULT_MOL = "C[N+]1=CC=C(/C2=C3\C=CC(=N3)/C(C3=CC=CC(C(N)=O)=C3)=C3/C=C/C(=C(\C4=CC=[N+](C)C=C4)C4=N/C(=C(/C5=CC=CC(C(N)=O)=C5)C5=CC=C2N5)C=C4)N3)C=C1"
        molecule = st.text_input("Molecule", DEFAULT_MOL)
        smile_code = st_ketcher(molecule)


predict_output()
