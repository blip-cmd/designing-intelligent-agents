import spade
import asyncio
import random
import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env from project root
xmpp_password = os.getenv("pass") or "password"
os.makedirs("logs", exist_ok=True)

class HelloAgent(spade.agent.Agent):
    async def setup(self):
        print("Safety Officer R.B. on duty!")

class SensorAgent(spade.agent.Agent):
    #to simulate periodic sensor readings and log perceptual events
    #TODO: conditions will be updated after a redesign
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
    # # Create agents using SPADE's embedded XMPP server
    agent = HelloAgent("agent@localhost", "password")
    sensor_agent = SensorAgent("sensor_agent@localhost", "password")

    
    # agent = HelloAgent("blip@xmpp.jp", env.pass)
    # sensor_agent = SensorAgent("blip1@xmpp.jp", env.pass)
    
    await agent.start()
    await sensor_agent.start()
    
    print("Agents running. Press Ctrl+C to stop...")
    try:
        # Run indefinitely until interrupted
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping agents...")
    finally:
        await agent.stop()
        await sensor_agent.stop()

if __name__ == "__main__":
    spade.run(main())