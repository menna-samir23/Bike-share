import datetime as dt
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
              'New york city': 'new_york_city.csv',
              'Washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('Entre city name chicago , new york city or washington: ').title()

    while city not in CITY_DATA:
        print('Invalid city name try again!')
        city = input('Entre city name (Chicago - New york city - Washington): ').title()

    months = ['January', 'February', 'March','April', 'May', 'June', 'July', 'All']
    month = input('Entre the month name: ').title()
    while month not in months:
        print('Invalid month name, try again!')
        month = input('Entre the month name: ').title()
        
    days = ['Sunday', 'Monday', 'Suesday', 'Wednesday', 'Thursday','Friday','Saturday', 'All']
    day = input('Entre day: ').title()
    while day not in days:
        print('Invalid day, try again!')
        day= input('Entre day: ').title()

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
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['Month'] = df['Start Time'].dt.strftime('%B')
    df['Weekday'] = df['Start Time'].dt.strftime('%A')

    if month != 'All':
        df = df[df['Month'] == month]
        
    if day != 'All':
        df = df[df['Weekday'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = dt.datetime.now()

    common_month = df['Month'].mode()[0]
    common_day = df['Weekday'].mode()[0]
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print(f'Most common month is :{common_month}')
    print(f'Most common day is: {common_day}')
    print(f'Most common hour is : {common_hour}')
    
    end_time = dt.datetime.now()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print(f'This took {(end_time - start_time).seconds} seconds!')
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = dt.datetime.now()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]
    df['Trip'] = df['Start Station'] + ">>>" + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print(f'Most common start station is: {common_start_station}')
    print(f'Most common end station is: {common_end_station}')
    print(f'Most popular trip is: {common_trip}')
    
    end_time = dt.datetime.now()

    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print(f'This took {(end_time - start_time).seconds} seconds!')
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = dt.datetime.now()

    # TO DO: display total travel time
    delta = (df['End Time'] - df['Start Time']).sum()
    
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = (delta.seconds % 3600) % 60

    print(f'Total travels time is {days} day, {hours} hour, {minutes} minutes and {seconds} seconds.')
    
    mean = (df['End Time'] - df['Start Time']).mean()
    mean_days = mean.days
    mean_hours = mean.seconds // 3600
    mean_minutes = (mean.seconds % 3600) // 60
    mean_seconds = (mean.seconds % 3600) % 60
    print(f'Mean travels time is {mean_days} day, {mean_hours} hour, {mean_minutes} minutes and {mean_seconds} seconds.')
    
    end_time = dt.datetime.now()

    print(f'This took {(end_time - start_time).seconds} seconds!')
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = dt.datetime.now()

    # TO DO: Display counts of user types
    count_of_users = df['User Type'].value_counts()
    print(count_of_users)


    # TO DO: Display counts of gender
    if ('Gender' in df.columns) and ('Birth Year' in df.columns):
        gender_count = df['Gender'].value_counts().to_frame()
        print(gender_count)
        common_birth_year = df['Birth Year'].mode()[0]
        print(common_birth_year)


    # TO DO: Display earliest, most recent, and most common year of birth

    
    end_time = dt.datetime.now()

    print(f'This took {(end_time - start_time).seconds} seconds!')
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
