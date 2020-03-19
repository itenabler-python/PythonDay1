
askforsec = int(input("enter number of seconds you wish to compute:"))
# time_in_hr = 0
if askforsec >= 3600:
    time_in_hr = askforsec // 3600
    time_in_min = (askforsec - (time_in_hr * 3600)) //60
    # time_in_sec = (askforsec -(time_in_hr*3600) - time_in_min*60) % 60
else:
    time_in_hr = 0
    time_in_min = askforsec // 60

time_in_sec = askforsec % 60
print("Time {} in seconds is equal to {} hr {} mins {} sec"
      .format(askforsec,time_in_hr, time_in_min, time_in_sec))