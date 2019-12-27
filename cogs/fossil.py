import random
import os
from data import db
import discord
from discord.ext import commands

class Fossil(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    async def fossil(self, ctx):
        fossil_list = ["Order Fusulinida","Genus Nummulites","Genus Astraeospongia","Genus Hydnoceras","Genus Archimedes","Genus Rhombopora","Order Dendroidea","Order Graptoloidea","Genus Favosites","Genus Halysites","Genus Heliophyllum","Genus Hexagonaria","Genus Septastraea","Order Eurypterida","Genus Cryptolithus","Genus Calymene","Genus Elrathia","Genus Isotelus","Genus Eldredgeops","Genus Lingula","Genus Atrypa","Genus Composita","Genus Juresania","Genus Leptaena","Genus Mucrospirifer","Genus Platystrophia","Genus Rafinesquina","Order Rhynchonellida","Genus Exogyra","Genus Gryphaea","Genus Pecten","Genus Glycymeris","Genus Astarte","Genus Nucula","Order Goniatitida","Order Ceratitida","Genus Baculites","Genus Dactylioceras","Genus Belemnitella","Order Nautilida","Order Orthocerida","Genus Conus","Genus Cypraea","Genus Platyceras","Genus Turritella","Genus Worthenia","Class Asteroidea","Genus Pentremites","Class Crinoidea","Class Echinoidea","Class Ophiuroidea","Superclass Agnatha","Genus Bothriolepis","Genus Dunkleosteus","Genus Otodus","Genus Carcharocles","Species C. megalodon","Superorder Batoidea","Genus Knightia","Genus Xiphactinus","Genus Eusthenopteron","Genus Latimeria","Genus Tiktaalik","Genus Acanthostega","Genus Eryops","Genus Diplocaulus","Order Crocodilia","Order Testudines","Order Ichthyosauria","Family Mosasauridae","Order Plesiosauria","Order Pterosauria","Genus Allosaurus","Genus Coelophysis","Genus Dilophosaurus","Genus Spinosaurus","Genus Tyrannosaurus","Genus Velociraptor","Genus Brachiosaurus","Genus Diplodocus","Genus Patagotitan","Genus Plateosaurus","Genus Ankylosaurus","Genus Triceratops","Genus Protoceratops","Genus Iguanodon","Genus Parasaurolophus","Genus Maiasaura","Genus Dracorex","Genus Stegosaurus","Genus Archaeopteryx","Genus Titanis","Genus Ichthyornis","Genus Dimetrodon","Genus Lystrosaurus","Genus Basilosaurus","Genus Equus","Genus Australopithecus","Species H. neanderthalensis","Species H. erectus","Species H. sapien","Genus Mammut","Species M. primigenius","Genus Megacerops","Genus Mesohippus","Genus Smilodon","Genus Acer","Genus Populus","Genus Platanus","Genus Ginkgo","Genus Lepidodendron","Genus Metasequoia","Genus Calamites","Genus Glossopteris","Genus Psaronius","Coprolites","Stromatolites","Amber/copal","Petrified wood","Coquina","Limestone","Sandstone","Shale","Chert"]
        specimen = random.choice(fossil_list)
        img = random.choice(os.listdir(f'{os.getcwd()}\\data\\images\\{specimen}'))
        await ctx.send("Getting Image...")
        with open(f'{os.getcwd()}\\data\\images\\{specimen}\\{img}', 'rb') as f:

            picture = discord.File(f)
            await ctx.send(file=picture)
        db.writeplaintext(ctx.message.author.id, specimen)

def setup(bot):
    bot.add_cog(Fossil(bot))
