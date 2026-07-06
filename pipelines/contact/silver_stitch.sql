-- generated_by: pipeline_factory
-- spec_id: spec-7ec8660b
-- spec_version: 1
-- DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
-- Silver stitch: workspace.bronze.sfdc_contact -> workspace.silver.contact via crosswalk join.

CREATE OR REPLACE TABLE workspace.silver.contact
TBLPROPERTIES (
  'generated_by' = 'pipeline_factory',
  'spec_id' = 'spec-7ec8660b',
  'spec_version' = '1'
)
AS
SELECT
src.`Id` AS `id`,
src.`AccountId` AS `account_id`,
src.`FirstName` AS `first_name`,
src.`LastName` AS `last_name`,
lower(src.`Email`) AS `email`,
src.`CreatedDate` AS `created_date`
FROM workspace.bronze.sfdc_contact AS src
INNER JOIN workspace.silver.crosswalk_sfdc_contact AS xw
ON src.`Id` = xw.`id`
