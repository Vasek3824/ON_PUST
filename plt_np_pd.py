import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def func1():
    data = np.random.rand(10) * 5
    print(data)
    print()
    df = pd.DataFrame({'x': data.tolist()})
    df['y'] = df['x']**0.5
    df['z'] = df['x']+df['y']
    df['Свеча графика'] = np.where(df['z'] > 5, 'высокая', 'низкая' )
    print(df)
    #plt.figure(figsize=(10, 8))
    plt.boxplot([df[df['Свеча графика'] == 'высокая']['z'], df[df['Свеча графика'] == 'низкая']['z']],
    tick_labels=['высокая', 'низкая'])
    plt.ylabel('z')
    plt.title('Какой-то график')
    plt.show()

func1()

