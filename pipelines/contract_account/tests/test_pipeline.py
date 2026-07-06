# generated_by: pipeline_factory
# spec_id: spec-94139bfa
# spec_version: 6
# DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
"""Rendered smoke tests for the contract_account pipeline artifacts."""

EXPECTED_TARGET_COLUMNS = [
    "account_id",
    "status_code",
    "balance_amount",
    "created_date",
]


def test_target_columns_present(spark):
    df = spark.table("workspace.silver.contract_account")
    for col in EXPECTED_TARGET_COLUMNS:
        assert col in df.columns, f"missing mapped column: {col}"


def test_target_tagged(spark):
    props = {
        row.key: row.value
        for row in spark.sql(
            "SHOW TBLPROPERTIES workspace.silver.contract_account"
        ).collect()
    }
    assert props.get("generated_by") == "pipeline_factory"
    assert props.get("spec_id") == "spec-94139bfa"
