# 🛒 Sklep Internetowy (Python & Tkinter)

Prosta aplikacja desktopowa imitująca system zamówień w sklepie internetowym. Projekt pozwala na przeglądanie asortymentu, zarządzanie koszykiem oraz generowanie podsumowania do pliku tekstowego.

---

## 🌟 Funkcje
* **Katalog produktów:** Wykorzystanie słownika (`dict`) do przechowywania bazy produktów i ich cen.
* **Zarządzanie koszykiem:** * Dynamiczne dodawanie produktów.
    * Usuwanie pojedynczych sztuk lub całego asortymentu.
    * Automatyczne przeliczanie sumy zamówienia.
* **System Rabatowy:** Możliwość aktywacji kodu zniżkowego (25%), który przelicza ceny wszystkich produktów w koszyku.
* **Eksport danych:** Zapisywanie listy zakupów do pliku `koszyk.txt` przy użyciu bezpiecznego menedżera kontekstu (`with open`).
* **Interfejs GUI:** Czytelny układ z kolorowymi przyciskami ułatwiającymi nawigację.

## 🛠️ Technologie
* **Język:** Python 3.x
* **Biblioteka:** `tkinter` (zarządzanie oknami, widgety typu Listbox, Text, Entry).

## 📖 Instrukcja obsługi
1. Wybierz produkt z listy na górze okna.
2. Użyj przycisków **Dodaj** lub **Usuń**, aby zarządzać ilością.
3. Jeśli posiadasz kod rabatowy (domyślnie: `5398`), wpisz go w pole i zatwierdź.
4. Kliknij **"zapisz do pliku"**, aby wygenerować rachunek.

## 📝 Uwagi do kodu (Dla dewelopera)
* Kod używa kodowania `utf-8` przy zapisie do pliku, co zapewnia poprawną obsługę polskich znaków (np. "Łóżko").
* Logika rabatu jest jednorazowa – po wpisaniu kodu ceny w słowniku koszyka są aktualizowane na stałe dla obecnej sesji.


---
*Projekt stworzony w celach edukacyjnych, demonstrujący obsługę zdarzeń (Event Handling) w Pythonie.*
