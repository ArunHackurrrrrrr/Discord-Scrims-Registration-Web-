import datetime
import time

def time_check(reg_Time,scrim_id):
    while True:
 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(0.1)
        if current_time == f'{reg_Time}':
            # from Registration_soft.views import registration_pro
            from Registration_soft.utils.Registration import registration_pro
            registration_pro(scrim_id)
            reg = True
            return (scrim_id,reg)
            
        if current_time>f'{reg_Time}':
            print(reg_Time)
            return
        if current_time<f'{reg_Time}':
            print('w0')


        