from datetime import date, datetime


def date_para_str(data: date) -> str:
    return data.strftime("%d/%m/%Y")


def str_para_date(data: str) -> date:
    return datetime.strptime(data, "%d/%m/%Y")


# Teste


def teste():

    # date_para_str
    print("date_para_str")
    data: date = datetime.now()
    print(f"data = {data}")
    data_str = date_para_str(data)
    print(f"{data_str=}")
    print()

    # str_para_data
    print("str_para_data")
    data_date = str_para_date(data_str)
    print(data_str)
    print(f"str = {data_date}")
    print()


if __name__ == "__main__":
    teste()
