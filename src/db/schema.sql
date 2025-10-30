CREATE TABLE dim_state (
  state_id SERIAL PRIMARY KEY,
  state_name TEXT,
  canonical_name TEXT,
  geocode TEXT
);

CREATE TABLE dim_district (
  district_id SERIAL PRIMARY KEY,
  district_name TEXT,
  canonical_name TEXT,
  state_id INTEGER REFERENCES dim_state(state_id),
  geocode TEXT
);

CREATE TABLE dim_crop (
  crop_id SERIAL PRIMARY KEY,
  crop_name TEXT,
  crop_type TEXT
);

CREATE TABLE dataset_registry (
  dataset_id SERIAL PRIMARY KEY,
  title TEXT,
  source_org TEXT,
  api_endpoint TEXT,
  last_updated DATE,
  license TEXT,
  retrieval_date TIMESTAMP DEFAULT now()
);

CREATE TABLE fact_crop_production (
  id SERIAL PRIMARY KEY,
  state_id INTEGER REFERENCES dim_state(state_id),
  district_id INTEGER REFERENCES dim_district(district_id),
  crop_id INTEGER REFERENCES dim_crop(crop_id),
  year INTEGER,
  season TEXT,
  area_hectares FLOAT,
  production_tonnes FLOAT,
  source_dataset INTEGER REFERENCES dataset_registry(dataset_id),
  source_url TEXT,
  raw_row_id TEXT
);

CREATE TABLE fact_rainfall (
  id SERIAL PRIMARY KEY,
  state_id INTEGER REFERENCES dim_state(state_id),
  district_id INTEGER,
  year INTEGER,
  month INTEGER,
  total_mm FLOAT,
  source_dataset INTEGER REFERENCES dataset_registry(dataset_id),
  source_url TEXT,
  raw_row_id TEXT
);
