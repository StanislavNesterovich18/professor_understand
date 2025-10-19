from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_data


if __name__ == "__main__":
    print(get_mask_card_number("2200 1209 9298 4334"))
    print(get_mask_account("7437903493 03 122 332 44342342 34"))


    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(get_data("2024-03-11T02:26:18.671407"))


