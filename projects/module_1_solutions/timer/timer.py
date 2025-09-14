"""
Консольный таймер и будильник с отсчетом времени и уведомлением
"""

import time
import os
import sys
from datetime import datetime, timedelta


def clear_screen():
    """Очищает экран консоли"""
    os.system('cls' if os.name == 'nt' else 'clear')


def play_alarm():
    """Воспроизводит звуковой сигнал (системный beep)"""
    sys.stdout.write('\a')
    sys.stdout.flush()


def format_time(seconds):
    """Форматирует время в формате ЧЧ:ММ:СС"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def countdown_timer():
    """Таймер обратного отсчета"""
    try:
        print("=== ТАЙМЕР ОБРАТНОГО ОТСЧЕТА ===")
        print("Введите время в формате ЧЧ:ММ:СС или только секунды")
        time_input = input("Время: ").strip()

        if ':' in time_input:
            time_parts = time_input.split(':')
            if len(time_parts) == 3:
                hours, minutes, seconds = map(int, time_parts)
            elif len(time_parts) == 2:
                hours = 0
                minutes, seconds = map(int, time_parts)
            else:
                print("Неверный формат времени!")
                return
        else:
            hours = 0
            minutes = 0
            seconds = int(time_input)

        total_seconds = hours * 3600 + minutes * 60 + seconds

        if total_seconds <= 0:
            print("Время должно быть больше 0!")
            return

        print(f"\nТаймер установлен на {format_time(total_seconds)}")
        print("Для отмены нажмите Ctrl+C")
        print("-" * 30)

        while total_seconds > 0:
            clear_screen()
            print("=== ТАЙМЕР ОБРАТНОГО ОТСЧЕТА ===")
            print(f"Осталось: {format_time(total_seconds)}")
            print("Для отмены нажмите Ctrl+C")
            print("-" * 30)

            time.sleep(1)
            total_seconds -= 1

        clear_screen()
        print("=== ТАЙМЕР ОБРАТНОГО ОТСЧЕТА ===")
        print("ВРЕМЯ ВЫШЛО!")
        print("-" * 30)

        for _ in range(5):
            play_alarm()
            time.sleep(0.5)

    except ValueError:
        print("Ошибка: введите корректное числовое значение!")
    except KeyboardInterrupt:
        print("\nТаймер отменен пользователем")


def alarm_clock():
    """Будильник на установленное время"""
    try:
        print("=== БУДИЛЬНИК ===")
        print("Введите время в формате ЧЧ:ММ (например, 14:30)")
        alarm_time = input("Время будильника: ").strip()

        if ':' not in alarm_time:
            print("Неверный формат времени! Используйте ЧЧ:ММ")
            return

        hours, minutes = map(int, alarm_time.split(':'))

        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            print("Неверное время! Часы: 0-23, Минуты: 0-59")
            return

        now = datetime.now()
        alarm_today = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)

        if alarm_today < now:
            alarm_today += timedelta(days=1)

        wait_seconds = (alarm_today - now).total_seconds()

        print(f"\nБудильник установлен на {alarm_today.strftime('%H:%M:%S')}")
        print(f"Ожидание: {int(wait_seconds // 60)} минут")
        print("Для отмены нажмите Ctrl+C")
        print("-" * 30)

        time.sleep(wait_seconds)

        clear_screen()
        print("=== БУДИЛЬНИК ===")
        print("ПРОСЫПАЙСЯ! ПОРА ВСТАВАТЬ!")
        print("-" * 30)

        for _ in range(10):
            play_alarm()
            time.sleep(0.5)

    except ValueError:
        print("Ошибка: введите корректное числовое значение!")
    except KeyboardInterrupt:
        print("\nБудильник отменен пользователем")


def main():
    """Основная функция программы"""
    while True:
        clear_screen()
        print("=== КОНСОЛЬНЫЙ ТАЙМЕР И БУДИЛЬНИК ===")
        print("1. Таймер обратного отсчета")
        print("2. Будильник")
        print("3. Выход")

        choice = input("\nВыберите опцию (1-3): ").strip()

        if choice == '1':
            countdown_timer()
            input("\nНажмите Enter для продолжения...")
        elif choice == '2':
            alarm_clock()
            input("\nНажмите Enter для продолжения...")
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")
            time.sleep(1)


if __name__ == "__main__":
    main()