from main import TOKEN
import discord
from discord.ext import commands, tasks
import random
from ai import AI



intents = discord.Intents.all() #permissões para o bot
bot = commands.Bot(command_prefix="!", intents=intents) #prefixo para os comandos do bot
ai = AI()
bot.modo_chato = True

#-----------------------eventos---------------------

@bot.event 
async def on_ready():
    print(f"{bot.user} está online!")

    #sincronizando os comandos de barra

    sincronizar = await bot.tree.sync()
    print(f"Sincronizado {len(sincronizar)} comandos")

    #------------------------------------


@bot.event
async def on_message(messagem: discord.Message):
    if messagem.author.bot:
        return 
    
    if messagem.content.startswith(bot.command_prefix):
        await bot.process_commands(messagem) #processa os comandos normalmente
        return
    #-----------------------respostas padrao---------------------
    mensagem_random = {
        "respostas_padrao":["Cala-boca noob", "Vai te fuder", "Calado"],
        }
    
    respostas = {
        "para com isso": f"Desculpa {messagem.author.mention}",
        "vou chorar": f"Desculpa {messagem.author.mention}",
        "chupa meu piuzinho": f"chupando piruzão do {messagem.author.mention}",
    }   

    if bot.modo_chato == True:

        for men, res in respostas.items():
            if men in messagem.content.lower():
                await messagem.reply(res)
                return

        
        await messagem.reply(f"{random.choice(mensagem_random['respostas_padrao'])} {messagem.author.mention}!")

    #---------------------------------------------------------------

@bot.event
async def on_member_join(member: discord.Member):
    try:
        canal = bot.get_channel(1063271661551497266)
        mensagens  = ["alah! Mais um fracassado!", "Bem-vindo, seu merda!", "Bem-vindo, sua gostosa!"]

        await canal.send (f'{member.mention} {random.choice(mensagens)}')
    except Exception as e:
        print(f"Erro ao enviar mensagem de boas-vindas: {e}")


#----------------criando comandos-------------------

@bot.command()
async def ping(ctx: commands.Context, *,texto: str): 
    nome = ctx.author.name
    await ctx.reply(f"nigger, {nome}!") 
    await ctx.send(texto)



#---------------------embed-------------------------

@bot.command()
async def hiro(ctx: commands.Context):
    meu_embed = discord.Embed()
    meu_embed.title = "Esse é o Hiro real"
    meu_embed.description = "O Hiro tem esse rosto aqui"
    meu_embed.color = discord.Color.blue()
    imagem = discord.File("yoshie.png", "death.png")
    meu_embed.set_image(url="attachment://death.png")
    meu_embed.set_thumbnail(url="attachment://death.png")
    meu_embed.set_footer(text="Esse é o Hiro real")


    await ctx.reply(embed=meu_embed, file=imagem)

@bot.command()
async def bluezao(ctx, membro: discord.Member):
    imagem = discord.File("bluezao.png", "bluezao.png")
    bluezaoembed = discord.Embed()
    bluezaoembed.title = f"{membro.name} na vida real"
    bluezaoembed.description = f"{membro.mention}, é um merda na vida real"
    bluezaoembed.color = discord.Color.red()
    bluezaoembed.set_thumbnail(url=membro.avatar.url)
    bluezaoembed.set_image(url="attachment://bluezao.png")
    bluezaoembed.set_author(name="Bluezao")
    await ctx.reply(embed=bluezaoembed, file=imagem)

@bot.command()
async def calar_se(ctx: commands.Context):
    await ctx.reply(f"Vou ficar calado {ctx.author.mention}")
    bot.modo_chato = False
    return bot.modo_chato


@bot.command()
async def acorda(ctx: commands.Context):
    await ctx.reply(f"{ctx.author.mention} fala aí linda!")
    bot.modo_chato = True
    return bot.modo_chato


@bot.command()
async def pergunta(ctx: commands.Context, *, pergunta: str):
    try:    
        resposta = ai.prompt(pergunta=pergunta)
          
        await ctx.reply(f"Para o(a) {ctx.author.mention}: {resposta}")

    except Exception as e:
        print(f"Erro ao obter resposta da IA: {e}")





#--------------------tasks---------------------------

@tasks.loop(seconds=10)
async def mensagem_loop():
    canal = bot.get_channel(1504306703263334561)

    await canal.send("O Hiro me abusa todos os dias")



#-----------------command tree-----------------------

@bot.tree.command()
async def calar_se(interac: discord.Interaction):
    await interac.response.send_message(f"Vou ficar calado {interac.user.mention}")
    bot.modo_chato = False
    return bot.modo_chato

@bot.tree.command()
async def acorda(interac: discord.Interaction):
    await interac.response.send_message(f"{interac.user.mention} fala aí linda!")
    bot.modo_chato = True
    return bot.modo_chato


@bot.tree.command()
async def pergunta(interac: discord.Interaction, *, pergunta: str):
    try:
        await interac.response.defer(thinking=True)
    
        resposta = ai.prompt(pergunta=pergunta)
          
        
        await interac.followup.send(resposta)

    except Exception as e:
        print(f"Erro ao obter resposta da IA: {e}")


#--------------bot run----------------------------------

def main():
    bot.run(TOKEN)



if __name__ == "__main__":
    main()








