# Official Data Sources & Technical Constraints Register

**Project Context:** Philanthropic Capital Flow Intelligence & Municipal City-Map Telemetry  
**Author:** Akshay Kumar (`akbknight`)  
**Date:** October 22, 2026  
**Status:** Verified Official Public Records & API Specifications  

---

## 1. Philanthropic Intelligence Engine Sources (Primary Dashboard)

### A. ProPublica Nonprofit Explorer API (Version 2)
- **Documentation URL:** [https://projects.propublica.org/nonprofits/api](https://projects.propublica.org/nonprofits/api)
- **API Base URL:** `https://projects.propublica.org/nonprofits/api/v2/`
- **Core Endpoints Utilized:**
  - `GET /search.json?q={search_term}`: Full-text search across 1.8M+ tax-exempt organizations by legal name, DBA, state, or NTEE code.
  - `GET /organizations/{ein}.json`: Single entity record returning verified legal name, 9-digit EIN, address, NTEE category, latest tax year, balance sheet assets, total revenues, and itemized multi-year filings.
- **Access Requirements & Cost:** Free public API. No API key required for standard v2 search and organization endpoints.
- **Geographic Coverage:** Complete United States (all 50 states, District of Columbia, Puerto Rico, and U.S. territories).
- **Update Interval:** Updated semi-monthly as IRS releases new electronic filings and paper-scanned documents.
- **Attribution & Licensing:** ProPublica Nonprofit Explorer data is released under Creative Commons Attribution-NonCommercial-NoDerivs 3.0 (CC BY-NC-ND 3.0). Attribution to "ProPublica Nonprofit Explorer & IRS" is mandatory.
- **Usage Limits & Best Practices:** Respectful rate limiting (~1 to 2 requests/sec). Implement client-side `localStorage` caching with 24-hour TTL and exponential backoff retry logic.

### B. IRS Tax Exempt Organization Search (TEOS) & AWS Open Data Registry
- **Documentation URL:** [https://registry.opendata.aws/irs990/](https://registry.opendata.aws/irs990/)
- **Bucket Location:** `s3://irs-form-990/` (AWS Region: `us-east-1`)
- **Data Format:** Raw XML electronic returns (`Form 990`, `Form 990-PF`, `Form 990-EZ`) and index CSVs (`index_2019.csv` through `index_2024.csv`).
- **Access Requirements & Cost:** Free public access hosted under the AWS Open Data Sponsorship Program. No AWS credentials required for requester-pays-exempt public buckets.
- **Geographic Coverage:** Nationwide US tax-exempt entities.
- **Update Interval:** Monthly IRS e-file bulk drops.
- **Pipeline Role:** Backend offline/scheduled ingestion (`master_pipeline.py` in `form990-grant-miner`). Decompresses XML returns in-memory to extract Schedule I Part II grants.

### C. IRS Exempt Organization Business Master File (EO BMF)
- **Documentation URL:** [https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf](https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf)
- **Format:** Cumulative tabular CSV files partitioned into 4 geographic regions.
- **Access Requirements & Cost:** Free public download from IRS.gov.
- **Update Interval:** Monthly updates by the IRS.
- **Pipeline Role:** Authoritative source for organization active status, foundation code, ruling date, deductible deductibility code, and NTEE classification.

---

## 2. Municipal City & Mobility Telemetry (Proposed Dedicated Module)

For the separate 3D City / Mobility Map module (`city-mobility-dashboard`), the following official, free public sources have been researched and verified:

### A. National Weather Service (NWS) API
- **Documentation URL:** [https://www.weather.gov/documentation/services-web-api](https://www.weather.gov/documentation/services-web-api)
- **API Base URL:** `https://api.weather.gov/`
- **Core Endpoints:**
  - `GET /points/{latitude},{longitude}`: Resolves station grid and forecast office.
  - `GET /stations/{stationId}/observations/latest`: Real-time temperature, dewpoint, wind velocity, barometric pressure, precipitation, and visibility.
  - `GET /alerts/active?point={lat},{lon}`: Official active weather warnings, watches, and advisories.
- **Access Requirements & Cost:** Free public API provided by NOAA. No API key required; requires a descriptive `User-Agent` header with contact email.
- **Update Interval:** Surface observations update every 5 to 20 minutes depending on ASOS/AWOS sensor station cycle.
- **Critical Limitation Notice:** NWS reports **ambient air temperature**, not **road-surface temperature**. Road icing cannot be inferred solely from air temperature.

### B. General Bikeshare Feed Specification (GBFS)
- **Documentation URL:** [https://gbfs.org/](https://gbfs.org/)
- **Live Example (Capital Bikeshare / Washington D.C.):**
  - Station Information: `https://gbfs.capitalbikeshare.com/gbfs/en/station_information.json`
  - Station Status: `https://gbfs.capitalbikeshare.com/gbfs/en/station_status.json`
- **Access Requirements & Cost:** Free, open, public JSON feed. No authentication required.
- **Update Interval:** Polling frequency every 60 seconds.
- **Data Provided:** Real-time dock capacity, available mechanical bikes, available e-bikes, disabled docks, and station operating status.

### C. Public Transit Realtime (WMATA / GTFS Realtime)
- **Documentation URL:** [https://developer.wmata.com/](https://developer.wmata.com/) (Washington D.C. Metropolitan Area)
- **Access Requirements & Cost:** Free developer tier with registration (API key required in `api_key` header).
- **Core Endpoints:** Real-time Metrorail station predictions, train positions, elevator/escalator outages, and Metrobus live vehicle locations.
- **Update Interval:** Polling intervals of 15 to 30 seconds for live arrivals; 7-day schedules for static GTFS.

### D. Road Surface & Environmental Telemetry: Truth & Constraints
- **Road Weather Information Systems (RWIS):** State DOTs (e.g., Maryland MDOT, Virginia VDOT, DC DDOT) operate specialized embedded road probes measuring sub-surface temperature, surface temperature, chemical concentration, and freeze point.
- **Access Status:** Most state RWIS sensor feeds require authorized agency partnerships or inter-governmental data exchange agreements.
- **Important Invariant:** Where road surface sensors are unavailable, the dashboard must explicitly display **"Road Surface Sensor: Not Deployed / Unavailable"** rather than fabricating estimated pavement temperatures from air temperature.
- **Treatment Guidance Invariant:** Any road treatment analysis (e.g. anti-icing brine or salt application) must be explicitly classified as **"Advisory Simulation"** requiring qualified municipal human engineer review. The dashboard will never issue autonomous control commands to road equipment or drones.
