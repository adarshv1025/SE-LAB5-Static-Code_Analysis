"""
Inventory System Module
Performs basic stock management with logging and secure file operations.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List

# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global variable for storing inventory data
stock_data: Dict[str, int] = {}


def add_item(item: str, qty: int = 0, logs: List[str] | None = None) -> None:
    """Add quantity of an item to inventory."""
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid item or quantity type: %s, %s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty

    if logs is not None:
        logs.append(f"{datetime.now()}: Added {qty} of {item}")

    logging.info("Added %d of %s", qty, item)


def remove_item(item: str, qty: int) -> None:
    """Remove quantity of an item from inventory."""
    try:
        if item not in stock_data:
            logging.warning("Attempted to remove non-existent item: %s", item)
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed item: %s (out of stock)", item)
        else:
            logging.info("Removed %d of %s", qty, item)

    except (KeyError, TypeError) as e:
        logging.error("Error removing item: %s", e)


def get_qty(item: str) -> int:
    """Return the quantity of the specified item."""
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json") -> None:
    """Load inventory data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stock_data.clear()
            stock_data.update(data)
        logging.info("Loaded data from %s", file)
    except FileNotFoundError:
        logging.warning(
            "File not found: %s. Starting with empty inventory.", file
        )
        stock_data.clear()
    except json.JSONDecodeError:
        logging.error(
            "Invalid JSON format in %s. Starting with empty inventory.", file
        )
        stock_data.clear()


def save_data(file: str = "inventory.json") -> None:
    """Save inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Saved data to %s", file)
    except OSError as e:
        logging.error("Error saving data: %s", e)


def print_data() -> None:
    """Print a report of all inventory items."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5) -> List[str]:
    """Return a list of items below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main() -> None:
    """Main function for testing inventory operations."""
    logs: List[str] = []

    add_item("apple", 10, logs)
    add_item("banana", 2, logs)
    add_item("orange", 1, logs)

    remove_item("apple", 3)
    remove_item("grapes", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    load_data()
    print_data()

    logging.info("Program executed successfully.")
    print("\nActivity Logs:")
    for entry in logs:
        print(entry)


if __name__ == "__main__":
    main()
