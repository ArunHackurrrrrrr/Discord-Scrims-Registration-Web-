from datetime import datetime, timedelta
import time
import threading

def time_check(reg_Time, scrim_id):
    # Ensure `reg_Time` is in datetime.time format
    if isinstance(reg_Time, str):
        time_format = "%H:%M:%S"
        reg_Time = datetime.strptime(reg_Time, time_format).time()

    # Calculate reduced and increased times
    reduced_time_more = (datetime.combine(datetime.today(), reg_Time) - timedelta(seconds=2)).time()
    reduced_time = (datetime.combine(datetime.today(), reg_Time) - timedelta(seconds=1)).time()
    reduced_timemore = (datetime.combine(datetime.today(), reg_Time) - timedelta(seconds=2)).time()
    increased_time = (datetime.combine(datetime.today(), reg_Time) + timedelta(seconds=1)).time()
    increased_timemore = (datetime.combine(datetime.today(), reg_Time) + timedelta(seconds=2)).time()
    increased_time_more = (datetime.combine(datetime.today(), reg_Time) + timedelta(seconds=3)).time()

    # Create threads for each time check
    threads = [
        threading.Thread(target=time_match, args=(reduced_time, scrim_id)),
        threading.Thread(target=time_match, args=(reg_Time, scrim_id)),
        threading.Thread(target=time_match, args=(increased_time, scrim_id)),
        threading.Thread(target=time_match, args=(increased_timemore, scrim_id)),
        threading.Thread(target=time_match, args=(increased_time_more, scrim_id)),
        threading.Thread(target=time_match, args=(reduced_timemore, scrim_id)),
        threading.Thread(target=time_match, args=(reduced_time_more, scrim_id))
        #git push
    ]

    # Start all threads
    for thread in threads:
        thread.start()

def time_match(reg_Time, scrim_id):
    while True:
        # Get current time as a `datetime.time` object without milliseconds
        now = datetime.now()
        current_time = now.replace(microsecond=0).time()

        if current_time == reg_Time:
            print(f"Time matched: {reg_Time} for scrim ID: {scrim_id}")
            from Registration_soft.utils.Registration import registration_pro
            registration_pro(reg_Time,scrim_id)  # Trigger registration
            return  # Exit the thread once registration is triggered

        elif current_time > reg_Time:
            # print(f"Time {reg_Time} has already passed for scrim ID: {scrim_id}.")
            return  # Exit the thread if the time has passed

        time.sleep(0.1)  
