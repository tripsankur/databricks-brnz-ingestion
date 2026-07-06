# generated_by: pipeline_factory
# spec_id: spec-94139bfa
# spec_version: 6
# DO NOT EDIT — rendered from the approved spec; changes belong in the spec.
"""Reconciliation job for contract_account: count + key + attribute-hash compare."""

from pyspark.sql import SparkSession, functions as F

SPEC_ID = "spec-94139bfa"
SPEC_VERSION = 6
SOURCE_TABLE = "workspace.bronze.aldm_contract_account"
TARGET_TABLE = "workspace.silver.contract_account"
CROSSWALK_TABLE = "workspace.silver.crosswalk_account"

KEYS = [
    ("account_id", "account_id"),
]

COMPARE_COLUMNS = [
    {
        "source": "account_id",
        "target": "account_id",
        "normalize": None,
        "tolerance": None,
    },
    {
        "source": "status_cd",
        "target": "status_code",
        "normalize": None,
        "tolerance": None,
    },
    {
        "source": "balance_amt",
        "target": "balance_amount",
        "normalize": None,
        "tolerance": 0.01,
    },
    {
        "source": "created_dt",
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
                "contract_account",
                source_count,
                target_count,
                key_match_rate,
            )
        ],
        "recon_id STRING, entity STRING, source_count LONG, target_count LONG, key_match_rate DOUBLE",
    ).withColumn("created_at", F.current_timestamp()).write.mode("append").saveAsTable(
        f"{ctl_schema}.recon_entity_result"
    )
