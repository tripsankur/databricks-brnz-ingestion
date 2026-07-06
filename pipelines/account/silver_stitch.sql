-- generated_by: pipeline_factory
-- spec_id: spec-86caa689
-- spec_version: 1
-- DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
-- Silver stitch: workspace.bronze.sfdc_account -> workspace.silver.account via crosswalk join.

CREATE OR REPLACE TABLE workspace.silver.account
TBLPROPERTIES (
  'generated_by' = 'pipeline_factory',
  'spec_id' = 'spec-86caa689',
  'spec_version' = '1'
)
AS
SELECT
src.`Id` AS `id`,
src.`Name` AS `name`,
src.`Type` AS `type`,
src.`Industry` AS `industry`,
src.`AnnualRevenue` AS `annual_revenue`,
src.`CreatedDate` AS `created_date`
FROM workspace.bronze.sfdc_account AS src
INNER JOIN workspace.silver.crosswalk_sfdc_account AS xw
ON src.`Id` = xw.`id`
