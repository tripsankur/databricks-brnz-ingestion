# Pipeline Factory evidence — contract_account

- **spec**: `spec-94139bfa` v2
- **source**: `workspace.bronze.aldm_contract_account` (aldm)
- **target**: `workspace.silver.contract_account` (salesforce_comms)
- **approved by**: ankurtripathi.cs@gmail.com
- **build run**: 88c31c14-5d78-43c2-86c3-f585002253be

## Mapping summary

| source | target | transform | confidence |
|---|---|---|---|
| `account_id` | `account_id` | passthrough | 100% |
| `status_cd` | `status_code` | `src.`status_cd`` | 80% |
| `balance_amt` | `balance_amount` | `CAST(src.`balance_amt` AS DECIMAL(20, 2))` | 70% |
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

_no fixes required_

## Artifacts

- `pipelines/contract_account/lakeflow_connect.yml` (`b5c571abb737`)
- `pipelines/contract_account/silver_stitch.sql` (`f1684c97bbf2`)
- `pipelines/contract_account/adapter_view.sql` (`c4332859a5ad`)
- `pipelines/contract_account/expectations.yml` (`7a8d3066bb4b`)
- `pipelines/contract_account/recon_job.py` (`6d002583185a`)
- `pipelines/contract_account/tests/test_pipeline.py` (`63dc1e45404e`)
- `pipelines/contract_account/bundle_resource.yml` (`96925d11fd2a`)

---
_generated_by: pipeline_factory · spec_id: spec-94139bfa · spec_version: 2_
