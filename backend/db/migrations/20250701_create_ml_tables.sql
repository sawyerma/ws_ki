-- Model Registry
CREATE TABLE IF NOT EXISTS ml_models (
    id String,
    name String,
    type String,
    version String,
    path String,
    features Array(String),
    metrics String,
    status String,
    user String,
    created_at DateTime,
    updated_at DateTime
) ENGINE = MergeTree()
ORDER BY (id);

-- Snapshots
CREATE TABLE IF NOT EXISTS ml_snapshots (
    id String,
    model_id String,
    timestamp DateTime,
    path String,
    config String,
    meta String,
    owner String
) ENGINE = MergeTree()
ORDER BY (id);

-- Templates
CREATE TABLE IF NOT EXISTS ml_templates (
    id String,
    name String,
    type String,
    config_json String,
    owner String,
    created_at DateTime,
    updated_at DateTime
) ENGINE = MergeTree()
ORDER BY (id);

-- AutoML-Jobs
CREATE TABLE IF NOT EXISTS ml_automl_jobs (
    id String,
    model_id String,
    status String,
    params String,
    best_score Float64,
    logs String,
    started_at DateTime,
    finished_at DateTime
) ENGINE = MergeTree()
ORDER BY (id);

-- Indikatoren
CREATE TABLE IF NOT EXISTS ml_indicators (
    id String,
    name String,
    script_ref String,
    config_json String,
    user String,
    shared UInt8 DEFAULT 0,
    created_at DateTime,
    updated_at DateTime
) ENGINE = MergeTree()
ORDER BY (id);
