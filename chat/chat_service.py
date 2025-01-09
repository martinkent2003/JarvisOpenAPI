from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from project_config import setup_app_config

setup_app_config()

model = ChatOpenAI(model="gpt-4o-mini")

memory = MemorySaver()
workflow = StateGraph(state_schema=MessagesState)

config = {"configurable": {"thread_id": "abc123"}}


def call_model(state: MessagesState):
    result = model.invoke(state["messages"])
    #print("result >> ", result)
    return {"messages": result}


workflow.add_edge(START, "model")
workflow.add_node("model", call_model)
app = workflow.compile(checkpointer=memory)


def invoke_app(input_message: str):
    input_messages = [HumanMessage(input_message)]
    output = app.invoke({"messages": input_messages}, config)
    return output["messages"][-1].content


def run():
    while True:
        user_prompt = input("Chat>:")
        if user_prompt == "q":
            break
        output = invoke_app(user_prompt)
        print(output)


if __name__ == '__main__':
    run()