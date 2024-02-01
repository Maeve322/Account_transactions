from scripts.insert import load_json, get_data, get_from, five_transactions, date_correct, sort_data, get_to, get_amount

def main():
    data = load_json()
    ex_items = get_data(data)
    sort_items = sort_data(ex_items)
    items = five_transactions(sort_items)
    for item in items:
        print(date_correct(item['date']), item["description"])
        print(get_from(item), get_to(item))
        print(get_amount(item))
        print()

if __name__ == '__main__':
	main()