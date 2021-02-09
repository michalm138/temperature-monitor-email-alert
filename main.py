import os
import schedule
import time
from datetime import datetime
import yagmail


def get_cpu_temp():
    os.system("sensors -u > temp_summary")
    receive_data = open('temp_summary', 'r').readlines()
    data = float(receive_data[3].split(': ')[1].rstrip())
    return data


def check():
    report_time = datetime.now()
    temperature = get_cpu_temp()
    log = f' *** [{str(report_time)}]: {temperature}°C\n'
    logs = open('logs', 'a')

    if temperature >= 40:
        try:
            email = yagmail.SMTP(
                'your_email_addressgmail.com', 'your_password')
            email.send(
                to='receiver_email_address@gmail.com',
                subject='Warning! High temperature',
                contents=f"""
                    Hey, the temperature on your home server is too high!

                    Last log:
                    {log}
                """,
                attachments='logs',
            )
        except:
            msg = f""" *** [{report_time}] Alert!: Too hight temperature.\n *** [{report_time}] Unexpected error: Email has not been sent.\n"""
            print(msg.rstrip())
            log += msg
        finally:
            msg = f""" *** [{report_time}] Alert!: Too hight temperature.\n *** [{report_time}] Info: Email has been sent.\n"""
            print(msg.rstrip())
            log += msg
    else:
        msg = f' *** [{report_time}] Info: No errors.\n'
        print(msg.rstrip())
        log += msg
    logs.write(log)


schedule.every(30).minutes.do(check)

while True:
    schedule.run_pending()
    time.sleep(1)
