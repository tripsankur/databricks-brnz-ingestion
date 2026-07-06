# generated_by: pipeline_factory
# spec_id: spec-7ec8660b
# spec_version: 1
# DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
"""Rendered smoke tests for the contact pipeline artifacts."""

EXPECTED_TARGET_COLUMNS = [
    "id",
    "account_id",
    "first_name",
    "last_name",
    "email",
    "created_date",
]


def test_target_columns_present(spark):
    df = spark.table("workspace.silver.contact")
    for col in EXPECTED_TARGET_COLUMNS:
        assert col in df.columns, f"missing mapped column: {col}"


def test_target_tagged(spark):
    props = {
        row.key: row.value
        for row in spark.sql(
            "SHOW TBLPROPERTIES workspace.silver.contact"
        ).collect()
    }
    assert props.get("generated_by") == "pipeline_factory"
    assert props.get("spec_id") == "spec-7ec8660b"
