### Projektstruktur

```
theEye/
│
├── .gitignore
├── README.md
├── setup.py
├── requirements.txt
├── LICENSE
│
├── docs/
│   └── index.md
│
├── theEye/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_data_processing.py
│   ├── test_model.py
│   ├── test_train.py
│   └── test_evaluate.py
│
└── scripts/
    └── run_app.py
```

### Förklaring av mappstrukturen:

1. **`theEye/`**: Huvudkoden för ditt projekt.
   - **`data_processing.py`**: Kod för att förbereda och hantera din inputdata.
   - **`model.py`**: Definition och implementering av din djupinlärningsmodell.
   - **`train.py`**: Träningslogik för din modell.
   - **`evaluate.py`**: Kod för att utvärdera modellen och göra prediktioner.
   - **`utils.py`**: Hjälpfunktioner som kan användas i flera delar av projektet.

2. **`tests/`**: Enhetstester för varje del av din kodbas.

3. **`scripts/`**: Skript för att köra applikationen eller andra relaterade uppgifter.

### Bibliotek att använda

1. **NumPy** (`numpy`): För matrisoperationer och grundläggande numeriska beräkningar.
2. **TensorFlow** (`tensorflow`) eller **PyTorch** (`torch`): För att bygga och träna djupinlärningsmodeller.
3. **Scikit-learn** (`scikit-learn`): För enklare maskininlärningsalgoritmer, datadelning och utvärdering.
4. **Matplotlib** (`matplotlib`) eller **Seaborn** (`seaborn`): För att visualisera data och modellens resultat.
5. **Pytest** (`pytest`): För enhetstester.

### Djupinlärningsalgoritmer

För ditt specifika problem kan du överväga följande:

1. **Fully Connected Neural Network (FCNN)**: En enkel feedforward neural network som tar in dina 4 inputs (en vektor av 4 element) och klassificerar dem som kub, linje eller inget mönster.

   - **Input Layer**: 4 neuroner (motsvarande 4 pixlar).
   - **Hidden Layer(s)**: 1-2 lager med ett lämpligt antal neuroner.
   - **Output Layer**: 3 neuroner (en för varje klass: kub, rak linje, diagonal linje).

2. **Logistic Regression**: Kan vara en utgångspunkt för att klassificera dina 4 input. Du kan börja med denna enklare algoritm innan du går vidare till neural networks.

3. **SVM (Support Vector Machine)**: Även om det inte är en djupinlärningsalgoritm, kan SVM vara effektiv för enkla klassificeringsuppgifter och ge dig en känsla för hur maskininlärning fungerar innan du dyker djupare in i neural networks.

### Träningsprocess

1. **Dataset**: Du kan skapa ett syntetiskt dataset med alla möjliga kombinationer av ON/OFF för dina 4 pixlar, och manuellt märka dem som kub, linje (rak eller diagonal), eller inget mönster.

2. **Preprocessing**: Normalisera eller skala dina inputdata om det behövs.

3. **Training**: Träna modellen med ditt dataset, använd en lämplig förlustfunktion som `categorical_crossentropy` (för klassificeringsproblem) och en optimerare som `Adam`.

4. **Evaluation**: Använd testdata för att utvärdera modellens prestanda och justera hyperparametrar som inlärningshastighet eller antalet lager i nätverket.

### Tips

- **Iterera gradvis**: Börja med en enklare modell som logistic regression eller en enkel neural network innan du går vidare till mer komplexa modeller.
- **Visualisera resultat**: Använd visualiseringar för att förstå hur modellen presterar och var den kan förbättras.
- **Testa och validera**: Skriv enhetstester för dina funktioner för att säkerställa att din kod fungerar som förväntat.

### Resurser och Lärande
- **TensorFlow eller PyTorch officiell dokumentation**: Bra resurser för att förstå och implementera djupinlärningsalgoritmer.
- **Kurs i maskininlärning**: Grundläggande kurs i maskininlärning hjälpa dig att förstå grunderna.