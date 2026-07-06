-- generated_by: pipeline_factory
-- spec_id: spec-7ec8660b
-- spec_version: 3
-- DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
-- Legacy-shaped adapter view: exposes workspace.silver.contact in the source shape
-- so downstream consumers keep working during cutover.

CREATE OR REPLACE VIEW workspace.silver.contact_legacy_adapter
TBLPROPERTIES (
  'generated_by' = 'pipeline_factory',
  'spec_id' = 'spec-7ec8660b',
  'spec_version' = '3'
)
AS
SELECT
  `id` AS `Id`,
  `account_id` AS `AccountId`,
  `first_name` AS `FirstName`,
  `last_name` AS `LastName`,
  `email` AS `Email`,
  `created_date` AS `CreatedDate`
FROM workspace.silver.contact
