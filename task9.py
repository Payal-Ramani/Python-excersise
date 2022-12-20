from datetime import datetime,timedelta,time
import portion as p

# Taking input from the users
start_time = input("Enter the start time in the format dd/mm/yy HH:MM:SS in 24 hours format  --->")
end_time = input("Enter the end time in the format dd/mm/yy HH:MM:SS in 24 hours format--->")
start_time_in_format = datetime.strptime(start_time ,'%d/%m/%Y %H:%M:%S')
end_time_in_format = datetime.strptime(end_time,'%d/%m/%Y %H:%M:%S')
start_end_interval = p.closed(start_time_in_format,end_time_in_format)

# Total time before removing any night intervals
difference_duration = end_time_in_format -start_time_in_format

# will append the intervals which considerd night times
night_dates = []
while start_time_in_format  < end_time_in_format + timedelta(days=1) :
    night_dates.append(p.closed(datetime.combine(start_time_in_format,time()),datetime.combine((start_time_in_format),time())+timedelta(hours=6)))
    start_time_in_format += timedelta(days=1)

#it will make an interval which is common in main interval and night interval so that we can get an intervals which gives us final hours which will be disgarded
time_after_difference = []
for interval in night_dates:
    time_after_difference.append(start_end_interval & interval)

# Here this code will give us the total duration which will be removed from total time 
total_time_of_night_hours = timedelta(0)
for i in range(len(time_after_difference)):
    if time_after_difference[i].empty != True:
        tmp =  time_after_difference[i].upper- time_after_difference[i].lower
        total_time_of_night_hours += tmp
final_duration_after_removing_night_hours = difference_duration - total_time_of_night_hours

# This will give the final result after removing the night duration
print(final_duration_after_removing_night_hours)

