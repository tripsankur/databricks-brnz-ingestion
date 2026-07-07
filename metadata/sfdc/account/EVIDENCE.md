# Pipeline Factory evidence — account

- **spec**: `spec-86caa689` v15
- **source**: `workspace.bronze.sfdc_account` (sfdc)
- **target**: `workspace.silver.account` (lakehouse)
- **approved by**: ankurtripathi.cs@gmail.com
- **build run**: acdbcd29-853d-4cee-b510-ff83981d1507

## Mapping summary

| source | target | transform | confidence |
|---|---|---|---|
| `Id` | `id` | `src.`Id`` | 100% |
| `Name` | `name` | `src.`Name`` | 100% |
| `Type` | `type` | `src.`Type`` | 80% |
| `Industry` | `industry` | `src.`Industry`` | 80% |
| `AnnualRevenue` | `annual_revenue` | `CAST(src.`AnnualRevenue` AS DOUBLE)` | 100% |
| `CreatedDate` | `created_date` | `src.`CreatedDate`` | 100% |

All mappings at or above 80% confidence.

## Expectations

- `id_not_null`: `id IS NOT NULL` → fail
- `name_not_null`: `name IS NOT NULL` → fail
- `created_date_not_null`: `created_date IS NOT NULL` → fail
- `annual_revenue_non_negative`: `annual_revenue IS NULL OR annual_revenue >= 0` → fail

## Reconciliation

- key match: **100.00%**
- row match: **100.00%**
- attribute match: **100.00%**

## Fix-loop timeline

_no fixes required_

## Artifacts

- `metadata/sfdc/account/dataflow.yml` (`b6f1335b9e8a`)
- `resources/sfdc.pipeline.yml` (`0359139f1065`)

---
_generated_by: pipeline_factory · spec_id: spec-86caa689 · spec_version: 15_
