import domain.model
import pytest
from datetime import date

class  OrderLine:
    def __init__(self, sku: str, quantity: int):
        self.sku = sku 
        self.quantity = quantity

class Batch: 
    def __init__(self, ref: str, sku: str, quantity: int, eta: str):
        self.ref = ref
        self.sku = sku
        self.eta = eta
        self.quantity = quantity
        

def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", quantity=20, eta=date.today())
    order_line = OrderLine("SMALL-TABLE", quantity=2)
    batch.allocate(order_line)
    assert batch.quantity == 18 

def test_can_allocate_if_available_greater_than_required():
    pytest.fail('todo')

def test_cannot_allocate_if_available_smaller_than_required():
    pytest.fail('todo')

def test_can_allocate_if_available_equal_to_required():
    pytest.fail('todo')

def test_allocation_is_idempotent():
    pytest.fail('todo')


def test_only_allocates_order_lines_to_batches_with_matching_skus():
    pytest.fail('todo')

def test_prefers_warehouse_batches_to_shipments():
    pytest.fail('todo')

def test_prefers_earlier_batches():
    pytest.fail('todo')