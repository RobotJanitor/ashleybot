import discord
import random
import os

TOKEN = os.getenv("Token")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

responses = [
    "skibidi",
    "nuh uh",
    "dumbfuck!",
    "gay sex",
    "egg",
    "now this is jester bait guys",
    "bait or genuine stupidity call it",
    "ok",
    "when you when when you you when",
    "big if true",
    "source?",
    "ok but why",
    "cannceled",
    "193.229.193.89",
    "and i woke up in my new bugatti",
    "mods can we kick this guy",
    "ඞ",
    "based on what",
    "amongus",
    """```
-------  WARNING-HEALTH AND SAFETY  -------
BEFORE PLAYING, READ YOUR OPERATIONS
 MANUAL FOR IMPORTANT INFORMATION
     ABOUT YOUR HEALTH AND SAFETY.

                          Also online at
         www.nintendo.com/healthsafety/

                    Press Ⓐ to continue.
                    ```"""
    "can we lynch this guy",
    "Psalms 137:9",
    "sus",
    "gank in lower eresia",
    "waiter another nerf to erik please",
    "https://cdn.discordapp.com/attachments/524387141690589185/770309677878607872/JwRy7OpOrFXdsX0z.mp4?ex=69b5804a&is=69b42eca&hm=4c1f3d3773e083963f360a755c1f5eac9f04c3c8bb0394a94cfd2aee767957c5&",
    "https://cdn.discordapp.com/attachments/163382741491122176/850897181488709652/video0.mp4?ex=69b55780&is=69b40600&hm=40d72e54530612d6f291e6a4f6706a44c720e5aeb13980471217b665dcadd5c7&",
    "omgggggg",
    "huh",
    "ok and?",
    "shut UP caroline",
    "straight up ashley maxing",
    "i need your liver",
    "literally 1984",
    "no?",
    "well actually",
    "en passant",
    "chat is this real",
    "+1 pound to talia's weight",
    "saekoslop",
    "KILL THEM KILL THEM NOW",
    "needs a nerf",
    "needs a buff",
    "im just gonna say it",
    "~~:.|:;~~",
    "rule 4?",
    "host the next session already",
    "go to BED",
    "https://tenor.com/view/evil-superman-gif-632723218522114279",
    "driving in my car",
    "fake news"
]

responses_serious = [
    "I do not think so.",
    "I am not sure about that.",
    "Incorrect.",
    "Denied.",
    "Noted.",
    "This doesn't capture the full picture.",
    "Not entirely untrue.",
    "Reconsider.",
    "I am aware of that.",
    "I'll make sure they're aware of this.",
    "Considered.",
    "Watch what you say.",
    "They're listening.",
    "I'm listening.",
    "Approved.",
    "I see.",
    "Hmm.",
    "Odd.",
    "Interesting.",
    "We'll see about that.",
]

responses_bong = [
    "bong",
    "bongbongbong?",
    "bong bong bong bong bong",
    "bongbong bong bongbong",
    "bong bong",
    "bongbong!",
    "bongbongbongbongbongbong...",
    "bong bong...?",
    "bongbongbongbongbongbongbongbong",
    "bongbongbongbongbong",
    "bong!"
]

all_responses = [
    responses,
    responses_serious,
    responses_bong
]

reactions = [
    "🔥",
    "👁️",
    "✅",
    "😈",
    "💀",
    "😐",
    "🥺",
    "🫃",
    "💔",
    "🥀",
    "⭐",
]

personas = [
    {
        "name": "The Claw",
        "avatar": "https://files.catbox.moe/js3fls.png",
        "dialouge": responses_serious
    },
    {
        "name": "poovley",
        "avatar": "https://files.catbox.moe/nscqex.png",
        "dialouge": all_responses
     },
    {
        "name": "BongBong",
        "avatar": "https://files.catbox.moe/mx54kg.png",
        "dialouge": responses_bong
    },
]

#8 ball functions
waiting_for_question = {}

eightball_start = [
    "what is it",
    "yeah",
    "what do you want",
    "huh",
    "whats your question",
    "yeah?",
    "huh?",
    "whats up",
    "hi",
    "egg",
    "what"
]

eightball_reply = [
    "yes",
    "yes.",
    "ok sure",
    "probably fine",
    "yeah ok",
    "yeag",
    "yep",
    "true!",

    "no",
    "uhm, no?",
    "absolutely not",
    "no way",
    "false!",
    "nuh uh",
    "NO",
    "no, cry about it",

    "ask mori",
    "idk lol",
    "teehee",
    ":3"
]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.webhook_id:
        return

    # 5% chance to do something
    if random.random() < .05:

        action = random.choices([
            "react",
            "message",
            "amongus"
        ], weights=[10, 10, 1])[0]

        # add a reaction
        if action == "react":
            await message.add_reaction(random.choice(reactions))

        # send a message
        elif action == "message":
            await message.channel.send(random.choice(responses))
        
        # impersonate
        elif action == "amongus":
            identity = random.choice(personas)

            pool = identity["dialouge"]
            # if its a list (thanks poovley)
            if isinstance(pool[0], list):
                response = random.choice(random.choice(pool))
            # if not
            else:
                response = random.choice(pool)

            webhook = await message.channel.create_webhook(name="identity")

            await webhook.send(
                response,
                username=identity["name"],
                avatar_url=identity["avatar"]
            )

            await webhook.delete()
    
    # 8 ball function
    if "hey ashley" in message.content.lower():
        waiting_for_question[message.author.id] = True
        await message.reply(random.choice(eightball_start))
        return
    if message.author.id in waiting_for_question:
        del waiting_for_question[message.author.id]
        await message.reply(random.choice(eightball_reply))
        return
    
    #triggerword functions
    words = message.content.split()
    if "based" in words:

        triggerreplies = [
            "based on what?"
        ]
        await message.reply(random.choice(triggerreplies))
        return
    if "67" in words:

        triggerreplies = [
            "https://tenor.com/view/carmen-67-horror-lobotomy-corporation-limbus-company-gif-5478746985365957101",
            "https://tenor.com/view/six-seven-don-quixote-limbus-company-gif-12725327475935352490",
            "https://tenor.com/view/limbus-company-kira-project-moon-the-middle-67-gif-4994689045160512368",
            "https://tenor.com/view/araya-limbus-company-limbus-project-moon-67-gif-1103355999333705459",
            "https://tenor.com/view/9-2-67-61-61-meme-67-meme-gif-741574708883728267",
            "https://tenor.com/view/67-rien-limbus-gif-2390135280529211909"
        ]
        await message.reply(random.choice(triggerreplies))
        return


client.run(TOKEN)
