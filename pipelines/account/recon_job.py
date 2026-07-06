# generated_by: pipeline_factory
# spec_id: spec-86caa689
# spec_version: 4
# DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
"""Reconciliation job for account: count + key + attribute-hash compare."""

from pyspark.sql import SparkSession, functions as F

SPEC_ID = "spec-86caa689"
SPEC_VERSION = 4
SOURCE_TABLE = "workspace.bronze.sfdc_account"
TARGET_TABLE = "workspace.silver.account"
CROSSWALK_TABLE = "workspace.silver.crosswalk_sfdc_account"

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
        "source": "Name",
        "target": "name",
        "normalize": "lowercase",
        "tolerance": None,
    },
    {
        "source": "Type",
        "target": "type",
        "normalize": "lowercase",
        "tolerance": None,
    },
    {
        "source": "Industry",
        "target": "industry",
        "normalize": "lowercase",
        "tolerance": None,
    },
    {
        "source": "AnnualRevenue",
        "target": "annual_revenue",
        "normalize": None,
        "tolerance": 0.01,
    },
    {
        "source": "CreatedDate",
        "target": "created_date",
        "normalize": None,
        "tolerance": None,
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
                "account",
                source_count,
                target_count,
                key_match_rate,
            )
        ],
        "recon_id STRING, entity STRING, source_count LONG, target_count LONG, key_match_rate DOUBLE",
    ).withColumn("created_at", F.current_timestamp()).write.mode("append").saveAsTable(
        f"{ctl_schema}.recon_entity_result"
    )
