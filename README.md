# TDD + DDD Using Architecture Patterns 

This project attempts to solve the problem presented in [Architecture Patterns with Python](https://learning.oreilly.com/library/view/architecture-patterns-with/9781492052197/).

## Problem Statement 

MADE.com is a furniture retailer that sources furniture from manufacturers all over the world and sell it across Europe  

At a high level, we have separate systems that are responsible for buying stock, selling stock to customers, and shipping goods to customers. A system in the middle needs to coordinate the process by allocating stock to a customer’s orders

![img](./docs/img/img1.png)

**Current System** 

For the purposes of this book, we’re imagining that the business decides to implement an exciting new way of allocating stock. Until now, the business has been presenting stock and lead times based on what is physically available in the warehouse. If and when the warehouse runs out, a product is listed as “out of stock” until the next shipment arrives from the manufacturer.

**Goal** 

Here’s the innovation: if we have a system that can keep track of all our shipments and when they’re due to arrive, we can treat the goods on those ships as real stock and part of our inventory, just with slightly longer lead times. Fewer goods will appear to be out of stock, we’ll sell more, and the business can save money by keeping lower inventory in the domestic warehouse.



## Domain Model

### Product 

* Product is part of the Domain Model 
* Product has the following  attributes: 
    - [ ] sku

### Order

* Order is part of the Domain Model 
* Customers place Orders 
* Order has the following attributes: 
    - [ ] ref: order reference
    - [ ] order_lines: List of OrderLine based on product

### OrderLine 

* OrderLine is part of the Domain Model  
* OrderLine has the following attributes:
    - [ ] sku
    - [ ] quantity 
    - [ ] ref

### Batch 
    
* Batch is part of the Domain Model 
* Batch has  the following  attributes: 
    - [ ] ref: unique identifier
    - [ ] sku
    - [ ] eta 
    - [ ] quantity 

## Actions 

- [ ] Allocate order lines to Batches 
    - [x] Can only allocate if the Batch quantity is more than or equal to the OrderLine's quantity 
    - [ ] Idempotent 
    - [x] Matching SKUs 
    - [x] Decrement Batch available quantity 
    - [ ] We allocate to warehouse stock in preference to shipment batches. 
    - [ ] We allocate to shipment batches in order of which has the earliest ETA.

- [ ] Can de-allocate order lines from  Batches 
    - [ ] Increment Batch available items 

- [ ] Raise Domain Exceptions

## Process:

- [x] Create the stubs for tests based on expected behavior of the entire model. Set the tests to fail.
- [x] Create class for relevant domain objects for the `test_model`
- [ ] Implement the model and the specific behavior  one passing test  at a time


## Notes

Describe any challenges encountered while building the app.

* Should my test for ensuring allocating orderLines to Batches decrements the Batch quantity  be in `test_model` test suite or its own `test_batch` test suite? [Related Commit](https://github.com/whitneygriffith/architecture_patterns_python/commit/9a2584383455779fe62a2f0cfc43c319cec01523)
* In my `test_can_allocate_if_available_greater_than_required` am I effectively unit testing if I assert against the `batch.can_allocate()` or do I need to assert that `batch.allocate` actuall allocates or do I need to do both? [Related Commit](https://github.com/whitneygriffith/architecture_patterns_python/commit/9a2584383455779fe62a2f0cfc43c319cec01523)
