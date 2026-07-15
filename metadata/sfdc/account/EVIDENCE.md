# Pipeline Factory evidence — account

- **spec**: `spec-9b97d38f` v2
- **source**: `workspace.bronze.sfdc_account` (sfdc)
- **target**: `workspace.silver.account` (lakehouse)
- **approved by**: ankurtripathi.cs@gmail.com
- **build run**: c3c48f21-e8fb-437c-b41d-865c0b799bb2

## Mapping summary

| source | target | transform | confidence |
|---|---|---|---|
| `Id` | `id` | `src.`Id`` | 100% |
| `Name` | `name` | `src.`Name`` | 100% |
| `Type` | `type` | `src.`Type`` | 70% |
| `Industry` | `industry` | `src.`Industry`` | 70% |
| `AnnualRevenue` | `annual_revenue` | `CAST(src.`AnnualRevenue` AS DOUBLE)` | 80% |
| `CreatedDate` | `created_date` | `src.`CreatedDate`` | 100% |

**2 mapping(s) below 80% confidence** were human-reviewed at approval.

## Expectations

- `id_not_null`: `id IS NOT NULL` → fail
- `name_not_null`: `name IS NOT NULL` → fail
- `created_date_not_null`: `created_date IS NOT NULL` → fail
- `annual_revenue_non_negative`: `annual_revenue IS NULL OR annual_revenue >= 0` → warn

## Reconciliation

- key match: **100.00%**
- row match: **100.00%**
- attribute match: **100.00%**

## Fix-loop timeline

_no fixes required_

## Artifacts

- `metadata/sfdc/account/dataflow.yml` (`1d7ac12658bd`)
- `resources/sfdc.pipeline.yml` (`6c2041f66e34`)

---
_generated_by: pipeline_factory · spec_id: spec-9b97d38f · spec_version: 2_
