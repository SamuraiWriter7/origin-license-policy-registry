# Trace and Royalty Preservation Rules

## Overview

Trace and Royalty Preservation Rules define how trace metadata, origin references, and royalty pointers must be preserved across reuse, transformation, redistribution, generated outputs, and AI agent consumption.

v0.1 introduced Usage Policy Records.

v0.2 introduced License Template Registry.

v0.3 introduced Asset Policy Binding.

v0.4 introduces explicit preservation rules.

```text
Usage Policy
        ↓
License Template
        ↓
Asset Policy Binding
        ↓
Trace and Royalty Preservation Rules
```

## Purpose

Origin-based structural assets require more than permission metadata.

They also require preservation rules.

A marketplace or AI agent must be able to answer:

* Which trace metadata must survive?
* Which origin reference fields must be preserved?
* Which royalty pointer must remain attached?
* Which actions are prohibited?
* Which redistribution conditions apply?
* Which AI agent actions are allowed?
* Which actions require human review?

## Why Preservation Rules Are Needed

A usage policy can define whether usage is allowed.

A license template can define reusable defaults.

An asset-policy binding can define which policy applies to which asset.

But a downstream system still needs to know what must not be removed.

Trace and Royalty Preservation Rules answer that question.

They define the survival requirements of:

* origin references
* trace receipts
* audit records
* policy bindings
* license template references
* usage policy references
* royalty allocation pointers
* beneficiary references

## v0.4 Scope

The v0.4 layer introduces:

* `schemas/trace-royalty-preservation-rules.schema.json`
* `examples/trace-royalty-preservation-rules.example.yaml`
* validation through `scripts/validate_examples.py`

## Core Relationship

```text
License Template
  = reusable policy pattern

Usage Policy
  = concrete policy record

Asset Policy Binding
  = effective connection between asset and policy

Trace and Royalty Preservation Rules
  = survival rules for origin, trace, and royalty metadata
```

## Preservation Scope

The preservation rule set may apply to:

* asset metadata
* marketplace listings
* derivative creation
* commercial distribution
* redistribution
* AI inference use
* AI training use
* agent consumption
* exported datasets
* generated outputs

## Trace Preservation

Trace preservation defines which metadata must survive.

Examples include:

* origin asset ID
* source asset ID
* trace receipt ID
* origin audit record ID
* asset-policy binding ID
* usage policy ID
* license template ID
* transformation record ID

It may also prohibit actions such as:

* removing trace metadata
* rewriting origin references
* hiding source assets
* detaching audit records
* stripping policy bindings
* obfuscating transformation paths

## Royalty Preservation

Royalty preservation defines which royalty-related fields must survive.

Examples include:

* royalty allocation ID
* royalty pointer
* origin creator ID
* allocation basis
* beneficiary reference
* payment review status

It may also prohibit actions such as:

* removing royalty pointers
* bypassing royalty allocation
* modifying allocation without review
* hiding beneficiary references
* executing payment without human review

## Origin Reference Preservation

Origin reference preservation defines which origin fields must remain attached.

Examples include:

* origin asset ID
* origin creator
* origin repository
* origin license template ID
* origin usage policy ID
* origin trace receipt ID
* origin audit record ID

## Agent Rules

AI agents may inspect and validate preservation rules.

They may also propose derivative or redistribution records.

However, they must not remove preservation metadata or execute rights/payment actions.

```text
read      : allowed
validate  : allowed
propose   : allowed
execute   : human_review_required
```

## Human Review Boundary

Human review is required for sensitive actions such as:

* payment execution
* rights transfer
* trace metadata removal
* royalty pointer removal
* royalty allocation modification
* policy conflict resolution
* bulk redistribution
* bulk AI training

## Design Principle

Trace and royalty metadata should not be treated as decorative metadata.

They are part of the asset’s structural continuity.

If origin information disappears, auditability collapses.

If royalty pointers disappear, value circulation collapses.

v0.4 therefore defines preservation as a first-class rule layer.

```text
Origin must remain visible.
Trace must remain attached.
Royalty must remain reachable.
Human review must guard execution.
```
