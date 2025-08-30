import streamlit as st

#x = st.slider("Select a value")
#st.write(x, "squared is", x * x)

import pandas as pd
from numpy.random import default_rng as rng

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
        ],
        "stars": rng(0).integers(0, 1000, size=3),
        "views_history": rng(0).integers(0, 5000, size=(3, 30)).tolist(),
    }
)

st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐★",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

df = pd.DataFrame(
    rng(0).standard_normal((50, 20)), columns=("col %d" % i for i in range(20))
)
df2 = pd.DataFrame(rng(0).standard_normal((4, 4)), 
                   columns=["あ", "い","う", "え"])

st.dataframe(df)
st.area_chart(df2)