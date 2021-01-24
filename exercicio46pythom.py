import time
print('Contagem regressiva de 10s!')
print('iniciando...')
time.sleep(0.3)
for f in range(10, -1, -1):
    time.sleep(1)
    print(f)
    if f == 1:
        time.sleep(1)
        print('VIVA!!')
