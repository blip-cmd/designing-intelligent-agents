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
            # 1. Simulate Raw Environmental Metrics (Sensors)
            # In a real disaster, these would be physical sensor readings(TODO: define agent environment and update sensors)
            water_level = random.uniform(0, 5.0)  # meters
            temperature = random.uniform(20, 100) # Celsius
            smoke_index = random.uniform(0, 100)  # %

            # 2. Logic-Based Perception (Control System)
            # Map raw metrics to severity levels based on defined thresholds
            if water_level > 4.0 or smoke_index > 80:
                event = "Critical Damage"
            elif water_level > 2.5 or temperature > 60:
                event = "Severe Damage"
            elif water_level > 1.0 or temperature > 40:
                event = "Mild Damage"
            else:
                event = "Safe"

            # 3. Create Perceptual Log Entry
            timestamp = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")
            # Including raw data in the log for better auditability
            metrics_str = f"W:{water_level:.1f}m, T:{temperature:.1f}C, S:{smoke_index:.1f}%"
            log_entry = f"[LOG][SENSOR AGENT][{timestamp}] {event} detected. Raw Metrics: ({metrics_str})"
            
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