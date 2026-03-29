from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio


load_dotenv()

async def main():
    client = MultiServerMCPClient({
        "Math":{
            "command":"python",
            "args":["mathserver.py"],
             "transport":"stdio" 
        },
        "Weather":{
            "url":"http://localhost:8000/mcp",
            "transport":"streamable-http"
        }
    })
    os.getenv("OPENAI_API_KEY")
    tools = await client.get_tools()
    model = ChatOpenAI(model="gpt-4o-mini")
    agent = create_agent(model, tools)
    math_result = await agent.ainvoke({"messages": [{"role": "user", "content": "What is the weather in pakistan"}]})
    print("Math Result:", math_result["messages"][-1].content)

asyncio.run(main())