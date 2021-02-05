import random
import threading
import time

thread_accessible = 0

lock = threading.Lock()


def send(id_, address):
    global thread_accessible
    # with lock:
    #     fval = thread_accessible + 1
    #     if address == 'jon@gmail.com':
    #         raise Exception('abc')
    #     time.sleep(.0001)
    #     thread_accessible = fval
    print(f'ND: {id_}: sending {address}....')
    ts = random.randint(1, 5)
    # lock.acquire()
    # print(f'ND: {id_}:ts {ts}')
    # if ts != 3:
    #     lock.release()

    time.sleep(ts)
    print(f'ND: {id_}: done.')


def task(name, address, send_mail=True):
    task_id = str((time.time()))[-4:]
    if send_mail:
        print(f'ND: sending mail to {name}, {address}')
        send(task_id, address)


def do_nothing():
    while 1:
        print('DT: will do nothing and run')
        time.sleep(1)


if __name__ == "__main__":

    address_list = [
        ('test', 'test@gmail.com'),
        ('jhon', 'jon@gmail.com'),
        ('mark', 'mark@gmail.com'),
        ('destin', 'destin@gmail.com'),

    ]

    mail_task = []
    for address in address_list:
        thr = threading.Thread(
            target=task,
            args=address,
            kwargs={'send_mail': True},
            name=address[0]
        )
        # thr.start()
        mail_task.append(thr)

    t = threading.Thread(target=do_nothing, daemon=True)
    t.start()
    #
    print('M : all thread started. watiing for finish')
    # j_val = [m.join() for m in mail_task]
    # print(j_val)
    print('M : all mail send. bye...')

    # time.sleep(1)
    print(f'M : thread_accesible val: {thread_accessible}')

    while 1:
        print('M: runnning')

        time.sleep(10)