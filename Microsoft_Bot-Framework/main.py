# main.py

# async library
import asyncio

# import EchoBot Object from bot
from bot import EchoBot

# from "adapter" package via __init__.py import the ConsoleAdapter
from adapter import ConsoleAdapter

# instanciate the BOT and ADAPTER
# Recall BOT is now an instance of the EchoBot Object...
# --- The Constructor is called for no param call
BOT = EchoBot()

# ADAPTER object...
# in this case a Console Adapter to communicate with bot via terminal
ADAPTER = ConsoleAdapter()

# Create event loop
LOOP = asyncio.get_event_loop()

# By default python will run from the 0 line when called.
# If python script is called by it's own name..by convention, then run this.
if __name__ == "__main__":
    try:  # try this except...
        # Greetings
        print("Hi I'm EchoBot, I can repeat what you say to me! Try ME :)")

        # Run the loop - unleesh the lava
        LOOP.run_until_complete(ADAPTER.process_activity(BOT.on_turn))

# if a keyboard interrupt happens
    except KeyboardInterrupt:
        pass

    finally:  # to finish off the try loop...run these to do a closedown
        LOOP.stop()  # stop event loop
        LOOP.close()  # close the loop
