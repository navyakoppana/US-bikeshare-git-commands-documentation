import sys
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city,month,day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new york city','washington']
    while True:
        city=input('Which city do you want to explore: ').lower()
        if city not in ['chicago', 'new york city', 'washington']:
              print('{} is an invalid city, you have to choose chicago,new york city,washington to get correct user input'.format(city))
              continue
        else:
              break
       
       
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january','february','march','april','may','june']
    while True:
       month = input('Enter any one of the first 6 months or enter All to select all 6 months you want the data for: ').lower()
       if month not in ['all', 'january', 'february', 'march',
                           'april', 'may', 'june']:
            
            print('{} is not in list'.format(month))
            continue
       else:
              break
      
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=input('Which day do you want the data for: ').lower()

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day_of_week:', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common start hour:', most_common_hour)

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station: ', Start_station)
    # TO DO: display most commonly used end station
    End_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station: ', End_station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combined trip: \n',Combination_Station)
    print('-'*40)
    print('\n')
    print("\nThis took %s seconds." %  round((time.time() - start_time),2))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time=df['Trip Duration'].sum()
    print('The total travel time: ', round(Total_travel_time/(60*60*24),2), "days")

    # TO DO: display mean travel time
    Mean_travel_time=df['Trip Duration'].mean()
    print('The mean travel time: ', round(Mean_travel_time/(60),2), "minutes")
                                               

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('counts of user types: \n',user_types)
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('counts of gender: \n',gender)
    except KeyError:
        print('No data available for gender count')
   
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year = (df['Birth Year']).min()
        print('Earliest Year:', int(Earliest_Year))
    
  
        Most_Recent_Year = (df['Birth Year']).max()
        print('Most Recent Year:', int(Most_Recent_Year))
    
 
        Most_Common_Year = (df['Birth Year']).value_counts().idxmax()
        print('\nMost Common Year:', int(Most_Common_Year))
    except KeyError:
        print('No data of birth year available')

    print("\nThis took %s seconds." %  round((time.time() - start_time),2))
    print('-'*40)
def display_raw_data(df):
    """ To display raw data if asked by the user """
    r = 0
    raw = input("Do you want to view the raw data?Yes or No: ").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[r:r+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Do you want to view more raw data?Yes or No: ").lower() # TO DO: convert the user input to lower case using lower() function
            r += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
    
def validate_userinput():
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart == "":
            print("input cannot be blank. Please re-enter.")
        elif restart.lower() not in ('yes',"no"):
            print('input is invalid, please enter yes or no (lower case)')
        elif restart.lower() == "no":
            sys.exit(0)
        else:
            print("input is valid")
            break
   

def main():
    while True:
        city, month, day = get_filters('city', 'month', 'day')
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        validate_userinput()

if __name__ == "__main__":
	main()
