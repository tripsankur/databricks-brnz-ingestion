-- generated_by: pipeline_factory
-- spec_id: spec-94139bfa
-- spec_version: 3
-- DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
-- Silver stitch: workspace.bronze.aldm_contract_account -> workspace.silver.contract_account via crosswalk join.

CREATE OR REPLACE TABLE workspace.silver.contract_account
TBLPROPERTIES (
  'generated_by' = 'pipeline_factory',
  'spec_id' = 'spec-94139bfa',
  'spec_version' = '3'
)
AS
SELECT
src.`account_id` AS `account_id`,
src.`status_cd` AS `status_code`,
CAST(src.`balance_amount` AS DECIMAL(20, 2)) AS `balance_amount`,
src.`created_dt` AS `created_date`
FROM workspace.bronze.aldm_contract_account AS src
INNER JOIN workspace.silver.crosswalk_account AS xw
ON src.`account_id` = xw.`account_id`
