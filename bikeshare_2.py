import time
import pandas as pd
import numpy as np
import csv
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("Enter the name of the city (Chicago, New York City, Washington): ")
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input("Invalid input. Please enter a valid city (Chicago, New York City, Washington): ")
        
    # get user input for month (all, january, february, ... , june)
    
    month = input("Enter the name of the month (all, January, February, ..., June): ")
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Invalid input. Please enter a valid month (all, January, February, ..., June): ")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input("Enter the name of the day (all, Monday, Tuesday, ..., Sunday): ")
    while day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input("Invalid input. Please enter a valid day (all, Monday, Tuesday, ..., Sunday): ")
        

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
    
    if city=="New York City" or "new york city" or "New york city" or "New York city":
        city="new"+"_"+"york"+"_"+"city"
        
    # Load the data file into a pandas DataFrame
    df = pd.read_csv(city + '.csv',index_col=[0])

    # Convert the 'Start Time' column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from 'Start Time' column
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        df = df[df['Month'] == month.title()]

    # Filter by day if applicable
    if day != 'all':
        df = df[df['Day'] == day.title()]
    return df

def display_raw_data(df):
    """
    This Function Displays the five rows of data egain and egain five more 
    if user decide so until he decide to stop.
    
    """
    
    rows_to_show = 5
    prompt = "\nWould you like to see 5 rows of the raw data? (yes/no): "
    
    # Iterate until user chooses 'no'
    while True:
        show_data = input(prompt)
        
        if show_data.lower() == "yes":
            print(df.head(rows_to_show))
            rows_to_show += 5
        elif show_data.lower() == "no":
            print("No more raw data will be displayed. Please continue with Statistics part")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def more_about_data(df):
    """Displays others usefull informations about dataset."""
    
    prompt = "\nWould you like to Displays Columns name and others usefull informations about dataset.? (yes/no): "
    answer=input(prompt)
    if answer.lower() == "yes":

        print('\nDisplaying others usefull informations about dataset....\n')
        start_time = time.time()


        print("Columns Name:", df.columns)
        print("Some Statistical about data:", df.describe())
        print("Others usefull Informations:", df.info())


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
    elif answer.lower() == "no":
            print("Ok, No problem")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    prompt = "\nWould you like to compute the statistics on the most frequent times of travel.? (yes/no): "
    answer=input(prompt)
    if answer.lower() == "yes":

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # Extract hour from 'start_time' column
        df['hour'] = df['Start Time'].dt.hour

        # Find the most common month
        most_common_month = df['Month'].mode()[0]

        # Find the most common day of week
        most_common_day_of_week = df['Day'].mode()[0]

        # Find the most common start hour
        most_common_start_hour = df['hour'].mode()[0]

        print("Most Common Month:", most_common_month)
        print("Most Common Day of Week:", most_common_day_of_week)
        print("Most Common Start Hour:", most_common_start_hour)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
    elif answer.lower() == "no":
            print("Ok")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    prompt = "\nWould you like to Know a litle about the statistics on the most popular stations and trip.? (yes/no): "
    answer=input(prompt)
    
    if answer.lower() == "yes":
        
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # Display the most commonly used Start Station
        most_common_start_station = df['Start Station'].mode()[0]
        print('Most commonly used Start Station:', most_common_start_station)

        # Display the most commonly used End Station
        most_common_end_station = df['End Station'].mode()[0]
        print('Most commonly used End Station:', most_common_end_station)

        # Calculate the frequency of each combination of Start Station and End Station
        station_combinations = df.groupby(['Start Station', 'End Station']).size().reset_index(name='Frequency')

        # Sort the combinations based on frequency in descending order
        sorted_combinations = station_combinations.sort_values('Frequency', ascending=False)

        # Display the most frequent combination of Start Station and End Station
        most_frequent_combination = sorted_combinations.iloc[0]
        print('Most frequent combination:')
        print('  Start Station:', most_frequent_combination['Start Station'])
        print('  End Station:', most_frequent_combination['End Station'])
        print('  Frequency:', most_frequent_combination['Frequency'])


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
    elif answer.lower() == "no":
            print("Ok no Problem")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    prompt = "\nWould you like to Know the total and average trip duration.? (yes/no): "
    answer=input(prompt)
    
    if answer.lower() == "yes":
        
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # Calculate the total travel time
        total_travel_time = sum(df["Trip Duration"])

        # Calculate the mean travel time
        mean_travel_time = np.mean(df["Trip Duration"])

        # Display the total travel time and mean travel time
        print("Total travel time: ", total_travel_time)
        print("Mean travel time: ", mean_travel_time)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
    elif answer.lower() == "no":
            print("Ok no Problem")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    prompt = "\nWould you like to Know the total and average trip duration.? (yes/no): "
    answer=input(prompt)
    
    if answer.lower() == "yes":


        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_types = df['User Type']
        type_counts = Counter(user_types)
        print(f"User Type Counts: {type_counts}\n")


        # Display counts of gender
        try:
            genders = df['Gender']
            gender_counts = Counter(genders)
            print(f"Gender Counts: {gender_counts}\n")
        except:
            print("This Current Database Does Not have Gender Column")


        # Display earliest, most recent, and most common year of birth
        try:
            birth_years = df['Birth Year']
            earliest_year = min(birth_years)
            most_recent_year = max(birth_years)
            most_common_year = Counter(birth_years).most_common(1)[0][0]
            print(f"Earliest Birth Year: {earliest_year}")
            print(f"Most Recent Birth Year: {most_recent_year}")
            print(f"Most Common Birth Year: {most_common_year}")
        except:
            print("This Current Database Does Not have Birth Year Column")


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
    elif answer.lower() == "no":
            print("Ok no Problem")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

def plot(df):
    """This bar plot will help visualize the distribution of the number of trips between the two user types."""
    
    prompt = "\nWould you like to visualize the distribution of the number of trips between user types..? (yes/no): "
    answer=input(prompt)
    
    if answer.lower() == "yes":

        # Grouping the data by user type and getting the count of trips
        grouped_data = df.groupby('User Type').size()

        # Plotting the bar plot
        grouped_data.plot(kind='bar', rot=0)

        # Adding labels and title
        plt.xlabel('User Type')
        plt.ylabel('Count of Trips')
        plt.title('Bike Dataset - Trip Distribution by User Type')

        # Displaying the plot
        plt.show()
    
    elif answer.lower() == "no":
            print("Ok no Problem")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        
def more_plot(df):
    """
    This plot will help better visualize and comparison of the distribution 
    of daily or monthly trips duration if user choose all month and/or all day.
    
    """
    
    prompt = "\nFinnaly, Would you like to visualize the bar plot of daily and monthly trips duration.? (yes/no): "
    answer=input(prompt)
    
    if answer.lower() == "yes":
        
        sns.barplot(data=df, x='Month', y='Trip Duration')#, hue='film_title'
        plt.title("Bar Plot of Monthly Trip Duration")
        plt.figure(figsize=(10, 6))
        # Displaying the plot
        plt.show()
        
        sns.barplot(data=df, x='Day', y='Trip Duration')#, hue='film_title'
        plt.title("Bar Plot of Daily Trip Duration")
        plt.figure(figsize=(10, 6))
        # Displaying the plot
        plt.show()
        # Displaying the plot
        plt.show()
    
    elif answer.lower() == "no":
            print("Ok no Problem")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        more_about_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        plot(df)
        more_plot(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()