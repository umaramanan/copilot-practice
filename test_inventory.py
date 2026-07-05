import pytest

from inventory import add_item, get_total_inventory_value, remove_item


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


def test_remove_item_removes_first_matching_item():
    inventory = [
        {"name": "Widget", "price": 1.0, "quantity": 1},
        {"name": "Gadget", "price": 2.0, "quantity": 1},
        {"name": "Widget", "price": 3.0, "quantity": 1},
    ]

    updated = remove_item(inventory, "Widget")

    assert len(updated) == 2
    assert updated[0].get("name") == "Gadget"
    assert updated[1].get("name") == "Widget"
    assert updated[1].get("price") == 3.0


def test_remove_item_no_match_leaves_inventory_unchanged():
    inventory = [{"name": "Gadget", "price": 4.5, "quantity": 2}]

    updated = remove_item(inventory, "Missing")

    assert updated == [{"name": "Gadget", "price": 4.5, "quantity": 2}]


def test_get_total_inventory_value_multiple_items():
    inventory = [
        {"name": "Widget", "price": 9.99, "quantity": 3},
        {"name": "Gadget", "price": 4.5, "quantity": 2},
    ]

    total = get_total_inventory_value(inventory)

    assert total == pytest.approx(9.99 * 3 + 4.5 * 2)


def test_get_total_inventory_value_empty_inventory():
    total = get_total_inventory_value([])

    assert total == 0.0


def test_get_total_inventory_value_missing_price():
    inventory = [{"name": "Widget", "quantity": 5}]

    total = get_total_inventory_value(inventory)

    assert total == 0.0


def test_get_total_inventory_value_missing_quantity():
    inventory = [{"name": "Widget", "price": 9.99}]

    total = get_total_inventory_value(inventory)

    assert total == 0.0

