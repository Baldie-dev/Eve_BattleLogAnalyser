log = "Sample_Log.txt"
RateOfFire = 4.0
NumOfDrones = 5
totalEnemyDPH = dict()


with open(log) as f:
    lines = [line.rstrip('\n') for line in f]

for i in range(5, len(lines), 1):
    if "(combat)" in lines[i]:
        lines[i] = lines[i].replace("<color=0xffcc0000>","").replace("<b>","").replace("</b>","").replace("<color=0x77ffffff>","").replace("<color=0xffffffff>","").replace("</font>","").replace("<font size=10>","").replace("<color=0xff00ffff>","").replace(" - Smashes","").replace(" - Glances Off","").replace(" - Grazes","").replace(" - Hits","").replace(" - Penetrates","").replace(" completely","")
        time = lines[i].split(' ')[2]
        lines[i] = lines[i][lines[i].index('(combat)')+9:]
        dmg = lines[i].split(' ')[0]
        if " to " in lines[i]:
            enemy = lines[i].split(" - ")[0].split(" to ")[1]
            if not enemy in totalEnemyDPH.keys():
                totalEnemyDPH[enemy] = [0,0,0]
            totalEnemyDPH[enemy][0] += (int)(dmg)
            totalEnemyDPH[enemy][1] += 1
        if "Your " in lines[i]:
            enemy = lines[i].split(" - ")[0].split(" misses ")[1]
            if not enemy in totalEnemyDPH.keys():
                totalEnemyDPH[enemy] = [0,0,0]
            totalEnemyDPH[enemy][1] += 1
            totalEnemyDPH[enemy][2] += 1 
        #if " from " in lines[i]:
            #print(lines[i])
            
totaldps = 0
totals = 0
for enemy in totalEnemyDPH.keys():
    dph = totalEnemyDPH[enemy][0]/totalEnemyDPH[enemy][1]
    totaldps += dph
    totals += 1
    print(f'{enemy:25} {dph:2.1f}/dph  (hits: {totalEnemyDPH[enemy][1]}) (miss: {totalEnemyDPH[enemy][2]})')

print()
totalAverageDamagePerHit = totaldps / totals
dps = totalAverageDamagePerHit * NumOfDrones / RateOfFire
print(f'Total DPS: {dps:2.1f}')