# Homework 05 — Data Storage

## Data Storage

This homework implements a reproducible data storage layer using environment-driven paths defined in `.env`.

### Folder Structure

- `data/raw/` stores raw CSV files.
- `data/processed/` stores processed Parquet files.

The storage paths are configured using the following environment variables:

```text
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```

### Storage Formats

CSV is used for raw data because it is human-readable, widely supported, and easy to inspect.

Parquet is used for processed data because it preserves data types, supports compression, and provides faster reads for repeated analytical workflows.

### Environment-Driven IO

The notebook reads storage locations from `.env` using `python-dotenv` and `pathlib`.

Using environment variables avoids hardcoded machine-specific paths and makes the workflow easier to reproduce on another computer.

The notebook also creates the required directories automatically if they do not already exist.

### Save and Load Workflow

The sample DataFrame is:

- Saved as CSV in `data/raw/`
- Saved as Parquet in `data/processed/`
- Reloaded using pandas
- Validated after reload

Reusable utility functions are also implemented to automatically detect file format from the file suffix and route read and write operations to CSV or Parquet.

### Validation

After reloading the saved files, the notebook checks:

- Whether the reloaded DataFrame has the same shape as the original DataFrame
- Whether the `date` column remains a datetime type
- Whether the `price` column remains numeric

These validation checks help detect storage-related type drift or structural changes.

### Assumptions and Risks

- A Parquet engine such as `pyarrow` or `fastparquet` must be installed for Parquet read and write operations.
- Files in `data/raw/` are treated as raw inputs and should not be manually edited.
- Processed files should be reproducible from code.
- CSV files may lose data type information when reloaded unless types such as dates are explicitly parsed.
- Storage paths should remain environment-driven rather than hardcoded to a specific operating system or machine.