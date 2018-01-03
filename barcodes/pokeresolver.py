with open('init_database.txt', 'r') as f:
    for i in range(18):
        f.readline()

    w = [[],[]]
    temp = []

    for i in range(210):
        if i < 200:
            l = f.readline()
            k = l.find('=')
            l = l[(k+2):]
            k = l.find(',')
            nazov = l[:(k-1)]
            l = l[(k+17):]
            staty = ['sila', 'rychlost', 'postreh', 'odolnost']
            for j in range(4):
                k = l.find('=')
                l = l[(k+1):]
                k = l.find(',')
                staty[j] = int(l[:k])
            if i+1 < 10:
                s = 'pokebar_00'+str(i+1)
            elif i+1 >= 10 and i < 100:
                s = 'pokebar_0'+str(i+1)
            else:
                s = 'pokebar_'+str(i+1)
            name = s+'.png'
        else:
            nazov = 'PokeGod'
            staty = [0, 0, 0, 0]
            name = 'pokebar_000.png'

        w[0].append("\\stitok{%s}{%d}{%d}{%d}{%d}\n" % (nazov, staty[0], staty[1], staty[2], staty[3]))
        temp.append("\\barcode{%s}\n" % (name))

        if (i+1) % 3 == 0:
            w[1].append(temp[2])
            w[1].append(temp[1])
            w[1].append(temp[0])
            temp = []

with open('pokestitky.txt', 'w') as f:
    for i in range(7):
        for j in range(30):
            k = 30*i + j
            f.write(w[0][k])
        for j in range(30):
            k = 30*i + j
            f.write(w[1][k])
