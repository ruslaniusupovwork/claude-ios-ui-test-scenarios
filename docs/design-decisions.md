# Design decisions

## Markdown cases instead of app test code

The scenario is readable by QA, product, and engineering stakeholders. Changes to
expected behaviour are reviewable without modifying the mobile application.

## Mocks for hard-to-create states

Rare states should be deterministic. A synthetic fixture can represent overdue,
blocked, pending, or unavailable states without manipulating a real account.

## OCR as an accelerator, not an oracle

OCR is useful for text and presence/absence checks, but it cannot reliably prove
colour, icon meaning, alignment, or interaction state. Those properties must be
covered by accessibility attributes, image comparison, or explicit human review.

## Full-screen negative checks

An element that moved outside a narrow target region is still present. Negative
checks therefore use the whole screen; positive checks stay scoped to reduce false
matches.

## Evidence and safety

Every run should produce a factual expected/actual table. A mismatch is recorded
instead of being rationalized away. Automated flows stop before consequential
financial or identity actions.

