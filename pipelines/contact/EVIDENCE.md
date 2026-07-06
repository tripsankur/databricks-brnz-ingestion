# Pipeline Factory evidence — contact

- **spec**: `spec-7ec8660b` v3
- **source**: `workspace.bronze.sfdc_contact` (sfdc)
- **target**: `workspace.silver.contact` (lakehouse)
- **approved by**: ankurtripathi.cs@gmail.com
- **build run**: 08ec685d-83aa-4777-953f-820a12cec057

## Mapping summary

| source | target | transform | confidence |
|---|---|---|---|
| `Id` | `id` | passthrough | 100% |
| `AccountId` | `account_id` | passthrough | 100% |
| `FirstName` | `first_name` | passthrough | 100% |
| `LastName` | `last_name` | passthrough | 100% |
| `Email` | `email` | `lower(src.`Email`)` | 90% |
| `CreatedDate` | `created_date` | `to_timestamp(src.`CreatedDate`)` | 100% |

All mappings at or above 80% confidence.

## Expectations

- `id_not_null`: `id IS NOT NULL` → fail
- `last_name_not_null`: `last_name IS NOT NULL` → fail
- `created_date_not_null`: `created_date IS NOT NULL` → fail
- `email_valid`: `email LIKE '%@%.%'` → warn

## Reconciliation

- key match: **100.00%**
- row match: **100.00%**
- attribute match: **100.00%**

## Fix-loop timeline

1. The 'CreatedDate' column is being cast to DOUBLE instead of TIMESTAMP or DATETIME, causing a CAST_INVALID_INPUT error.
2. The 'CreatedDate' column is being cast to DOUBLE instead of TIMESTAMP or DATETIME, causing a CAST_INVALID_INPUT error.

## Artifacts

- `pipelines/contact/lakeflow_connect.yml` (`db3a5e18fc01`)
- `pipelines/contact/silver_stitch.sql` (`a002d8f24534`)
- `pipelines/contact/adapter_view.sql` (`11f1fac970fd`)
- `pipelines/contact/expectations.yml` (`d72b5d636117`)
- `pipelines/contact/recon_job.py` (`35b74ee107d2`)
- `pipelines/contact/tests/test_pipeline.py` (`79a5ea5e0440`)
- `pipelines/contact/bundle_resource.yml` (`b5a2c194bef8`)

---
_generated_by: pipeline_factory · spec_id: spec-7ec8660b · spec_version: 3_
