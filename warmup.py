def sort_products_by_price(products: list[dict]) -> list[dict]:
    """
    Sorts a list of products by their price in descending order.

    Args:
        products (list[dict]): A list of dictionaries, where each dictionary represents a product with a 'price' key.

    Returns:
        list[dict]: A new list of products sorted by price in descending order.
    """
    return sorted(products, key=lambda x: x.get('price', 0), reverse=True)

print(sort_products_by_price([{"name": "Pen", "price": 2}, {"name": "Mug"}]))

from typing import Any, Dict, List

def filter_active_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Return only the user dictionaries where the 'active' key is True.

    Args:
        users: A list of dictionaries representing users.

    Returns:
        A list containing only the user dicts with user.get('active', False) is True.
    """
    return [user for user in users if user.get('active', False) is True]


if __name__ == "__main__":
    users = [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False},
        {"id": 3, "name": "Carol"}  # no 'active' key -> treated as False
    ]
    print(filter_active_users(users))