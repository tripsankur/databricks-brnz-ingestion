-- generated_by: pipeline_factory
-- spec_id: spec-86caa689
-- spec_version: 3
-- DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
-- Legacy-shaped adapter view: exposes workspace.silver.account in the source shape
-- so downstream consumers keep working during cutover.

CREATE OR REPLACE VIEW workspace.silver.account_legacy_adapter
TBLPROPERTIES (
  'generated_by' = 'pipeline_factory',
  'spec_id' = 'spec-86caa689',
  'spec_version' = '3'
)
AS
SELECT
  `id` AS `Id`,
  `name` AS `Name`,
  `type` AS `Type`,
  `industry` AS `Industry`,
  `annual_revenue` AS `AnnualRevenue`,
  `created_date` AS `CreatedDate`
FROM workspace.silver.account
