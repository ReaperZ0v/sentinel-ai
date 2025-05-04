from langchain_community.llms.ollama import Ollama
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents import initialize_agent, AgentType
from models import CriminalRecord
from config import DB_CONN_STRING


def perform_sentinal_search(question: str):
    db = SQLDatabase.from_uri(DB_CONN_STRING)
    llm = Ollama(model="qwen2:7b-instruct-q5_K_M", temperature=0)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    tools = toolkit.get_tools()

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

    qst = f"""

    The question is : \n
    {question} \n \n

    the database table name is: criminalrecord \n
    the crime column name is: crimes \n
    the gender column is: gender with the options of female or male \n

    Convert the height to meters IF mentioned or provided and THEN search the converted height in SQL \n

    DO NOT give false information, retrieve and render information from the database itself \n

    DO NOT match ethnicity to an exact value, check if it resembles any values in your found results. \n

    DO NOT return SQL queries, return the records you found from the database based on your reasoning of the provided question, return back the results full details in a organized table containing all other details of the row or rows of data found \n

    When you find the results from the database include ALL fields from the database in your final output and DO NOT make up fields. \n

    ONLY give information found from the database, if nothing is found then simply say nothing was found \n
    """

    response = agent.run(qst)
    return response 







