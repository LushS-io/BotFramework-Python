# Troy Kirin edition

import datetime
import asyncio
import warnings
from typing import List, Callable

from botbuilder.schema import (
    Activity,  # the activity of a bot
    ActivityTypes,  # types of activites bot can handle, such as text, audio, image
    ChannelAccount,  # the channel type working with "facebook messenger"
    ConversationAccount,  # conversation ID?
    ResourceResponse,  # hold context?
    ConversationReference,
)
from botbuilder.core.turn_context import (
    TurnContext
)

from botbuilder.core.bot_adapter import (BotAdapter)


# Object Oriented Programming
# Object of ConsoleAdapter taking in the BotAdapter Object imported from BotBuilder Core
class ConsoleAdapter(BotAdapter):
    """
    Adapter to communicate with bot via console window

    - Example - 
    import asyncio
    from botbuilder.core import ConsoleAdapter

    async def logic(context):
        await context.send_activity("hello world!)

    # the adapter we are using is for the console, this could be a browser type or adatper to something like Telegram / Facebook Messenger
    adapter = ConsoleAdapter() # instanciate the adapter and save to var

    loop = asyncio.get_event_loop()
    if __name__ == "__main__":
        try:
            loop.run_until_complete(adapter.process_activity(logic))
        except KeyboardInterupt:
            pass
        finally:
            loop.stop()
            loop.close()
    """

    # __init__ is a special function that
    def __init__(self, reference: ConversationReference = None):
        super(ConsoleAdapter, self).__init__()  # TODO ; learn what this means

        # possibly a self reference to the reference object to come in
        # which is a key, value (dict)
        self.reference = ConversationReference(
            # the id of conversation channel taking place
            channel_id="console",

            # the account that is either user or bot that sits within a channel
            user=ChannelAccount(id="user", name="User1"),

            # save as above but this is the bot channel itself,
            # imagine the ability to have a channel with multi bot.
            bot=ChannelAccount(id="bot", name="Bot"),

            # TODO: side project """
            #     one user that enters a channel with two bots in the room
            #     what would this do?
            #     Could the bot then just be able to both talk to other bot
            #  say one is finance and one is healthcare
            #     the different bots would then handle various questions,
            #     this would segment the difference and handling of data
            # permissions

            #     """the user would not know the difference if the bots know
            #  (through orchestration how to handle when an incoming activity
            # triggers both bots. maybe ask a clarifying question to determine
            # which bot should be used. -> this leads to bot hand-off. when a
            # healthcare bot then needs to transfer to finance bot. what data
            # log and conversation information would be preseved between the
            #  two? how do we ensure a user experience that the user
            # understands and trusts the bot? So multi-bot with one name,
            # with different skills.)
            # """

            conversation=ConversationAccount(
                id="convo1", name="", is_group=False),
            service_url="",

        )

        # warn that users need to pass in a conversation reference instance,
        # otherwise DEBUG: "parameter ignored"
        # checking if isinstance of reference a ConversationReference

        # Warn users to pass in an instance of a ConversationReference,
        # otherwise the parameter will be ignored.

        # check if there is a conversation reference meaning,
        #  not a new conversation?
        if reference is not None and not isinstance(
                reference,
                ConversationReference):
            # .then() the conditional is done to check if x is not y...
            # .then()
            warnings.warn(
                "ConsoleAdapter: 'reference' argument is not an instance of"
                "ConversationReference and will be ignored."
            )
        else:  # if it is the proper instance "reference"
            self.reference.channel_id = getattr(
                reference,
                "channel_id",
                self.reference.channel_id
            )
            self.reference.user = getattr(
                reference,
                "user",
                self.reference.user

            )
            self.reference.bot = getattr(
                reference,
                "bot",
                self.reference.bot
            )
            self.reference.conversation = getattr(
                reference,
                "conversation",
                self.reference.conversation

            )
            self.reference.service_url = getattr(
                reference,
                "service_url",
                self.reference.service_url

            )

            # Different case
            # self.reference only has one attribute if nothing was initalized;
            # which is.. activity_id
            # so that is why..
            # have a value for default id for self.reference.activity_id to
            # None type

            # The only attribute on self.reference without an initial value is activity_id, so if reference does not
            # have a value for activity_id, default self.reference.activity_id to None
            self.reference.activity_id = getattr(
                reference, "activity_id", None
            )

        self._next_id = 0

        pass

    async def process_activity(self, logic: Callable):
        """
        Begins listening to console input
        :param logic:
        :return:
        """
        while True:
            msg = input()
            if msg is None:
                pass
            else:
                self._next_id += 1
                activity = Activity(
                    text=msg,
                    channel_id="console",
                    from_property=ChannelAccount(id="user", name="User1"),
                    recipient=ChannelAccount(id="bot", name="Bot"),
                    conversation=ConversationAccount(id="Convo1"),
                    type=ActivityTypes.message,
                    timestamp=datetime.datetime.now(),
                    id=str(self._next_id),
                )

                activity = TurnContext.apply_conversation_reference(
                    activity,
                    self.reference,
                    True
                )
                context = TurnContext(self, activity)
                await self.run_pipeline(context, logic)

    async def send_activities(self, context: TurnContext, activities: List[Activity]) -> List[ResourceResponse]:
        """
        Logs a series of activites to the console
        :param context:
        :param activites:
        :return:
        """

        if context is None:
            raise TypeError(
                "ConsoleAdapter.send_activites(): `conexxt` argument cannot be None"
            )
        if not isinstance(activities, list):
            raise TypeError(
                "ConsoleAdapter.send_activites(): `activites` arguemnt must be a list."
            )

        if len(activities) == 0:
            raise ValueError(
                "ConsoleAdapter.send_activites(): `activites` argument cannot have a length of 0."
            )

        async def next_activity(i: int):
            responses = []

            if i < len(activities):
                responses.append(ResourceResponse())
                activity = activities[i]

                if activity.type == "delay":
                    await asyncio.sleep(activity.delay)
                    await next_activity(i + 1)
                elif activity.type == ActivityTypes.message:
                    if (
                        activity.attachments is not None
                        and len(activity.attachments) > 0
                    ):

                        append = (
                            "(1 attachment)"
                            if len(activity.attachments) == 1
                            else f"({len(activity.attachmets)} attachments)"
                        )
                        print(f"{activity.text} {append}")

                    else:
                        print(activity.text)
                    # await for next activity in this case keyboard input
                    await next_activity(i+1)

                else:
                    print(f"[{activity.type}]")
                    await next_activity(i + 1)
            else:
                return responses

        await next_activity(0)

    async def delete_activity(
        self, context: TurnContext, reference: ConversationReference
    ):
        """
        """
        raise NotImplementedError(
            "ConsoleAdapter.delete_activity(): not supported.")

    async def update_activity(self, context: TurnContext, activity: Activity):
        raise NotImplementedError(
            "ConsoleAdapter.update_activity(): not supported.")
