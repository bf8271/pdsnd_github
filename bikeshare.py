# Import packages
import time
import pandas as pd
import numpy as np

# read in csv files
chicago_data = pd.read_csv('chicago.csv')
nyc_data = pd.read_csv('new_york_city.csv')
washington_data = pd.read_csv('washington.csv')

CITY_DATA = { 'chicago': chicago_data,
              'new york city': nyc_data,
              'washington': washington_data }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    city = ''
    month = ''
    day = ''
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    while city not in CITY_DATA.keys():
        print('Please enter your city:')
        print('Cities: chicago, new york city, washington')
        city = input().lower()
        cities = ['chicago', 'new york city', 'washington']
        if city in cities: 
            break
        else:
            print('Please re-enter a valid city.')
            
    while month not in months:
        print('Please enter a month:')
        print('Please enter from the following options: all, january, february, march, april, may, june')
        month = input().lower()
        if month in months: 
            break
        else:
            print('Please re-enter a valid month.')
            
    while day not in days:   
        print('please enter a day of week:')
        print('Please enter from the following options: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday')
        day = input().lower()
        if day in days:
            break
        else:
            print('Please re-enter valid day.')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = CITY_DATA[city]

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['month_name'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    
    most_common_month = df['month'].mode()[0]
    most_common_month_name = df['month_name'].mode()[0]
    most_common_day_of_week = df['day_of_week'].mode()[0]
    most_common_hour = df['hour'].mode()[0]
    
    print('Most common month number to travel: ', most_common_month)
    print('Most common month name to travel: ', most_common_month_name)
    print('Most common day of week to travel: ', most_common_day_of_week)
    print('Most common hour to travel: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    df['Start to End Station'] = df['Start Station'] + ' to ' + df['End Station']
    
    most_popular_start_station = df['Start Station'].mode()[0]
    most_popular_end_station = df['End Station'].mode()[0]
    most_popular_start_end_station = df['Start to End Station'].mode()[0]
    
    print('Most Popular Start Station: ', most_popular_start_station)
    print('Most Popular End Station: ', most_popular_end_station)
    print('Most Popular Start to End Station route: ', most_popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_travel_time = df['Trip Duration'].sum()
    average_travel_time = round(df['Trip Duration'].mean(),2)
    longest_trip_time = df['Trip Duration'].max()
    route_longest_time = df['Start to End Station'][df['Trip Duration'] == df['Trip Duration'].max()].values[0]
    shortest_trip_time = df['Trip Duration'].min()
    route_shortest_time = df['Start to End Station'][df['Trip Duration'] == df['Trip Duration'].min()].values[0]

    print('Total Travel Time: ', total_travel_time)
    print('Average Travel Time: ', average_travel_time)
    print('Longest Trip Time: ', longest_trip_time)
    print('The route for the longest trip was:', route_longest_time)
    print('Shortest Trip Time: ', shortest_trip_time)
    print('The route for the shortest trip was:', route_shortest_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print('\n Value counts for each user type: \n' , df['User Type'].value_counts().to_string())
    
    try:
        print('\n Value counts for each gender: \n' , df['Gender'].value_counts().to_string())
    except:
        print('There is no gender data for your selection')
    
     

    
    try:
        earliest_birth_year = round(df['Birth Year'].min())
        route_oldest_user = df['Start to End Station'][df['Birth Year'] == df['Birth Year'].min()].values[0]
        gender_oldest_user = df['Gender'][df['Birth Year'] == df['Birth Year'].min()].values[0]
        most_recent_birth_year = round(df['Birth Year'].max())
        route_youngest_user = df['Start to End Station'][df['Birth Year'] == df['Birth Year'].max()].values[0]
        gender_youngest_user = df['Gender'][df['Birth Year'] == df['Birth Year'].min()].values[0]
        most_common_birth_year = round(df['Birth Year'].mode()[0])
        user_most_common_birth_year = len(df['Birth Year'][df['Birth Year'] == df['Birth Year'].mode().values[0]])
        
        print('\n Birth Year Statistics: \n')
        print('Earliest birth year: ', earliest_birth_year)
        print('The route for the oldest user:', route_oldest_user)
        print('The gender for the oldest user:', gender_oldest_user)
        print('Most Recent birth year: ', most_recent_birth_year)
        print('The route for the youngest user:', route_youngest_user)
        print('The gender for the youngest user:', gender_youngest_user)
        print('Most common birth year: ', most_common_birth_year)
        print('Number of users born in the most common year: ', user_most_common_birth_year)
    except:
        print('There is no birth year data for you selection')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def display_raw_data(df):
    """Asks the user if they would like to see the raw data. If they respond yes, returns data 5 rows at a time."""
    display = ''
    n = 5
    accepted_responses = ['yes', 'no']

    try:
        while display not in accepted_responses:
            display = input('\nWould you like to see 5 rows of the data? Enter yes or no.\n').lower()
            if display == 'yes':
                print(df.head())
                while display == 'yes':
                    display = input('\n Would you like to see 5 more rows? Enter yes or no. \n').lower()
                    if display == 'yes':
                        n += 5
                        start = n-5
                        print(df.iloc[start:n, :])   
                    elif display == 'no':
                        break
                    else:
                        print('We do not recognize that response. Please enter a vlaid response.')
            elif display == 'no':
                return
            else:
                print('We do not recognize that response. Please enter a valid response.')
    except:
        print('There is no more data to be displayed.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
