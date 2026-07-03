from typing import List, Dict


def add_item(inventory: List[Dict], name: str, price: float, quantity: int) -> List[Dict]:
    """Add a new item to the inventory list and return the updated list.

    Args:
        inventory: A list of item dictionaries. Each item is expected to have keys
            like 'name', 'price', and 'quantity'. The list may be mutated in place.
        name: The name of the item to add.
        price: The price of the item.
        quantity: The quantity of the item (must be >= 0).

    Returns:
        The updated inventory list with the new item appended.

    Raises:
        ValueError: If quantity is negative or price is negative.
    """
    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    if price < 0:
        raise ValueError(f"price must be non-negative, got {price}")

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
    }

    inventory.append(item)
    return inventory
