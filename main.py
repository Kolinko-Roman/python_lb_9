def calculate_cosmic_distance(speed_of_light_fraction, time_years):
    return speed_of_light_fraction * time_years

def calculate_simplified_gravity(mass1, mass2, cosmic_factor=1.0):
    return mass1 * mass2 * cosmic_factor

def calculate_time_dilation_approximation(speed_of_light_fraction, time_seconds):
    try:
        return time_seconds / (1 - speed_of_light_fraction)
    except ZeroDivisionError:
        return float('inf')

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Будь ласка, введіть коректне числове значення.")

def main():
    print("Вітаємо у програмі космічних обчислень!")

    while True:
        print("\nОберіть розрахунок:")
        print("1 - Космічна відстань")
        print("2 - Спрощене гравітаційне притягання")
        print("3 - Наближення сповільнення часу")
        choice = input("Ваш вибір (1/2/3): ")

        if choice == "1":
            speed = get_float_input("Введіть частку швидкості світла (від 0 до 1): ")
            time = get_float_input("Введіть час у роках: ")
            result = calculate_cosmic_distance(speed, time)
            print(f"Космічна відстань: {result:.3f} світлових років.")

        elif choice == "2":
            mass1 = get_float_input("Введіть масу першого об'єкта: ")
            mass2 = get_float_input("Введіть масу другого об'єкта: ")
            factor_input = input("Введіть космічний фактор (Enter для значення 1.0): ")
            factor = float(factor_input) if factor_input else 1.0
            result = calculate_simplified_gravity(mass1, mass2, factor)
            print(f"Гравітаційне притягання: {result:.3f}")

        elif choice == "3":
            speed = get_float_input("Введіть частку швидкості світла (від 0 до 1): ")
            time = get_float_input("Введіть час у секундах: ")
            result = calculate_time_dilation_approximation(speed, time)
            print(f"Сповільнення часу: {result:.3f} секунд.")

        else:
            print("Невірний вибір. Спробуйте ще раз.")
            continue

        repeat = input("Бажаєте виконати ще один розрахунок? (так/ні): ").strip().lower()
        if repeat != "так":
            print("Дякуємо за використання програми.")
            break

if __name__ == "__main__":
    main()
