import pytest

from inventory import add_item


def test_add_item_to_empty_inventory():
    inventory = []
    updated = add_item(inventory, "Widget", 9.99, 5)

    assert len(updated) == 1
    item = updated[0]
    assert item.get("name") == "Widget"
    assert item.get("price") == 9.99
    assert item.get("quantity") == 5


def test_add_item_with_existing_inventory():
    inventory = [{"name": "Gadget", "price": 4.5, "quantity": 2}]
    updated = add_item(inventory, "Widget", 9.99, 1)

    assert len(updated) == 2
    # new item should be the last one appended
    item = updated[-1]
    assert item.get("name") == "Widget"
    assert item.get("price") == 9.99
    assert item.get("quantity") == 1


def test_add_item_with_zero_quantity():
    inventory = []
    updated = add_item(inventory, "FreeSample", 0.0, 0)

    assert len(updated) == 1
    item = updated[0]
    assert item.get("name") == "FreeSample"
    assert item.get("price") == 0.0
    assert item.get("quantity") == 0


def test_add_item_raises_on_negative_quantity():
    with pytest.raises(ValueError):
        add_item([], "Bad", 1.0, -1)


def test_add_item_raises_on_negative_price():
    with pytest.raises(ValueError):
        add_item([], "Bad", -5.0, 1)
