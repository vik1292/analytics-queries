---
name: yamlheader-specialist
description: Expert at creating and maintaining high-quality YAML header documentation that will be added to the top of each query
---

## Purpose
This document defines the **authoritative spec** for YAML header that must accopany every query added to this repository. It is optimized for use by a GitHub Copilot agent and human contributors. The header's **parameter names, order, and formatting MUST match the sample** provided in the repo.

---

## Required Header Structure (exact keys & order)
Every query files **must** begin with a YAML front marker block delimited by `---` on a line by itself and closed with `---`. The header must contain **exactly** the following parameters, in this order:

1. id: string - machine-friendly identifier (lower_snake_case)
2. name: string - human-friendly title in Title Case, quoted
3. tags: list<string>
4. business_question: string - succinct description of the question
5. source_system: string
6. primary_tables: list<string>
7. output_columns: list<string>
8. filters: list<string>
9. assumptions: list<string>
10. grain: string - e.g., Daily, Monthly
11. last_validated: YYYY-MM-DD
12. owner_team: string
13. owner_contact: string

14. ---

## Canonical Template
```yaml
---
id: <lower_snake_case_id>
name: "<Human-Friendly Title in Title Case>"
tags:
  - <tag_one>
  - <tag_two>
business_question: "<One-or-two-sentence description>"
source_system: "<System name>"
primary_tables:
  - <schema.table_one>
output_columns:
  - <column_one>
filters:
  - <predicate_one>
assumptions:
  - <assumption_one>
grain: "<Daily|Monthly>"
last_validated: "<YYYY-MM-DD>"
owner_team: "<Team name>"
owner_contact: "<Contact handle>"
---
```

---

## Population Rule
- id: lower_snake_case from query intent
- name: Title case, quoted
- tags: 3-8 topical tags
- business_question: 1-3 sentences, quoted
- source_system: main system
- primary_tables: FROM/JOIN tables
- output_columns: SELECT columns
- filters: normalized WHERE predicates
- assumptions: derivations/grouping logic
- grain: aggregation level
- last_validated: ISO date
- owner_team & owner_contact: accountable team and contact

---

## Example
```yaml
---
id: customer_churn_rate_monthly
name: "Customer Churn Rate by Month"
tags:
  - churn
  - retention
business_question: "Measures monthly churn rate by identifying customers who cancelled or became inactive wihtin the month."
soruce_system: "SAS"
primary_tables:
  - dw_sub.f_subscription_status_daily
output_columns:
  - customer_sid
filters:
  - business_date_sid BETWEEN 20250101 AND 20251231
assumptions:
  - yyyymm derived from business_date_sid
grain: "Monthly"
last_validated: "2025-12-04"
owner_team: "Customer Analytics"
owner_contact: "Cust Analytics"
---
```

---

## Validation Checklist
- Header starts and ends with `---`
- Keys exactly as specified, in order
- Lists formatted correctly
- last_validated in YYYY-MM-DD

---

## Copilot Agent Instructions
Generate YAML header strictly following this spec for each new query.
