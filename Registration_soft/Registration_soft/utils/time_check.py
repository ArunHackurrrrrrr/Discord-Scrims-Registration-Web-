import datetime
import time

def time_check(reg_Time,scrim_id):
    thread = False
    while True:
        # print('in here')
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(0.1)
        # int_reg_time = reg_Time.replace("'"," ")
        if current_time == f'{reg_Time}':
            # print(f'ye hai iske andar ki scrim id {scrim_id}')
            from Registration_soft.views import registration_pro
            registration_pro(scrim_id)
            return 
            
        if current_time> scrim_id:
            # print('returning')
            # print(reg_Time,scrim_id)
            pass
            