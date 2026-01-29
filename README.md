# The Goal

## Disaster Response & Relief Coordination System

This project builds a decentralized intelligent system to coordinate emergency response after disasters like floods, earthquakes, or fires. When disasters strike, centralized control systems often fail or become overwhelmed. This system uses autonomous software agents that work together to detect disasters, assess damage, perform rescues, and manage limited resources. The system includes four types of agents. Sensor agents detect and report disaster conditions. Rescue agents perform emergency operations. Logistics agents manage relief supplies. A coordinator agent assigns tasks and sets priorities. The agents communicate using standard messaging protocols and make decisions independently while coordinating with each other. Built using Python and the SPADE framework, the system demonstrates how distributed artificial intelligence can solve real world problems. The final system will autonomously detect disasters, allocate rescue tasks, manage resources, and adapt to changing conditions without relying on centralized control.

## Objectives

1. 1st objective is to configure and deploy a basic agent using SPADE and XMPP
SPADE: Smart Python Agent Development Environment
XMPP: Extensible Messaging and Presence Protocol

2. Implement agent perception of environmental and disaster-related events


# Quick References

## Installation (in codebase-helps avoid internal sub process rust package error)
```bash
python3 -m pip install spade python-dotenv
# python3 -m pip freeze > requirements.txt
```

## Running the Agents
```bash
# Run the spade server
spade run

# end busy port
lsof -i :5222 #returns PID
kill -9 <PID>

# Run the agent script
python3 rb.py

# Press Ctrl+C to stop the agents
```

**Note:** This script uses SPADE's embedded XMPP server, so no separate server setup is needed.