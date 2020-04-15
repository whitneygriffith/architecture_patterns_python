import domain.model
import pytest
from datetime import date
import random 

class  OrderLine:
    def __init__(self, ref: str, sku: str, quantity: int):
        self.ref = ref
        self.sku = sku 
        self.quantity = quantity

class Batch: 
    def __init__(self, ref: str, sku: str, quantity: int, eta: str):
        self.ref = ref
        self.sku = sku
        self.eta = eta
        self.quantity = quantity

    def can_allocate(self, quantity: int) -> bool:
        if quantity < self.quantity:
            return True
        elif quantity ==  self.quantity:
            return True
        return  False

    def allocate(self, order_line: OrderLine) -> None: 
        if self.can_allocate(order_line.quantity):
            self.quantity -= order_line.quantity

def create_batch_order_line(sku: str, batch_qty: int, order_line_qty: int) -> [Batch, OrderLine]:
    batch = Batch(f"batch-{random.random()}", sku, quantity=batch_qty, eta=date.today())
    order_line = OrderLine(f"{random.random()}", sku, quantity=order_line_qty)
    return (batch, order_line)

def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch, order_line = create_batch_order_line("SMALL-TABLE", 20, 2)
    batch.allocate(order_line)
    assert batch.quantity == 18 

def test_can_allocate_if_available_greater_than_required():
    batch, order_line = create_batch_order_line("SMALL-TABLE", 20, 2)
    batch.allocate(order_line)
    assert batch.can_allocate(order_line.quantity) == True
    assert batch.quantity == 18


def test_cannot_allocate_if_available_smaller_than_required():
    batch, order_line = create_batch_order_line("SMALL-TABLE", 2, 20)
    batch.allocate(order_line)
    assert batch.can_allocate(order_line.quantity) == False
    assert batch.quantity == 2

def test_can_allocate_if_available_equal_to_required():
    batch, order_line = create_batch_order_line("SMALL-TABLE", 2, 2)
    batch.allocate(order_line)
    assert batch.quantity == 0

def test_only_allocates_order_lines_to_batches_with_matching_skus():
    batch, order_line = create_batch_order_line("SMALL-TABLE", 20, 2)
    batch2, order_line2 = create_batch_order_line("LARGE-TABLE", 20, 2)
    batch.allocate(order_line2)
    assert batch.can_allocate(order_line2) == False
    assert batch.quantity == 20

def test_prefers_warehouse_batches_to_shipments():
    pytest.fail('todo')

def test_prefers_earlier_batches():
    pytest.fail('todo')

def test_allocation_is_idempotent():
    pytest.fail('todo')

