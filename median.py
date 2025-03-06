import datetime
import random

expenses = {
    "2023-01": {
        "01": {
            "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
            "fuel": [ 210.22 ]
        },
        "09": {
            "food": [ 11.9 ],
            "fuel": [ 190.22 ]
        }
    },
    "2023-03": {
        "07": {
            "food": [ 20, 11.9, 30.20, 11.9 ]
        },
        "04": {
            "food": [ 10.20, 11.50, 2.5 ],
            "fuel": []
        }
    },
    "2023-04": {}
}
#Wyznacz medianę wydatków do pierwszej niedzieli (włącznie) każdego miesiąca
#(np. dla 2023-09 i 2023-10 są to dni 1, 2, 3 wrz i 1 paź).

"""Kroki:
1. Selekcja dni pierwszych w miesiącu do pierwszej niedzieli włącznie.
Możliwe biblioteki: datetime
Możliwe kroki: Podzielenie roku i miesiąca w celu zwrócenia dwóch wartości - (map)
2. Obliczanie mediany wydatków"""

def solution1(expenses):
  wszystkie_miesiace = []

  for years, months in expenses.items():
    year, month = map(int, years.split('-'))

    sunday = None
    for day in range(1,8):
      if datetime.date(year, month, day).weekday() == 6:
        sunday = day
        break
    if sunday is None:
      sunday = 7

    #stworzenie listy zakupów i sformatowanie dnia tak, że można się odnosić do kluczy w dict
    lista_zakupow = []
    for day in range(1, sunday + 1):
      formated_day = f"{day:02d}"

      if formated_day in months:
        for i in months[formated_day]:
          lista_zakupow.extend(months[formated_day][i])
         
    wszystkie_miesiace.extend(lista_zakupow)

    # obliczanie mediany z listy zakupów (kosztów z wszystkich miesięcy):
    n = len(wszystkie_miesiace)
    if n == 0:  
      mediana = None
    else:
      wszystkie_miesiace.sort()
      if n % 2 == 1:  
          mediana = wszystkie_miesiace[n // 2]
      else:
          middle1 = wszystkie_miesiace[n // 2 - 1]
          middle2 = wszystkie_miesiace[n // 2]
          mediana = (middle1 + middle2) / 2 
    
  return mediana

#print(solution1(expenses))

def solution2(expenses):
  """
  Zastanawiałem się między kolejką priorytetową a quickselectem jednak postanowiłem wybrać to drugie rozwiązanie ze względu na brak potrzeby sortowania całej listy.
  Plan polega na podzieleniu listy kosztów na trzy - wartości mniejsze niż pivot (left_side), wartości większe (right_side) i wartości równe.
  Zalety quick select to możliwość znalezienia szukanych elementów bez potrzeby sortowania listy. Średnia złożoność to O(n)
  Wady tego rozwiązania to niefortunny przypadek, który może mieć złożoność O(n^2). Szansa jest jednak mała przy losowym wyborze pivota.
  """
  wszystkie_miesiace = []

  def quickselect(koszty, k):
    #Stworzenie warunku w razie gdyby lista zawierała jeden element 
    if len(koszty) == 1:
      return koszty[0]
    
    #Wybranie pivota i podział listy na trzy 
    pivot = random.choice(koszty)
    left_side = []
    right_side = []
    pivots = []

    for x in koszty:
      if x < pivot:
        left_side.append(x)

      elif x == pivot:
        pivots.append(x)

      else:
        right_side.append(x)

    #Określanie środkowej wartości do mediany (k-ty element)
    #Jeżeli lista elementów po lewej stronie jest większa niż k, to element znajduje się w tej części, ponownie wywołujemy quick select do znalezienia k po lewej stronie. 
    if k < len(left_side):
      return quickselect(left_side, k)
    
    #Przypadek, w którym lista k jest większa niż lista z lewej strony
    elif k < len(left_side) + len(pivots):
      return pivot
    
    #W przypadku gdy k jest po prawej stronie odrzucamy a raczej omijamy liste pivot i lewą stronę, szukamy wartości k dla nowej listy 
    else:
      new_k = k - len(left_side) - len(pivots)
      return quickselect(right_side, new_k)
   #Koniec funkcji quick select

  # Część z poprzedniej funkcji z zastosowaniem quickselect
  for years, months in expenses.items():
    year, month = map(int, years.split('-'))

    sunday = None
    for day in range(1,8):
      if datetime.date(year, month, day).weekday() == 6:
        sunday = day
        break
    if sunday is None:
      sunday = 7
    
    lista_zakupow = []
    for day in range(1, sunday + 1):
      formated_day = f"{day:02d}"

      if formated_day in months:
        for i in months[formated_day]:
          lista_zakupow.extend(months[formated_day][i])

    wszystkie_miesiace.extend(lista_zakupow)

    n = len(wszystkie_miesiace)
    if n == 0:
      mediana = None
    else:
      if n % 2==1:
        mediana = quickselect(wszystkie_miesiace, n //2)
      
      else:
        middle1 = quickselect(wszystkie_miesiace, n // 2 - 1)
        middle2 = quickselect(wszystkie_miesiace, n // 2)
        mediana = (middle1 + middle2)/2
  return mediana
    


print(solution1(expenses))
print(solution2(expenses))