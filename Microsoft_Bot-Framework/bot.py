# bot.py

# Library Imports
from sys import exit

# Object class called EchoBot


class EchoBot:
    # will have properties such as conversation_id, user name, bot name,
    #  session_url,
    # basically a bunch of handlers

    async def on_turn(self, context):
        # we want to take in the activity context and then do something with it
        # essentially in this case, "message handling?"

        # Check to see if this activity is an incoming message.
        # (It could theoretically be another type of activity.)
        if context.activity.type == "message" and context.activity.text:
            # check if quit statement was said
            if context.activity.text.lower() == "quit":
                # say adios
                await context.send_activity("Thanks for your time, bye!")
                exit(0)
            else:
                # reply with what was sent
                await context.send_activity(f"You said, the following... \n{context.activity.text}")

            # @GOAL
            # send the activity back out from bot to repeat the message
