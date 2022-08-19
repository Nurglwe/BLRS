import discord,os,json,tools
from better_profanity import profanity
from discord.ext import commands



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

@client.event
async def on_message_delete(message):
  ato = tools.alltheobject(client)
  eb=tools.embedhandler("Deleted message",0x690AA9,ato.delc,False,client)
  await tools.embedhandler.sendembed(eb, {"Message deleted:":message.content,"Author:":message.author.name,"Author ID:":message.author.id,"Message ID:":message.id,"Link:":"https://discordapp.com/channels/{}/{}/{}".format(ato.guild.id,message.channel.id,message.id)})

@client.event
async def on_message_edit(beforemessage,aftermessage):
  if beforemessage.content != aftermessage.content:
    ato=tools.alltheobject(client)
    eb=tools.embedhandler("Deleted message",0xdf5fef,ato.delc,False,client)
    await tools.embedhandler.sendembed(eb,{"Message before:":beforemessage.content,"Message after:":aftermessage.content,"Author:":beforemessage.author.name,"Message author ID:":beforemessage.author.id,"Message ID:":beforemessage.id,"Message link:":"https://discordapp.com/channels/{}/{}/{}".format(ato.guild.id,beforemessage.channel.id,aftermessage.id)})
  else:
    print("Link / embed")
                                     
@client.event
async def on_raw_bulk_message_delete(payload):
  ato = tools.alltheobject(client)
  eb=tools.embedhandler("Mass / old message deletion",0xc20927,ato.delc,False,client)
  await tools.embedhandler.sendembed(eb,{"Message IDs:":payload.message_ids,"Amount of messages":len(payload.message_ids)})


'''

Below is commands

'''

@client.command()
async def ping(ctx):
    await ctx.send('Pong, {} Ms'.format(round(client.latency * 1000,2)))

@client.command()
@commands.has_role('Femboy')
async def purge(ctx,num:int):
  num = num+1
  await ctx.channel.purge(limit=num)




#Don't touch below
token=os.getenv('DSTOKEN')
client.run(token)