import struct

#EXO 1
print("Exo 1")

def lire_fichier(fichier):
    with open(fichier, "rb") as f:
        data = f.read()
    l = len(data[44:])
    num_samples = l // 4
    gauche = []
    droite = []
    for i in range(num_samples):
        # 2 premiers : la gauche et 2 derniers : la droite
        (l,r) = struct.unpack_from('hh', data, 44 + i * 4)
        gauche.append(l)
        droite.append(r)
    return (gauche, droite)

a = lire_fichier("the_wall.wav")[0]
b = lire_fichier("the_wall.wav")[1]
print(a,b)

#EXO 2
print("Exo 2")
def ecrire_fichier(gauche,droite,filename):
    with open(filename,"wb")as f:
        f.write(b"RIFF")
        f.write(struct.pack("I",44-8+len(gauche)*4))
        f.write(b"WAVEfmt")
        f.write(struct.pack("IHHIIHH",16,1,2,44100,176400,4,16))
        f.write(b"data")
        f.write(struct.pack("I",len(gauche)*4))
        for i in range(len(gauche)):
            f.write(struct.pack("hh",gauche[i],droite[i]))

ecrire_fichier(a,b,"the_wall_bis.wav")

#Comme vu avec vous pendant le TD, le fichier .wav créé ne fonctionne pas alors que j'ai le même code que vous ( sûrement dû à MacOS )
       
#EXO 3
print("Exo 3")

def lire_fichierEXO3(fichier):
    with open(fichier, "rb") as f:
        data = f.read()
    l = len(data[44:])
    num_samples = l // 4
    gauche = []
    droite = []
    for i in range(0,num_samples,2):
        # 2 premiers : la gauche et 2 derniers : la droite
        (l,r) = struct.unpack_from('hh', data, 44 + i * 4)
        gauche.append(l)
        droite.append(r)
    return (gauche, droite)
    
aa = lire_fichierEXO3("the_wall.wav")[0]
bb = lire_fichierEXO3("the_wall.wav")[1]
print(aa,bb)
lire_fichierEXO3("the_wall.wav")
ecrire_fichier(aa,bb,"the_wall_demi.wav")
    



