# 2. Improving gilded rose kata

Date: 2024-06-04

## Status

Proposed

## Context

While solving the gilded rose kata, the current code depends upon the type of 'items'. It can result in the need for revision of code everytime a new item is added in the inventory.

## Decision

The change we are proposing is to implement Structural Pattern as number of items exceeds certain number of items (say 7).

## Consequences

Implementing structural pattern will enhance the readability of the code with separation of concern for each type of items if the logic for quality/sell_in change is maintained in their own separate classes as well as accomodating flexibiltiy and scalability as items increases. 