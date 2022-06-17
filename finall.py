import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'C:\\Users\\amrel\\.spyder-py3\\chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january','february','march','april','may','june']
days = ['monday','tuesday','wednesday','thursday','friday','satarday','sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    month ,day = None, None
    print('Hello! Let\'s explore some US bikeshare data!')
    while True :
        try:
            city = input("Please enter the name of city you'd like to see its (chicago, newyork, washington) : ").lower()
            if city not in CITY_DATA:
                print("Please make sure that you type the city right!!")
            else:
                break
        except ValueError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("\nThere is no INPUT taken")
    while True :
        try:
            if month != None and day != None:
                break
            choose = input("Would u like to filter a data by month, day, or not at all : ").lower()
            if choose == 'month':
                while True:
                    try:
                        month = input("Enter a month from (january, february, ... , june) of type all :").lower()
                        if month not in months and month != 'all':
                            print("Please type month name right or type all.")
                        else:
                            day = 'all'
                            break
                    except ValueError:
                        print("Invalid input")
                    except KeyboardInterrupt:
                        print("There is no INPUT taken")
            elif choose == 'day':
                while True:
                    try:
                        day = input("choose a day you'd like see its data or type all:").lower()
                        if day not in days and day != 'all':
                            print("Please type day name right or type all.")
                        else:
                            month = 'all'
                            break
                    except ValueError:
                        print("Invalid input")
                    except KeyboardInterrupt:
                        print("There is no INPUT taken")
            elif choose == 'all':
                month, day = 'all', 'all'
                break
            else:
                print('Please enter month, day, or all')
        except ValueError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("There is no INPUT taken")

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common montth
    most_month = df['month'].mode()[0]
    most_month = months[most_month-1]
    print('The most common month is {}'.format(most_month).title())
    # TO DO: display the most common day of week
    most_day = df['day_of_week'].mode()[0]
    print('The most common day is {}'.format(most_day))
    # TO DO: display the most common start hour
    most_hour = df['hour'].mode()[0]
    print('The most common hour is {}'.format(most_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start = df['Start Station'].mode()[0]
    print('The most commonly used Start Station is [{}]'.format(most_start))
    # TO DO: display most commonly used end station
    most_end = df['End Station'].mode()[0]
    print('The most commonly used End Station is [{}]'.format(most_end))
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] +' --> '+ df['End Station'] 
    print('The most commonly used combinations of Start and End stations is [{}]'.format(df['combination'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is [{}] hour'.format(total_time/3600))
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('The avreage travel time is [{}] mintue'.format(avg_time/60))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Users Types are:\n',df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('Gender types are:\n',df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year'in df:
        now = datetime.datetime.now().year
        young =  now - int(df['Birth Year'].max())
        old =  now - int(df['Birth Year'].min())
        most_age = now - df['Birth Year'].mode()[0]
        print('Youngest one is [{}] \nOldest one is [{}] \nThe most common Age is [{}]'.format(young, old, most_age))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return 
def head_5(df):
    x = 0 
    while True:
        try:
            choose = input('Would you like to display 5 rows of The Data Frame. Please Type yes/no?').lower()
            if choose == 'no':
                break
            elif choose == 'yes':
                print(df[x:x+5])
                x +=5
            else:
                print('Please Type yes or no')
        except ValueError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("There is no INPUT taken")

        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        head_5(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
