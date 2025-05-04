from aerich import Command
from tortoise import Tortoise
import streamlit as st 
from config import *
from utils.utils import * 
import asyncio
import time 


async def runme():
    await Tortoise.init(
        config=TORTOISE_ORM,
    )

    command = Command(tortoise_config=TORTOISE_ORM, app="models")
    await command.init()
    await command.upgrade()

@st.cache_resource
def initializer():
    asyncio.run(runme())

st.markdown("## S3NTIN3L AI")
st.markdown("`v.1.0.0` :green-badge[BETA]")
st.markdown(">A Retrieval Augmented Generation (RAG) powered system to search through a database of criminals and provide accurate results based on the searcher's provided prompt. A BETA variant to demonstrate how AI can give LEAs an Edge. (Expand the below JSON to see the schema of a criminal.)")
st.json({
    "id": 1,
    "first_name": "Carla",
    "last_name": "Alexander",
    "crime": [
        "Robbery",
        "Drug Possession"
    ],
    "age": 35,
    "height": 1.75,
    "gender": "female",
    "ethnicity": "Native Hawaiian",
    "hair_color": "Dark Brown",
    "additional_description": "",
    "in_custody": 1,
    "has_past_convictions": 1
}, expanded=False)

st.divider()
alert = st.empty()

question = st.text_input(label="Query", placeholder="e.g looking for a 1.8 meter tall criminal with hispanic ethnicity")
trigger_rag_search = st.button(label="Search")

if trigger_rag_search:
    with st.spinner("Searching..."):
        result = perform_sentinal_search(question)
        print(result)

    alert.success("Augmented Information Retrieval Successful!")

    def stream_response():
        for chunk in result:
            yield chunk 
            time.sleep(0.01)

    st.write_stream(stream_response())
    



