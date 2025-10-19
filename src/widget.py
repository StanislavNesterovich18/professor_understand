from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_namber):
    if card_namber[-20:].isdigit():
        return f"Счет {get_mask_account(card_namber[-20:])}"

    #if "Cчет" in card_namber:
       #return f"Счет {get_mask_account(card_namber[-20:])}"
    else:
        return f"{card_namber[:-16]} {get_mask_card_number(card_namber[-16:])}"




if __name__ == '__main__':
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))