import spade
import asyncio

class HelloAgent(spade.agent.Agent):
    async def setup(self):
        print("agent.rb says hi!")

async def main():
    agent = HelloAgent("blip@xmpp.jp", "Niiola70$$xmpp")
    await agent.start()
    await asyncio.sleep(5)
    # await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())