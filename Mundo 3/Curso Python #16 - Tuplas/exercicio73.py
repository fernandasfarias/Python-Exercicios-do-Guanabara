times = ('Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo', 'Cruzeiro', 'Atlético-MG', 'Bragantino','Palmeiras', 'Internacional', 'Fortaleza', 'Grêmio', 'Vasco', 'Criciúma', 'Juventude', 'Corinthians', 'Fluminense', 'Vitória', 'Atlético-GO', 'Cuiabá')
print(f'Os cinco primeiros colocados foram: {times[0:5]}')
print(f'Os últimos 4 colocados foram: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O time do Corinthians se encontra na {times.index('Corinthians') + 1}ª posição.')
