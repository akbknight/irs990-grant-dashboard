# Research Notes — IRS Form 990 Grant Analysis

## IRS Form 990 as a Public Data Source

Form 990 is a federal tax return required of tax-exempt organizations under Section 501(c)(3). The IRS makes 990 filings publicly available through two channels:

1. **IRS SOI Tax Stats**: Annual bulk downloads at tax.gov
2. **AWS S3 Public Dataset**: `s3://irs-form-990/` — machine-readable XML for all e-filed returns since 2011

The AWS dataset is the primary source for the pipeline. XML files are indexed by filing year and EIN. Each XML file corresponds to one 990 filing.

### Schedule I: Grants and Other Assistance

Schedule I (Part II) requires organizations to list every grant or contribution to a domestic organization ≥ $5,000, including:
- Grantee name and EIN
- Address and IRC section status
- Grant purpose description
- Amount of cash grant and non-cash assistance

This schedule is the source for all grant records in this dataset.

---

## Scale of US Philanthropic Sector

For reference, key sector statistics from Giving USA 2024 and Foundation Center data:

- Total US charitable giving (2023): ~$557B (Giving USA)
- Foundation grant-making (2023): ~$105B
- Corporate giving: ~$22B
- Individual giving: ~$374B

The 990 dataset captures primarily foundation and organizational giving, not individual donations. The $550B total in this dataset over 6 years (2019–2024) represents grant-making by 501(c)(3) organizations — primarily foundations and donor-advised funds — not total US charitable giving.

---

## Jewish Philanthropic Sector Context

Relevant benchmarks from publicly available research:

- **Giving to Jewish causes**: Estimated $5–8B annually (Jewish Federations of North America estimates, various years)
- **Jewish DAF giving**: Jewish federations operate major donor-advised fund programs; Federation DAF grants are included in this dataset
- **Major foundation giving**: The dataset captures grant distributions from major Jewish family foundations (not named here), private foundations, and federation grant-making arms

The $10.6B in Jewish grants over 6 years ($1.77B/year average) is broadly consistent with published estimates of organized Jewish grant-making through 990-reporting entities.

---

## Known Data Gaps

1. **Cash donations to individuals**: Schedule I captures organizational grants; direct donations to individuals (another 990 schedule) are not included
2. **Non-e-filers**: Organizations that file paper 990s are not in the XML dataset; primarily very small organizations
3. **Fiscal year variation**: "Tax year 2022" may reflect filings for fiscal years ending in 2022 or 2023, depending on the organization's fiscal year
4. **Purpose field quality**: Grant purpose descriptions are inconsistently completed by filers; subject classification uses NTEE codes, not purpose text, for this reason
