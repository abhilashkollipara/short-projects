import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

weather_data = pd.read_csv('KPHL.csv', parse_dates=['date'])
print(weather_data.describe())

with plt.style.context('ggplot'):
    for column in weather_data.columns:
        if column in ['date']:
            continue
        plt.figure()
        plt.hist(weather_data[column].values)
        plt.title(column)
        plt.savefig('{}.png'.format(column))

    weather_data_subset = weather_data[weather_data['date'] >= datetime(year=2018, month=, day=1)]
    weather_data_subset = weather_data_subset[weather_data_subset['date'] < datetime(year=2018, month=7, day=1)].copy()
    weather_data_subset['day_order'] = range(len(weather_data_subset))

    day_order = weather_data_subset['day_order']
    record_max_temps = weather_data_subset['record_max_temp'].values
    record_min_temps = weather_data_subset['record_min_temp'].values
    average_max_temps = weather_data_subset['average_max_temp'].values
    average_min_temps = weather_data_subset['average_min_temp'].values
    actual_max_temps = weather_data_subset['actual_max_temp'].values
    actual_min_temps = weather_data_subset['actual_min_temp'].values

    fig, ax1 = plt.subplots(figsize=(15, 7))

    plt.bar(day_order, record_max_temps - record_min_temps, bottom=record_min_temps,
            edgecolor='none', color='#C3BBA4', width=1)

    plt.bar(day_order, average_max_temps - average_min_temps, bottom=average_min_temps,
            edgecolor='none', color='#9A9180', width=1)

    plt.bar(day_order, actual_max_temps - actual_min_temps, bottom=actual_min_temps,
            edgecolor='black', linewidth=0.5, color='#5A3B49', width=1)

    new_max_records = weather_data_subset[weather_data_subset.record_max_temp <= weather_data_subset.actual_max_temp]
    new_min_records = weather_data_subset[weather_data_subset.record_min_temp >= weather_data_subset.actual_min_temp]

    plt.scatter(new_max_records['day_order'].values + 0.5,
                new_max_records['actual_max_temp'].values + 1.25,
                s=15, zorder=10, color='#d62728', alpha=0.75, linewidth=0)

    plt.scatter(new_min_records['day_order'].values + 0.5,
                new_min_records['actual_min_temp'].values - 1.25,
                s=15, zorder=10, color='#1f77b4', alpha=0.75, linewidth=0)

    plt.ylim(-15, 111)
    plt.xlim(-5, 370)

    plt.yticks(range(-10, 111, 10), [r'{}$^\circ$'.format(x)
                                     for x in range(-10, 111, 10)], fontsize=10)
    plt.ylabel(r'Temperature ($^\circ$F)', fontsize=12)

    month_beginning_df = weather_data_subset[weather_data_subset['date'].apply(lambda x: True if x.day == 1 else False)]
    month_beginning_indeces = list(month_beginning_df['day_order'].values)
    month_beginning_names = list(month_beginning_df['date'].apply(lambda x: x.strftime("%B")).values)
    month_beginning_names[0] += '\n\'14'
    month_beginning_names[6] += '\n\'15'

    month_beginning_indeces += [weather_data_subset['day_order'].values[-1]]
    month_beginning_names += ['July']

    plt.xticks(month_beginning_indeces,
               month_beginning_names,
               fontsize=10)

    ax2 = ax1.twiny()
    plt.xticks(month_beginning_indeces,
               month_beginning_names,
               fontsize=10)

    plt.xlim(-5, 370)
    plt.grid(False)

    ax3 = ax1.twinx()
    plt.yticks(range(-10, 111, 10), [r'{}$^\circ$'.format(x)
                                     for x in range(-10, 111, 10)], fontsize=10)
    plt.ylim(-15, 111)
    plt.grid(False)

    plt.title('City weather, Jan 2018 - June 2018\n\n', fontsize=20)

    plt.savefig('city-weather-jan18-june18.png')