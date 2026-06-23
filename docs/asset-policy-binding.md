# Asset Policy Binding

## Overview

Asset Policy Binding defines how a specific origin-based structural asset is connected to a reusable license template and a concrete usage policy.

This layer turns policy records into effective asset-level rules.

## Purpose

v0.1 introduced the Usage Policy Record.

v0.2 introduced the License Template Registry.

v0.3 connects them to actual assets, listings, derivatives, and agent-readable records.

```text
License Template
        ↓
Usage Policy
        ↓
Asset Policy Binding
        ↓
Origin Asset / Derivative Asset / Marketplace Listing
Why Binding Is Needed

A license template is reusable.

A usage policy is concrete.

But a marketplace, registry, or AI agent still needs to know which policy actually applies to which asset.

Asset Policy Binding answers that question.

It defines:

which asset is bound
which license template is used
which usage policy is attached
which fields are inherited
which permissions are effective
which trace and royalty links must be preserved
which conflicts require human review
v0.3 Scope

The v0.3 Asset Policy Binding introduces:

schemas/asset-policy-binding.schema.json
examples/asset-policy-binding.example.yaml
validation through scripts/validate_examples.py
Core Relationship
License Template
  = reusable policy pattern

Usage Policy
  = concrete policy record

Asset Policy Binding
  = effective connection between asset and policy
Conflict Resolution

A binding may define how conflicts are resolved between a reusable template and a concrete usage policy.

Supported resolution modes include:

usage_policy_overrides_template
template_overrides_usage_policy
most_restrictive_rule_wins
human_review_required
Effective Permissions

The binding record exposes the effective permissions that should be applied to the asset.

These include:

commercial use
derivative use
AI training
AI inference
Trace and Royalty Links

Asset Policy Binding also preserves links to:

origin asset ID
license template ID
usage policy ID
trace receipt ID
royalty allocation ID
origin audit record ID

This makes the binding record useful for marketplaces, audit systems, royalty systems, and AI agents.

Human Review Boundary

AI agents may read, evaluate, and propose actions based on the binding.

However, execution-level actions should remain under human review.

read      : allowed
evaluate  : allowed
propose   : allowed
execute   : human_review_required

Examples requiring human review include:

payment execution
rights transfer
metadata removal
royalty allocation modification
commercial sublicensing
bulk AI training
policy conflict resolution
Design Principle

Asset Policy Binding is not only a reference link.

It is the effective policy surface of an asset.

It tells humans, systems, and AI agents:

This asset uses this template.
This asset has this policy.
These permissions are effective.
These trace and royalty links must survive.
These actions require human review.
