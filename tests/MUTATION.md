Mutation Testing Scenario

Target:
Price validation.

Original condition:

    if price <= 0:

Mutation:

    if price < 0:

Expected result:

The test
test_zero_price_rejected
should fail because a price of 0 would become accepted.

Conclusion:

The existing unit and integration tests are capable of detecting this mutation.
