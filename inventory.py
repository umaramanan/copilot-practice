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


def remove_item(inventory: list[dict], name: str) -> list[dict]:
    """Remove the first item matching ``name`` from inventory and return the list.

    Args:
        inventory: A list of item dictionaries.
        name: The item name to remove.

    Returns:
        The inventory list after removing the first matching item, if found.
        If no item matches, the inventory is returned unchanged.
    """
    for index, item in enumerate(inventory):
        if item.get("name") == name:
            del inventory[index]
            break

    return inventory


def get_total_inventory_value(inventory: list[dict]) -> float:
    """Calculate the total value of all items in the inventory.

    Args:
        inventory: A list of item dictionaries. Each item may have 'price' and
            'quantity' keys. Missing keys are treated as 0.

    Returns:
        The sum of (price × quantity) for every item in the inventory.
        Returns 0.0 if the inventory list is empty.
    """
    return sum(item.get("price", 0) * item.get("quantity", 0) for item in inventory)
