# Pipeline Factory evidence — account

- **spec**: `spec-ae820f4e` v6
- **source**: `workspace.bronze.sfdc_account` (sfdc)
- **target**: `workspace.silver.account` (lakehouse)
- **approved by**: ankurtripathi.cs@gmail.com
- **build run**: 3e04564a-e537-474d-9759-35ef3ff84694

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

- `metadata/sfdc/account/dataflow.yml` (`18ee9c1da08d`)
- `resources/sfdc.pipeline.yml` (`2a3c4a7ea346`)

---
_generated_by: pipeline_factory · spec_id: spec-ae820f4e · spec_version: 6_
