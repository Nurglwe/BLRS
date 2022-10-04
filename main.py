import discord,os,json,tools,keepalive,requests,datetime
from better_profanity import profanity
from discord.ext import commands
from discord.ext import tasks
intents = discord.Intents.default()
intents = discord.Intents.default()
intents.presences = True
intents.members = True
client = discord.Client(intents=intents, guilds=True, members=True)


#no touch above (*cough* future me)

#Commenting in progress
#Contact me on discord at Nurglwe#8387 if you want 
profanity.load_censor_words()
client = commands.Bot(command_prefix="->")
'''

Below is events

'''

@client.event
async def on_ready():
  print("Ready")
  remind.start()


'''

Below is commands

'''

def view(actions=None, attachments=None, attachment_fields=None, stickers=None, members=None, member_fields=None, checkItemStates=None, checklists=None, limit=None, since=None, before=None, filter=None, fields=None, customFieldItems=None):
  resp = requests.get(f"https://trello.com/1/boards/GGtwifeZ/cards", params={"key": os.getenv("TRKEY"), "token": os.getenv("TRTKN"), "actions": actions, "attachments": attachments, "attachment_fields": attachment_fields, "stickers": stickers, "members": members, "member_fields": member_fields, "checkItemStates": checkItemStates, "checklists": checklists, "limit": limit, "since": since, "before": before, "filter": filter, "fields": fields, "customFieldItems": "true" if customFieldItems else None}, data=None)
  b=resp.json()
  tgt = ["Backlog","To Do","Doing"]
  li = []
  for i in b: 
    if i["name"] == "Done":
      break
    elif not(i["name"] in tgt):
      li.append({i["name"]:i["desc"]})
    else:
      li.append({"--":i["name"]})
  return li


@tasks.loop(minutes = 5)
async def remind():
  with open("file.txt") as f:
    data = f.readlines()
    print(data)
    print(round(datetime.datetime.timestamp(datetime.datetime.now())))
  if int(round(datetime.datetime.timestamp(datetime.datetime.now()))) > int(data[0]):
    guilds=client.guilds
    print(guilds)
    gu = discord.utils.get(guilds,id=522098642362957847)
    a=await gu.fetch_member(220213079944724482)
    li = view()
    for i in li:
      await a.send(str(list(i.keys())[0])+"\n"+str(list(i.values())[0]))
    with open("file.txt","w") as f:
      print(str(round(datetime.datetime.timestamp(datetime.datetime.now()))+24*60*60))
      f.write(str(round(datetime.datetime.timestamp(datetime.datetime.now()))+24*60*60)) 
  else:
    print('False',int(round(datetime.datetime.timestamp(datetime.datetime.now()))) < int(data[0]) )

@client.command()
async def forcestart(ctx):
  with open("file.txt") as f:
    data = f.readlines()
  print(data)
  print(round(datetime.datetime.timestamp(datetime.datetime.now())))
  guilds=client.guilds
  print(guilds)
  gu = discord.utils.get(guilds,id=522098642362957847)
  a=await gu.fetch_member(220213079944724482)
  li = view()
  print(li)
  for i in li:
    print(i)
    await a.send(str(list(i.keys())[0])+"\n"+str(list(i.values())[0]))


@client.command()
async def start(ctx):
  remind.start()

@client.command()
async def ping(ctx):
    await ctx.send('Pong, {} Ms'.format(round(client.latency * 1000,2)))


#Don't touch below
keepalive.keep_alive()
token=os.getenv('DSTOKEN')
client.run(token)