import time
import datetime
import pandas as pd
import numpy as np



#Please check line 166




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = input('Please enter the city to explore it\'s data: (chicago,new york city or washington)\n')
    while city.lower() not in ('chicago','new york city','washington'):
        city = input('Please enter a valid city name: \n')
    
    month = input('Please enter month name or enter all: \n')
    while month.lower() not in ('all','january','february','march','april','may','june'):
        month = input('Please enter a valid month name: \n')
    
    day = input('Please enter day of week or enter all: \n')
    while day.lower() not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
        day = input('Please enter a valid day name: \n')
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv('{}.csv'.format(city.lower().replace(' ','_')))
    df = df.interpolate(method = 'linear', axis = 0)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day'] = df['Start Time'].dt.weekday_name
          
    if month.lower() == 'all' and day.lower() != 'all':
        df = df[df['day']== day.title()]
        
    elif month.lower() != 'all' and day.lower() == 'all':
        datetime_object = datetime.datetime.strptime(month.title(), "%B")
        month_number = datetime_object.month
        df = df[df['month']== month_number]
        
    elif month.lower() != 'all' and day.lower() != 'all':
        datetime_object = datetime.datetime.strptime(month.title(), "%B")
        month_number = datetime_object.month
        df = df.loc[(df['month'] == month_number) & (df['day'] == day.title())]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    
    print('The most common month is {}'.format(df['Start Time'].dt.month.mode()[0]))

    
    print('The most common day of week is {}'.format(df['Start Time'].dt.weekday_name.mode()[0]))

    
    print('The most common hour is {}'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    print('The most common start station is {}'.format(df['Start Station'].mode()[0]))

   
    print('The most common end station is {}'.format(df['End Station'].mode()[0]))

    
    df['Combination'] = df['Start Station'] + ',' + df['End Station']
    co = df['Combination'].mode()[0]
    print('The most frequent combination of start and end stations are {} and {}'.format(co.split(',')[0],co.split(',')[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    print('Total travel time is {} seconds'.format(df['Trip Duration'].sum()))

    
    print('Mean travel time is {} seconds'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_types = df['User Type'].value_counts()
    print(user_types)

    
    if 'Gender' in df:
        print(df['Gender'].count())

    
    if 'Birth Year' in df:
        print('The earliest year of birth is {}'.format(df['Birth Year'].min()))
        print('The most recent year of birth is {}'.format(df['Birth Year'].max()))
        print('The most common year of birth is {}'.format(df['Birth Year'].mode()[0]))

        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        
        #The following is the implementation of the function to prompt the user to view 5 rows from the data which works fine at all cases
        
        
        x=0
        y=5
        while True:
            if y <= len(df):
                display = input('\nWould you like to view 5 rows of data? Enter yes or no.\n')
                if display.lower() != 'yes':
                    break
                else:
                        print(df.iloc[x:y])
                        x+=5
                        y+=5
            else:
                break

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
