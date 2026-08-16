# Installment limit — status matrix

## Purpose

Verify that the home screen and limit details show consistent information for
available and overdue installment-limit states.

## Environment

- Demo or simulator build only
- Synthetic account data
- Local response mocking enabled
- No connection to production services

## State A — available limit

Fixture: `mocks/installment_limit_available.json`

| Step | Action | Expected result | Check type |
|---|---|---|---|
| 1 | Open the home screen | Installment entry is visible | Region text check |
| 2 | Open limit details | Available amount is shown | Region text check |
| 3 | Inspect the status area | Overdue warning is absent | Full-screen negative check |
| 4 | Inspect the primary action | Action is visually enabled | Visual review |

## State B — overdue

Fixture: `mocks/installment_limit_overdue.json`

| Step | Action | Expected result | Check type |
|---|---|---|---|
| 1 | Return to the home screen | Overdue indicator is visible | Region text check |
| 2 | Open limit details | Overdue warning is shown | Region text check |
| 3 | Inspect available-limit copy | Available-limit copy is absent | Full-screen negative check |
| 4 | Inspect the primary action | Action is visually disabled | Visual review |

## Acceptance rules

- Positive text checks are scoped to the intended screen region.
- Negative checks scan the entire screen so a displaced element is not mistaken
  for an absent one.
- Colour, icons, alignment, and enabled/disabled states require visual review.
- Any mismatch is recorded as observed; the expected result is not rewritten to
  make the run pass.
- The flow stops before any action with financial or identity consequences.

