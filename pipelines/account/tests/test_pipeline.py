# generated_by: pipeline_factory
# spec_id: spec-86caa689
# spec_version: 1
# DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
"""Rendered smoke tests for the account pipeline artifacts."""

EXPECTED_TARGET_COLUMNS = [
    "id",
    "name",
    "type",
    "industry",
    "annual_revenue",
    "created_date",
]


def test_target_columns_present(spark):
    df = spark.table("workspace.silver.account")
    for col in EXPECTED_TARGET_COLUMNS:
        assert col in df.columns, f"missing mapped column: {col}"


def test_target_tagged(spark):
    props = {
        row.key: row.value
        for row in spark.sql(
            "SHOW TBLPROPERTIES workspace.silver.account"
        ).collect()
    }
    assert props.get("generated_by") == "pipeline_factory"
    assert props.get("spec_id") == "spec-86caa689"
