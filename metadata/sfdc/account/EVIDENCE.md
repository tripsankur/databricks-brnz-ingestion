# Pipeline Factory evidence — account

- **spec**: `spec-2443d331` v2
- **source**: `workspace.bronze.sfdc_account` (sfdc)
- **target**: `workspace.silver.account` (lakehouse)
- **approved by**: ankurtripathi.cs@gmail.com
- **build run**: 0983c54b-bcb7-470e-a38d-d2b4d964a695

## Mapping summary

| source | target | transform | confidence |
|---|---|---|---|
| `Id` | `id` | `src.`Id`` | 100% |
| `Name` | `name` | `src.`Name`` | 100% |
| `Type` | `type` | `src.`Type`` | 70% |
| `Industry` | `industry` | `src.`Industry`` | 70% |
| `AnnualRevenue` | `annual_revenue` | `CAST(src.`AnnualRevenue` AS DOUBLE)` | 90% |
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

- `metadata/sfdc/account/dataflow.yml` (`64448c759026`)
- `resources/sfdc.pipeline.yml` (`4b297c9634db`)

---
_generated_by: pipeline_factory · spec_id: spec-2443d331 · spec_version: 2_
