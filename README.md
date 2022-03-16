# RunnerGame

## Spis treści
* [Główne informacje](#główne-informacje)
* [Instrukcja](#instrukcja)
* [Funkcje](#funkcje)
* [Zrzuty ekranu](#zrzuty-ekranu)
* [Miejsca na udoskonalenia](#miesjca-na-udoskonalenia)


## Główne informacje
- Gra 2D napisana w języku Python w oparciu o moduł pygame.
- Gra polega na zdobyciu jak największej ilości punktów poprzez pokonanie przeszkód przemieszczających się w stronę postaci. Punkty naliczane są dzięki czasu przetrwania.
- Gra zgodnie ze zdobytą ilością punktów przyspiesza, co utrudnia pokonanie przeszkód.


## Instrukcja
Po uruchomieniu programu, aby rozpocząć rozgrywkę, należy nacisnąć dowolony przycisk na klatwiaturze.
Po rozpoczęciu gry, plansza się przesuwa z losowymi przeszkodami typu: kaktusy lub ptaki. Kaktusy można omijać skakając(strzałka w górę), a ptaki skakając(strzałka w górę) lub kucając(strzałka w dół).
Z każdą wielokrotnością stu, gra przyspiesza. 

Po zderzeniu się z przeszkodą rozgrywka się zakańcza. Z opóźnieniem pojawia się ponownie menu, aby zdążyć zobaczyć w jaki sposób się zakończyła rozgrywka.
W menu po zderzeniu się z przeszkodą można zobaczyć ile się zdobyło punktów za poprzednią rozgrywkę oraz naciskając dowolny przycisk, można rozpocząć nową rozgrywkę.


## Funkcje
Funkcje, innowacyjności w grze:
- Skok oraz kucanie,
- Kolizja z przeszkodami,
- Postać sprawia wrażenie anomowanej w biegu oraz kucaniu,
- Ptaki sprawiają wrażenie animowanych,
- Wszystkie grafiki zawarte w grze zostały wykonane oraz zmodyfikowane przeze mnie na potrzebę gry.


## Zrzuty ekranu
- [Menu rozpoczęcia gry](./images/Screenshots/StartMenu.jpg)
- [Gra w toku](./images/Screenshots/Game.jpg)
- [Koniec Gry](./images/Screenshots/GameOver.jpg)
- [Menu po zakończeniu rozgrywki](./images/Screenshots/DeathMenu.jpg)


## To do lista
To do:
- Ranking z najwyższymi rekordami,
- Wybór poziomu trudności, czyli zgodnie z iloma zdobytymi punktami gra przyspiesza,
- Dodanie kolejnych przeszkód,
- Możliwość zniszczenia ograniczoną ilość przeszkód przez biegnącą postać, poprzez np. strzał w przeszkodę.
