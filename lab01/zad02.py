import pandas
import matplotlib.pyplot as plt

miasta = pandas.read_csv('miasta.csv')

new_city = pandas.DataFrame({'Rok': [2010], 'Gdansk': 460, 'Poznan': [555], 'Szczecin': [405]})

miasta = pandas.concat([miasta, new_city], ignore_index=True)

print(miasta)

plt.plot(miasta['Rok'], miasta['Gdansk'], color='red', marker='o', label='Gdansk')
plt.plot(miasta['Rok'], miasta['Poznan'], color='blue', marker='o', label='Poznan')
plt.plot(miasta['Rok'], miasta['Szczecin'], color='green', marker='o', label='Szczecin')
plt.title('Ludność Gdańska w latach 1900-2010')
plt.xlabel('Rok')
plt.ylabel('Liczba ludności')
plt.legend()
plt.show()

stdGdansk = (miasta['Gdansk'] - miasta['Gdansk'].mean()) / miasta['Gdansk'].std()
stdPoznan = (miasta['Poznan'] - miasta['Poznan'].mean()) / miasta['Poznan'].std()
stdSzczecin = (miasta['Szczecin'] - miasta['Szczecin'].mean()) / miasta['Szczecin'].std()

print('Średnia Gdańsk', stdGdansk.mean(), '\nOdchylenie Gdańsk', stdGdansk.std())
print('Średnia Poznan', stdPoznan.mean(), '\nOdchylenie Poznań', stdPoznan.std())
print('Średnia Szczecin', stdSzczecin.mean(), '\nOdchylenie Szczecin', stdSzczecin.std())

normGdansk = (miasta['Gdansk'] - miasta['Gdansk'].min()) / (miasta['Gdansk'].max() - miasta['Gdansk'].min())
normPoznan = (miasta['Poznan'] - miasta['Poznan'].min()) / (miasta['Poznan'].max() - miasta['Poznan'].min())
normSzczecin = (miasta['Szczecin'] - miasta['Szczecin'].min()) / (miasta['Szczecin'].max() - miasta['Szczecin'].min())

print('Wartosc minimalna Gdansk', normGdansk.max(), '\nWartosc maksymalna Gdansk', normGdansk.min())
print('Wartosc minimalna Poznan', normPoznan.max(), '\nWartosc maksymalna Poznan', normPoznan.min())
print('Wartosc minimalna Szczecin', normSzczecin.max(), '\nWartosc maksymalna Szczecin', normSzczecin.min())