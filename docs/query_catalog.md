# Analytics Query Catalog

This catalog provides an index of all available queries organized by category and source system.

## Table of Contents

- [IVR Queries](#ivr-queries)
- [Agent Queries](#agent-queries)
- [Collections Queries](#collections-queries)

---

## IVR Queries

### SQL Queries

#### [IVR Containment Rate Analysis](../sql/ivr/ivr_containment_rate.sql)

**Business Question:** What percentage of calls are resolved within IVR without agent transfer?

**Details:**
- **ID:** `ivr_containment_rate`
- **Tags:** `ivr`, `ivr_metrics`, `contact_center`, `containment`, `self_service`
- **Source System:** Snowflake
- **Primary Tables:** `fact_ivr_calls`
- **Grain:** daily
- **Owner Team:** Auto Ops Analytics - IVR
- **Last Validated:** 2025-11-22

#### [IVR Dropped Calls Analysis](../sql/ivr/ivr_dropped_calls.sql)

**Business Question:** What is the dropped-call rate in IVR before reaching an agent?

**Details:**
- **ID:** `ivr_dropped_calls`
- **Tags:** `ivr`, `ivr_metrics`, `contact_center`, `dropped_calls`, `call_volume`
- **Source System:** Snowflake
- **Primary Tables:** `fact_ivr_calls`
- **Grain:** daily
- **Owner Team:** Auto Ops Analytics - IVR
- **Last Validated:** 2025-11-22

#### [IVR Transfer Rate Analysis](../sql/ivr/ivr_transfer_rate.sql)

**Business Question:** What is the rate of calls transferred from IVR to agents?

**Details:**
- **ID:** `ivr_transfer_rate`
- **Tags:** `ivr`, `ivr_metrics`, `contact_center`, `transfers`, `agent_routing`
- **Source System:** Snowflake
- **Primary Tables:** `fact_ivr_calls`, `fact_agent_calls`
- **Grain:** daily
- **Owner Team:** Auto Ops Analytics - IVR
- **Last Validated:** 2025-11-22


### SAS Queries

#### [IVR Containment Rate Analysis](../sas/ivr/ivr_containment_rate.sas)

**Business Question:** What percentage of calls are resolved within IVR without agent transfer?

**Details:**
- **ID:** `ivr_containment_rate_sas`
- **Tags:** `ivr`, `ivr_metrics`, `contact_center`, `containment`, `self_service`
- **Source System:** SAS
- **Primary Tables:** `fact_ivr_calls`
- **Grain:** daily
- **Owner Team:** Auto Ops Analytics - IVR
- **Last Validated:** 2025-11-22

#### [IVR Dropped Calls Analysis](../sas/ivr/ivr_dropped_calls.sas)

**Business Question:** What is the dropped-call rate in IVR before reaching an agent?

**Details:**
- **ID:** `ivr_dropped_calls_sas`
- **Tags:** `ivr`, `ivr_metrics`, `contact_center`, `dropped_calls`, `call_volume`
- **Source System:** SAS
- **Primary Tables:** `fact_ivr_calls`
- **Grain:** daily
- **Owner Team:** Auto Ops Analytics - IVR
- **Last Validated:** 2025-11-22

#### [IVR Transfer Rate Analysis](../sas/ivr/ivr_transfer_rate.sas)

**Business Question:** What is the rate of calls transferred from IVR to agents?

**Details:**
- **ID:** `ivr_transfer_rate_sas`
- **Tags:** `ivr`, `ivr_metrics`, `contact_center`, `transfers`, `agent_routing`
- **Source System:** SAS
- **Primary Tables:** `fact_ivr_calls`, `fact_agent_calls`
- **Grain:** daily
- **Owner Team:** Auto Ops Analytics - IVR
- **Last Validated:** 2025-11-22


## Agent Queries

### SQL Queries

#### [Agent Average Handle Time (AHT)](../sql/agent/agent_aht.sql)

**Business Question:** What is the average handle time per agent?

**Details:**
- **ID:** `agent_aht`
- **Tags:** `agent`, `agent_metrics`, `contact_center`, `efficiency`, `aht`
- **Source System:** Snowflake
- **Primary Tables:** `fact_agent_calls`, `dim_agent`
- **Grain:** daily by agent
- **Owner Team:** Auto Ops Analytics - Agent
- **Last Validated:** 2025-11-22

#### [Agent Productivity Metrics](../sql/agent/agent_productivity.sql)

**Business Question:** What is the overall productivity and utilization of agents?

**Details:**
- **ID:** `agent_productivity`
- **Tags:** `agent`, `agent_metrics`, `contact_center`, `productivity`, `utilization`, `performance`
- **Source System:** Snowflake
- **Primary Tables:** `fact_agent_calls`, `fact_agent_state`, `dim_agent`
- **Grain:** daily by agent
- **Owner Team:** Auto Ops Analytics - Agent
- **Last Validated:** 2025-11-22


### SAS Queries

#### [Agent Average Handle Time (AHT)](../sas/agent/agent_aht.sas)

**Business Question:** What is the average handle time per agent?

**Details:**
- **ID:** `agent_aht_sas`
- **Tags:** `agent`, `agent_metrics`, `contact_center`, `efficiency`, `aht`
- **Source System:** SAS
- **Primary Tables:** `fact_agent_calls`, `dim_agent`
- **Grain:** daily by agent
- **Owner Team:** Auto Ops Analytics - Agent
- **Last Validated:** 2025-11-22

#### [Agent Productivity Metrics](../sas/agent/agent_productivity.sas)

**Business Question:** What is the overall productivity and utilization of agents?

**Details:**
- **ID:** `agent_productivity_sas`
- **Tags:** `agent`, `agent_metrics`, `contact_center`, `productivity`, `utilization`, `performance`
- **Source System:** SAS
- **Primary Tables:** `fact_agent_calls`, `fact_agent_state`, `dim_agent`
- **Grain:** daily by agent
- **Owner Team:** Analytics - Agent
- **Last Validated:** 2025-11-22


## Collections Queries

### SQL Queries

#### [Delinquency Roll Rates](../sql/collections/delinquency_roll_rates.sql)

**Business Question:** How are accounts moving across delinquency buckets over time?

**Details:**
- **ID:** `delinquency_roll_rates`
- **Tags:** `collections`, `delinquency`, `risk`, `credit`, `roll_rates`
- **Source System:** Snowflake
- **Primary Tables:** `fact_account_delinquency`, `dim_account`
- **Grain:** monthly by delinquency_bucket
- **Owner Team:** Ops Analytics
- **Last Validated:** 2025-11-22

#### [Repossession Recovery Rates](../sql/collections/repo_recovery_rates.sql)

**Business Question:** What are the recovery rates on repossessed assets?

**Details:**
- **ID:** `repo_recovery_rates`
- **Tags:** `collections`, `repossession`, `recovery`, `asset_recovery`, `risk`
- **Source System:** Snowflake
- **Primary Tables:** `fact_repossessions`, `fact_asset_sales`, `dim_account`
- **Grain:** monthly by asset_type
- **Owner Team:** Analytics
- **Last Validated:** 2025-11-22


### SAS Queries

#### [Delinquency Roll Rates](../sas/collections/delinquency_roll_rates.sas)

**Business Question:** How are accounts moving across delinquency buckets over time?

**Details:**
- **ID:** `delinquency_roll_rates_sas`
- **Tags:** `collections`, `delinquency`, `risk`, `credit`, `roll_rates`
- **Source System:** SAS
- **Primary Tables:** `fact_account_delinquency`, `dim_account`
- **Grain:** monthly by delinquency_bucket
- **Owner Team:** Ops Analytics
- **Last Validated:** 2025-11-22

#### [Repossession Recovery Rates](../sas/collections/repo_recovery_rates.sas)

**Business Question:** What are the recovery rates on repossessed assets?

**Details:**
- **ID:** `repo_recovery_rates_sas`
- **Tags:** `collections`, `repossession`, `recovery`, `asset_recovery`, `risk`
- **Source System:** SAS
- **Primary Tables:** `fact_repossessions`, `fact_asset_sales`, `dim_account`
- **Grain:** monthly by asset_type
- **Owner Team:** Analytics
- **Last Validated:** 2025-11-22


---

*Last updated: 2025-12-03 05:50:15*
