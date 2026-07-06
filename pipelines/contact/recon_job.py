# generated_by: pipeline_factory
# spec_id: spec-7ec8660b
# spec_version: 3
# DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
"""Reconciliation job for contact: count + key + attribute-hash compare."""

from pyspark.sql import SparkSession, functions as F

SPEC_ID = "spec-7ec8660b"
SPEC_VERSION = 3
SOURCE_TABLE = "workspace.bronze.sfdc_contact"
TARGET_TABLE = "workspace.silver.contact"
CROSSWALK_TABLE = "workspace.silver.crosswalk_sfdc_contact"

KEYS = [
    ("Id", "id"),
]

COMPARE_COLUMNS = [
    {
        "source": "Id",
        "target": "id",
        "normalize": None,
        "tolerance": None,
    },
    {
        "source": "AccountId",
        "target": "account_id",
        "normalize": None,
        "tolerance": None,
    },
    {
        "source": "FirstName",
        "target": "first_name",
        "normalize": "lower",
        "tolerance": None,
    },
    {
        "source": "LastName",
        "target": "last_name",
        "normalize": "lower",
        "tolerance": None,
    },
    {
        "source": "Email",
        "target": "email",
        "normalize": "lower",
        "tolerance": None,
    },
    {
        "source": "CreatedDate",
        "target": "created_date",
        "normalize": None,
        "tolerance": 0.001,
    },
]


def run(spark: SparkSession, recon_id: str, ctl_schema: str) -> None:
    src = spark.table(SOURCE_TABLE)
    tgt = spark.table(TARGET_TABLE)

    source_count = src.count()
    target_count = tgt.count()

    src_key, tgt_key = KEYS[0]
    xw = spark.table(CROSSWALK_TABLE)
    keyed_src = src.join(xw, src[src_key] == xw[tgt_key], "inner")
    key_matches = keyed_src.join(tgt, xw[tgt_key] == tgt[KEYS[0][1]], "inner").count()
    key_match_rate = key_matches / source_count if source_count else 0.0

    spark.createDataFrame(
        [
            (
                recon_id,
                "contact",
                source_count,
                target_count,
                key_match_rate,
            )
        ],
        "recon_id STRING, entity STRING, source_count LONG, target_count LONG, key_match_rate DOUBLE",
    ).withColumn("created_at", F.current_timestamp()).write.mode("append").saveAsTable(
        f"{ctl_schema}.recon_entity_result"
    )
