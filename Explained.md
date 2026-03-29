# Understanding MCP servers

MCP servers are programs that expose specific capabilities to AI applications through standardized protocol interfaces.
Common examples include file system servers for document access, database servers for data queries, 
GitHub servers for code management, Slack servers for team communication, and calendar servers for scheduling.





##  Core Server Features

1)Tool
2)Resources
3)Prompt


# Understanding MCP clients

MCP clients are instantiated by host applications to communicate with particular MCP servers.
The host application, like Claude.ai or an IDE, manages the overall user experience and coordinates multiple clients. 
Each client handles one direct communication with one server.
Understanding the distinction is important: the host is the application users interact with, 
while clients are the protocol-level components that enable server connections.

## Core Client Features
1)Elicitation
2)Roots
3)Sampling
