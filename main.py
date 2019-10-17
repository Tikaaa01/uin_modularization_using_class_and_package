nama = 'Tika Ayu Ariyanti'
program = 'Momentum dan Impuls'

print(f'Program {program} oleh {nama}')

def hitung_massa(momentum, kecepatan):
    massa = momentum / kecepatan
    print(f'Momentum = {momentum}kg.m/s dalam kecepatan = {kecepatan}m/s')
    print(f'Sehingga massa = {massa}kg')
    return momentum / kecepatan

# momentum = 2500
# kecepatan = 10
massa = hitung_massa(2500, 10)
massa = hitung_massa(4000, 20)

def hitung_impuls(gaya, waktu):
    impuls = gaya * waktu
    print(f'Gaya = {gaya}N dalam selang waktu = {waktu / 60}menit')
    print(f'Sehingga impuls = {impuls}Ns')
    return gaya * waktu

# gaya = 200
# waktu = 2 * 60
impuls = hitung_impuls(200, 2 * 60)
impuls = hitung_impuls(150, 4 * 60)

def hitung_momentum(massa, kecepatan):
        momentum = massa * kecepatan
        print(f'Massa = {massa}kg dalam kecepatan = {kecepatan}m/s')
        print(f'Sehingga momentum = {momentum}kg.m/s')
        return massa * kecepatan

# massa = 100
# kecepatan = 10
momentum = hitung_momentum(100, 10)
momentum = hitung_momentum(300, 20)





