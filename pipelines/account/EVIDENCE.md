# Pipeline Factory evidence — account

- **spec**: `spec-86caa689` v4
- **source**: `workspace.bronze.sfdc_account` (sfdc)
- **target**: `workspace.silver.account` (lakehouse)
- **approved by**: ankurtripathi.cs@gmail.com
- **build run**: 06e0ab4c-5eb9-4038-ac0d-fb5071fa6077

## Mapping summary

| source | target | transform | confidence |
|---|---|---|---|
| `Id` | `id` | `src.`Id`` | 100% |
| `Name` | `name` | `src.`Name`` | 100% |
| `Type` | `type` | `src.`Type`` | 80% |
| `Industry` | `industry` | `src.`Industry`` | 80% |
| `AnnualRevenue` | `annual_revenue` | `src.`AnnualRevenue`` | 100% |
| `CreatedDate` | `created_date` | `src.`CreatedDate`` | 100% |

All mappings at or above 80% confidence.

## Expectations

- `id_not_null`: `id IS NOT NULL` → fail
- `name_not_null`: `name IS NOT NULL` → fail
- `created_date_not_null`: `created_date IS NOT NULL` → fail
- `annual_revenue_non_negative`: `annual_revenue >= 0` → warn

## Reconciliation

- key match: **100.00%**
- row match: **100.00%**
- attribute match: **100.00%**

## Fix-loop timeline

_no fixes required_

## Artifacts

- `pipelines/account/lakeflow_connect.yml` (`496c30ac81f6`)
- `pipelines/account/silver_stitch.sql` (`7d90f7363e25`)
- `pipelines/account/adapter_view.sql` (`3bad12a55ee4`)
- `pipelines/account/expectations.yml` (`b14903c3bdc6`)
- `pipelines/account/recon_job.py` (`b7be4e2a6ea6`)
- `pipelines/account/tests/test_pipeline.py` (`b64a56379a56`)
- `pipelines/account/bundle_resource.yml` (`8f57c6f890d8`)

---
_generated_by: pipeline_factory · spec_id: spec-86caa689 · spec_version: 4_
