import streamlit as st


st.set_page_config(
    page_title = "Toxic.AI",
    page_icon = "🏠",
    layout="wide",
    initial_sidebar_state= "collapsed"
)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 3rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

def Home_Page():

    col1,col2 = st.columns(spec=(1.5,1), gap="large")
    with col1:

        st.markdown(
            "<h1 class='center' style='font-size: 72px;'>DrugShield.AI🧪</h1>",
            unsafe_allow_html=True,
        )
        st.write("")
        Intro_text1 = ("<p style='font-size: 22px;'>Our main goal in this collaborative project was to advance drug toxicity prediction using the Tox21 dataset and innovative graph neural networks. Leveraging these tools, we delved into the intricate relationships within molecular structures to enhance the accuracy of toxicity predictions. By employing novel approaches to analyze complex interactions, our team aimed to contribute to the development of more effective and safer pharmaceuticals. The utilization of Tox21 data and graph neural networks underscores our commitment to exploring cutting-edge techniques in computational biology for drug discovery and safety assessment.</p>")
        st.markdown(Intro_text1, unsafe_allow_html=True)

        Intro_text2 = (
            "<p style='font-size: 22px;'>Below, you'll find the GitHub links for both team members, as well as the project's GitHub repository and the dataset link. Feel free to explore and access the resources.</p>")
        st.markdown(Intro_text2, unsafe_allow_html=True)
        st.markdown("***")


        # Creating toggle for the dataset link and the github link
        Member1_info_col,Member2_info_col,dataset_col, github_col = st.columns(spec=(1,1,1,1), gap="medium")
        with Member1_info_col:
            st.link_button(label="Yuvraj Singh (Github)", url="https://github.com/yuvraaj2002?tab=repositories")
        with Member2_info_col:
            st.link_button(label="Swatita Dash (Github)", url="https://github.com/swatuu0602")
        with dataset_col:
            st.link_button(label="Tox21 Dataset Link", url="https://paperswithcode.com/dataset/tox21-1")
        with github_col:
            st.link_button(label="Project Github Repo", url="https://github.com/yuvraaj2002/Deep_Learning_Projects/tree/master/Illegal_Discussion")

        st.markdown("***")
        Intro_text3 = (
            "<p style='font-size: 22px;'>The module for predicting the drug's toxicity is available in the drop-down menu at the top left corner of this page. Just select the module, and you will be directed to the prediction model page.</p>")
        st.markdown(Intro_text3, unsafe_allow_html=True)


    with col2:
        st.image('drug_ai/Durg_Toxicity/Images/Home.jpg')




Home_Page()


