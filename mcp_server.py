from mcp.server.fastmcp import FastMCP

# Create the MCP server, give it a name
mcp = FastMCP("inventory-tools")

from inventory import get_total_inventory_value

sample_inventory = [
    {"name": "Widget", "price": 9.99, "quantity": 5},
    {"name": "Gadget", "price": 4.50, "quantity": 12},
]

@mcp.tool()
def get_inventory_summary() -> dict:
    total_value = get_total_inventory_value(sample_inventory)
    return {"total_value": total_value}


@mcp.tool()
def get_inventory_items() -> list[dict]:
    """Return the full list of inventory items with name, price, and quantity."""
    return sample_inventory   

if __name__ == "__main__":
    mcp.run()
