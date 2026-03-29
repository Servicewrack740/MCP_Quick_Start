from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city:str) -> str:
    """Get the current weather for a given city."""
    return f"The current weather in {city} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")