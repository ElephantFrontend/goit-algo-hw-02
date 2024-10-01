# Імпортуємо бібліотеки.
import queue
import random
import time

# Створюємо чергу заявок.
request_queue = queue.Queue()

# Створюємо лічильник для унікальних ідентифікаторів заявок.
request_counter = 0

# Створюємо функцію для генерації заявок.
def generate_request():
    global request_counter
    request_counter += 1
    request = f"Request #{request_counter}"
    request_queue.put(request)
    print(f"Заявка додана: {request}")

# Створюємо функцію для обробки заявок.
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробка {request}")
        time.sleep(2)  # Імітація часу обробки
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Створорюємо main для запуску циклу заявок.
def main():
    try:
        while True:
            # Імітуємо генерацію нових заявок рандомно.
            if random.random() < 0.5:
                generate_request()
            process_request()

            # Створюємо пауза між ітераціями.
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nThe End.")

if __name__ == "__main__":
    main()