# 1. Use Structurizr DSL and ADD 3.0 for architecture docs

## Status

Accepted

## Context

We need a single source of truth for architecture and decisions in the repo.

## Decision

We use Structurizr DSL (C4) with !docs and !adrs, and follow ADD 3.0 for design steps.

## Consequences

- Diagrams and docs live in the repo; Structurizr vNext (local/export) for viewing.
- ADRs in MADR format for compatibility with Structurizr importers.
