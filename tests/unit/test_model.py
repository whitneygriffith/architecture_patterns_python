import domain.model
import pytest


def test_allocating_to_a_batch_reduces_the_available_quantity():
    pytest.fail('todo')

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