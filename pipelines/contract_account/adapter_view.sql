-- generated_by: pipeline_factory
-- spec_id: spec-94139bfa
-- spec_version: 7
-- DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
-- Legacy-shaped adapter view: exposes workspace.silver.contract_account in the source shape
-- so downstream consumers keep working during cutover.

CREATE OR REPLACE VIEW workspace.silver.contract_account_legacy_adapter
TBLPROPERTIES (
  'generated_by' = 'pipeline_factory',
  'spec_id' = 'spec-94139bfa',
  'spec_version' = '7'
)
AS
SELECT
  `account_id` AS `account_id`,
  `status_code` AS `status_cd`,
  `balance_amount` AS `balance_amt`,
  `created_date` AS `created_dt`
FROM workspace.silver.contract_account
