# Pipeline Factory evidence — contract_account

- **spec**: `spec-94139bfa` v8
- **source**: `workspace.bronze.aldm_contract_account` (aldm)
- **target**: `workspace.silver.contract_account` (salesforce_comms)
- **approved by**: ankurtripathi.cs@gmail.com
- **build run**: 2fd418e2-9ec5-42fb-9f76-04b03c6dfba7

## Mapping summary

| source | target | transform | confidence |
|---|---|---|---|
| `account_id` | `account_id` | passthrough | 100% |
| `status_cd` | `status_code` | `src.`status_cd`` | 80% |
| `balance_amt` | `balance_amount` | passthrough | 70% |
| `created_dt` | `created_date` | passthrough | 100% |

**1 mapping(s) below 80% confidence** were human-reviewed at approval.

## Expectations

- `account_id_not_null`: `account_id IS NOT NULL` → fail
- `created_date_not_null`: `created_date IS NOT NULL` → fail
- `status_code_enum`: `status_code IN ('A', 'I')` → warn
- `balance_non_negative`: `balance_amount >= 0` → warn

## Reconciliation

- key match: **99.50%**
- row match: **100.00%**
- attribute match: **100.00%**

## Fix-loop timeline

1. The column 'balance_amount' does not exist in the source; it should be 'balance_amt'.

## Artifacts

- `pipelines/contract_account/lakeflow_connect.yml` (`55f7a7e7a6df`)
- `pipelines/contract_account/silver_stitch.sql` (`99e3629030b4`)
- `pipelines/contract_account/adapter_view.sql` (`d2178f3b1d79`)
- `pipelines/contract_account/expectations.yml` (`d629f9aa1cb7`)
- `pipelines/contract_account/recon_job.py` (`ed78b8e200b0`)
- `pipelines/contract_account/tests/test_pipeline.py` (`2a9586aa2a38`)
- `pipelines/contract_account/bundle_resource.yml` (`28b828ee06af`)

---
_generated_by: pipeline_factory · spec_id: spec-94139bfa · spec_version: 8_
