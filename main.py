import time
from functools import reduce
import plyer


def read():
    """
    read args for notification
    :return: dict with args
    """
    args = dict()
    args['message_title'] = input('Введите имя уведомления: ') or None
    args['message_text'] = input('Введите текст уведомления: ') or None
    args['time_to_sleep'] = reduce(
        lambda prev, x: prev * 60 + x,
        map(int, input('Введите время (часы:минуты:секунды): ').split(":"))
    ) or 0
    args['repeats'] = int(input('Сколько раз повторять: ')) or 1
    return args


def show_message(message_title='Notificator', message_text='The time is over'):
    """
    print win message
    """
    plyer.notification.notify(
        title=message_title,
        message=message_text
    )


def timer_countdown(time_to_sleep):
    """
    Function that sleep until time is over
    """
    time.sleep(time_to_sleep)


def main():
    """
    read args and run timer
    """
    args = read()
    for _ in range(args['repeats']):
        timer_countdown(args['time_to_sleep'])
        show_message(
            args['message_title'],
            args['message_text']
        )


if __name__ == '__main__':
    main()