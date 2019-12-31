class Delete(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def fossil(self, ctx):
        fossil_list = ["Fusulinida","Nummulites","Astraeospongia","Hydnoceras","Archimedes","Rhombopora","Dendroidea","Graptoloidea","Favosites","Halysites","Heliophyllum","Hexagonaria","Septastraea","Eurypterida","Cryptolithus","Calymene","Elrathia","Isotelus","Eldredgeops","Lingula","Atrypa","Composita","Juresania","Leptaena","Mucrospirifer","Platystrophia","Rafinesquina","Rhynchonellida","Exogyra","Gryphaea","Pecten","Glycymeris","Astarte","Nucula","Goniatitida","Ceratitida","Baculites","Dactylioceras","Belemnitella","Nautilida","Orthocerida","Conus","Cypraea","Platyceras","Turritella","Worthenia","Asteroidea","Pentremites","Crinoidea","Echinoidea","Ophiuroidea","SuperAgnatha","Bothriolepis","Dunkleosteus","Otodus","Carcharocles","C. megalodon","SuperBatoidea","Knightia","Xiphactinus","Eusthenopteron","Latimeria","Tiktaalik","Acanthostega","Eryops","Diplocaulus","Crocodilia","Testudines","Ichthyosauria","Mosasauridae","Plesiosauria","Pterosauria","Allosaurus","Coelophysis","Dilophosaurus","Spinosaurus","Tyrannosaurus","Velociraptor","Brachiosaurus","Diplodocus","Patagotitan","Plateosaurus","Ankylosaurus","Triceratops","Protoceratops","Iguanodon","Parasaurolophus","Maiasaura","Dracorex","Stegosaurus","Archaeopteryx","Titanis","Ichthyornis","Dimetrodon","Lystrosaurus","Basilosaurus","Equus","Australopithecus","H. neanderthalensis","H. erectus","H. sapien","Mammut","M. primigenius","Megacerops","Mesohippus","Smilodon","Acer","Populus","Platanus","Ginkgo","Lepidodendron","Metasequoia","Calamites","Glossopteris","Psaronius","Coprolites","Stromatolites","Amber/copal","Petrified wood","Coquina","Limestone","Sandstone","Shale","Chert"]
        specimen = random.choice(fossil_list)
        img = random.choice(os.listdir(f'{os.getcwd()}\\data\\images\\{specimen}'))
        await ctx.send("Getting Image...")
        with open(f'{os.getcwd()}\\data\\images\\{specimen}\\{img}', 'rb') as f:

            picture = discord.File(f)
            await ctx.send(file=picture)
        db.writefossil(ctx.message.author.id, specimen)

def setup(bot):
    bot.add_cog(Fossil(bot))