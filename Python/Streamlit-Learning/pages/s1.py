#!/usr/bin/env python3
import streamlit as st

import pandas as pd
import numpy as np


def app():
    st.set_page_config(page_title="S1 Demo", page_icon="📊")

    # st.markdown("S1 Demo")
    # st.sidebar.header("S1 Demo")
    st.write(
        """This demo shows how to use `st.write` to visualize Pandas DataFrames.
    (Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
    )
    df = pd.DataFrame(np.random.randn(50, 20),
                      columns=('col %d' % i for i in range(20)))

    st.dataframe(df.style.highlight_max(axis=0))

    # Cache the dataframe so it's only loaded once
    @st.cache_data
    def load_data():
        return pd.DataFrame({
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        })

    # Boolean to resize the dataframe, stored as a session state variable
    UCWidth = st.checkbox("Use container width",
                          value=False,
                          key="use_container_width")

    df = load_data()

    # Display the dataframe and allow the user to stretch the dataframe
    # across the full width of the container, based on the checkbox value
    st.dataframe(df, use_container_width=st.session_state.use_container_width)
    # st.dataframe(df, use_container_width=UCWidth)

    title = st.text_input('Element name', 'DEFAULT VALUE')
    st.write('The default value is:', title)


app()
