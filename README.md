# Fizyka---projekt
## Grzegorz Gajecki - symulacja rzutu ukośnego
![image](https://github.com/user-attachments/assets/a3e69626-2c0c-4658-bedf-99d3a430e633)
Projekt przedstawia symulację rzutu ukośnego w języku programowani Python. Do jego wykonania zostały użyte biblioteki:
- math - biblioteka używana do obliczeń matematycznych
- tkinter - biblioteka graficzna do tworzenia interfejsu użytkownika
- numpy - zewnętrzna biblioteka używana m.in. do obliczeń matematycznych
- matplotlib - zewnętrzna biblioteka używana do generowania wykresów.

W projekcie zostały użyte m.in. następujące wzory lub ich przekształcenia:

**Prędkość pozioma:**
v_x = v_0 * cos(θ)

**Prędkość początkowa pionowa:**
v_y0 = v_0 * sin(θ)

**Maksymalna odległość (zasięg):**
x_max = (v_0² * sin(2θ)) / g

**Równanie toru ruchu:**
y(x) = x * tan(θ) - (g * x²) / (2 * v_0² * cos²(θ))

**Praca równa energii kinetycznej:**
W = E_k = (1/2) * m * v_0²

![image](https://github.com/user-attachments/assets/3ee93fb2-7411-463c-9c31-9dff70575fe4)

Do uruchomienia projektu niezbędny jest interpreter języka Python - można go pobrać [Z tej strony](https://www.python.org/)
Po jego zainstalowaniu należy zainstalować również biblioteki, można to zrobić po pobraniu udostępnionych przeze mnie plików przy użyciu polecenia (na Windows):
```
pip install -r requirements.txt
```
Po zainstalowaniu bibliotek projekt uruchamiamy poleceniem (na windows):
```
python ścieżka\do\pliku\Grzegorz_Gajecki_projekt.py
```
np:
```
python d:\Grzegorz_Gajecki_projekt.py
```
Następnie zgodnie z instrukcjami wpisujemy dane i zatwierdzamy enterem. Jeśli okienko z wykresem nie pojawi samoistnie, to będzie ono zminimalizowane na pasku zadań. Wykres generuje się po naciśnięciu przycisku "Wykres" na górze okienka. Program zakończy swoje działanie po zamknięciu okna.
