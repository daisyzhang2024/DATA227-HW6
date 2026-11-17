# Corruption Perceptions Index - Data package

This data package contains the data that powers the chart ["Corruption Perceptions Index"](https://ourworldindata.org/grapher/ti-corruption-perception-index?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV structure

Each row is an observation for an entity (usually a country or region) at a timepoint.

- "Entity" — the name of the entity, e.g. "United States".
- "Code" — our internal entity code. For most countries this is the [ISO alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code, e.g. "USA"; historical and other non-standard entities get a custom code.
- "Year" or "Day" — the timepoint. Annual data has a "Year" column holding an integer year; otherwise a "Day" column holds a date string in the form "YYYY-MM-DD".
- Every remaining column is a data column, each one a time series. Downloaded with the "full data" option each corresponds to one time series below; with "only selected data visible in the chart" they are transformed depending on the chart type, so the correspondence may be less direct.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc.

## How we process data at Our World in Data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stitch together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

Preparing this data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/).

## Detailed information about each time series


### Corruption Perceptions Index (CPI)
A country’s score, from 0 (most corrupt) to 100 (least corrupt), that reflects the average of expert surveys on public sector corruption, including misuse of office and bribery.
Last updated: May 13, 2025  
Next expected update: December 2026  
Date range: 2012–2024  
Source: Transparency International (2024) – with minor processing by Our World in Data  

#### How to cite this data

Transparency International (2024) – with minor processing by Our World in Data

#### What you should know about this data
- The Corruption Perceptions Index (CPI) ranks countries and territories based on the perceived level of public sector corruption, as judged by experts and business leaders.
- Depending on the country, it combines data up to 13 independent sources, including expert assessments and business surveys from trusted institutions.
- Each source is converted to a scale from 0 to 100, where 0 means very corrupt and 100 means very clean.
- A country’s CPI score is the simple average of the available sources for that year.
- The method has stayed the same since 2012, so scores can be compared over time.
- The CPI includes a 90% confidence interval (margin of error) to reflect differences between sources and possible inconsistencies.
- The CPI does not measure corruption directly. It measures perceptions, because there are no fully objective national measures of corruption.

#### How this data is described by its producers
The Corruption Perceptions Index (CPI) aggregates information from several sources that capture how business professionals and country experts perceive corruption in the public sector.

To build the CPI, eligible data sources are first selected. A source qualifies only if it measures public‑sector corruption perceptions; relies on a sound, comparable scoring method; is produced by a credible institution; shows enough score variation to differentiate countries; covers a substantial number of nations; bases its ratings on the views of country experts or businesspeople; and is updated at least every two years. The current CPI draws on 13 data sets supplied by 12 separate institutions, each reflecting perceptions recorded during the preceding two years (the accompanying source‑description document details them).

Next, every source is converted to a 0–100 scale, where 0 represents the highest perceived corruption and 100 the lowest. This standardization subtracts the source’s baseline‑year mean from each country’s raw score and divides the result by that source’s baseline‑year standard deviation. The standardized value is then rescaled by multiplying by the CPI’s 2012 standard deviation (20) and adding the CPI’s 2012 mean (45), ensuring scores remain comparable across years while fitting the CPI’s 0–100 range.

Finally, a country or territory enters the CPI only when at least three separate sources assess it. The country’s CPI figure is the arithmetic mean of all its available standardized scores, rounded to the nearest whole number.


### World region according to OWID
Regions defined by Our World in Data, which are used in OWID charts and maps.
Last updated: January 1, 2023  
Date range: 2023–2023  
Source: Our World in Data  

#### How to cite this data

Our World in Data


## Sources

These are the sources behind the data in this package. Each time series above names the ones it draws on in its citation.

### Transparency International – Corruption Perceptions Index

The Corruption Perceptions Index (CPI), produced by Transparency International, ranks countries and territories based on the perceived level of corruption in their public sectors, as evaluated by experts and business executives. It is a composite index that combines data from at least three and up to thirteen independent sources specializing in governance and business climate analysis. These sources provide perception-based assessments, which are necessary since corruption is largely clandestine and cannot be directly measured at a national level. The CPI uses a scale from 0 (highly corrupt) to 100 (very clean) and has been consistently comparable year-to-year since a methodological revision in 2012.
The CPI captures perceptions of public sector corruption in areas such as bribery, diversion of public funds, abuse of office, red tape, meritocracy in public appointments, and protections for whistleblowers. It does not measure private sector corruption, tax fraud, money laundering, or citizens’ personal experiences of corruption. Countries are included only if sufficient data is available, and changes of one or two points in the index are generally not considered statistically significant. The methodology has undergone independent audits, confirming its validity and reliability.

Producer: Transparency International  
Published: 2024  
Retrieved on: 2025-05-13  
Retrieved from: https://www.transparency.org/en/cpi/2024  
Direct download: https://images.transparencycdn.org/images/CPI2024-Results-and-trends.xlsx  
License: CC BY-ND 4.0 (https://images.transparencycdn.org/images/CPI-2024-Methodology.zip)  

Citation: Corruption Perceptions Index (2024) by Transparency International, https://www.transparency.org/en/cpi/2024.

### Our World in Data – Regions

Producer: Our World in Data  

    