def input_prices():
    # Удаляем лишние пробелы при вводе товаров и магазинов
    products = [product.strip() for product in input("Введите список товаров через запятую: ").split(',')]
    stores = [store.strip() for store in input("Введите названия магазинов через запятую: ").split(',')]
    
    product_prices = {}

    # Ввод цен для каждого товара в каждом магазине
    for product in products:
        prices = []
        print(f"Введите цены для товара {product} в каждом магазине.")
        for store in stores:
            price = float(input(f"Цена в магазине {store}: "))
            prices.append(price)
        product_prices[product] = prices

    return products, stores, product_prices

def calculate_totals(products, stores, product_prices):
    store_totals = {store: 0 for store in stores}

    # Подсчет общей стоимости товаров в каждом магазине
    for product in products:
        prices = product_prices[product]
        for i, store in enumerate(stores):
            store_totals[store] += prices[i]

    return store_totals

def find_cheapest_store(store_totals):
    # Поиск магазина с наименьшей стоимостью
    cheapest_store = min(store_totals, key=store_totals.get)
    return cheapest_store, store_totals[cheapest_store]

def main():
    products, stores, product_prices = input_prices()
    store_totals = calculate_totals(products, stores, product_prices)

    # Вывод общей стоимости покупок в каждом магазине
    print("\nОбщая стоимость покупок в каждом магазине:")
    for store, total in store_totals.items():
        print(f"{store}: {total:.2f} руб.")

    # Поиск и вывод самого дешевого магазина
    cheapest_store, cheapest_total = find_cheapest_store(store_totals)
    print(f"\nВы можете сэкономить больше всего денег, если купите в магазине {cheapest_store}. Общая стоимость: {cheapest_total:.2f} руб.")

if __name__ == "__main__":
    main()