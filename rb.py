import spade
import asyncio
import random
import datetime

class HelloAgent(spade.agent.Agent):
    async def setup(self):
        print("agent.rb says hi!")

class SensorAgent(spade.agent.Agent):
    async def setup(self):
        print("SensorAgent started")
        self.add_behaviour(self.SensorBehaviour(period=7))

    class SensorBehaviour(spade.behaviour.PeriodicBehaviour):
        async def on_start(self):
            print("SensorBehaviour started")

        async def run(self):
            severity_levels =["Safe", "Mild Damage", "Severe Damage", "Critical Damage"]
            event = random.choice(severity_levels)

            # Create timestamp 
            timestamp = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")
            log_entry = f"[LOG][SENSOR AGENT][{timestamp}] Disaster event detected: {event}"
            
            print(log_entry)
            # Append to file 
            with open("logs/log-sensor-agent.txt", "a") as f:
                f.write(log_entry + "\n")

        async def on_end(self):
            print("SensorBehaviour ended")

async def main():
    agent = HelloAgent("blip@xmpp.jp", "Niiola70$$xmpp")
    sensor_agent = SensorAgent("blip1@xmpp.jp", "Niiola70$$xmpp")
    await agent.start()
    await sensor_agent.start()
    await asyncio.sleep(20)
    await agent.stop()
    await sensor_agent.stop()

if __name__ == "__main__":
    asyncio.run(main())