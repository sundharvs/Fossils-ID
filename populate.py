from google_images_download import google_images_download
import os

response = google_images_download.googleimagesdownload()
fossil_list = ["Fusulinida","Nummulites","Astraeospongia","Hydnoceras","Archimedes","Rhombopora","Dendroidea","Graptoloidea","Favosites","Halysites","Heliophyllum","Hexagonaria","Septastraea","Eurypterida","Cryptolithus","Calymene","Elrathia","Isotelus","Eldredgeops","Lingula","Atrypa","Composita","Juresania","Leptaena","Mucrospirifer","Platystrophia","Rafinesquina","Rhynchonellida","Exogyra","Gryphaea","Pecten","Glycymeris","Astarte","Nucula","Goniatitida","Ceratitida","Baculites","Dactylioceras","Belemnitella","Nautilida","Orthocerida","Conus","Cypraea","Platyceras","Turritella","Worthenia","Asteroidea","Pentremites","Crinoidea","Echinoidea","Ophiuroidea","SuperAgnatha","Bothriolepis","Dunkleosteus","Otodus","Carcharocles","C. megalodon","SuperBatoidea","Knightia","Xiphactinus","Eusthenopteron","Latimeria","Tiktaalik","Acanthostega","Eryops","Diplocaulus","Crocodilia","Testudines","Ichthyosauria","Mosasauridae","Plesiosauria","Pterosauria","Allosaurus","Coelophysis","Dilophosaurus","Spinosaurus","Tyrannosaurus","Velociraptor","Brachiosaurus","Diplodocus","Patagotitan","Plateosaurus","Ankylosaurus","Triceratops","Protoceratops","Iguanodon","Parasaurolophus","Maiasaura","Dracorex","Stegosaurus","Archaeopteryx","Titanis","Ichthyornis","Dimetrodon","Lystrosaurus","Basilosaurus","Equus","Australopithecus","H. neanderthalensis","H. erectus","H. sapien","Mammut","M. primigenius","Megacerops","Mesohippus","Smilodon","Acer","Populus","Platanus","Ginkgo","Lepidodendron","Metasequoia","Calamites","Glossopteris","Psaronius","Coprolites","Stromatolites","Amber","Petrified wood","Coquina","Limestone","Sandstone","Shale","Chert"]


for specimen in fossil_list:
    arguments = {"keywords":(specimen + " fossil"), "limit":100, "output_directory": "./data/images", "thumbnail_only": True}   #creating list of arguments
    response.download(arguments)   #passing the arguments to the function
	
for root, dirs, files in os.walk("./data/images"):
    for dir in dirs:
        if(dir[-9:] != "thumbnail"):
            os.removedirs(f'./data/images/{dir}')
    
    for dir in dirs:
        os.rename(f'./data/images/{dir}', f'./data/images/{dir[:-11]}')
