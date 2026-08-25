
# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
The project aims to support a portfolio manager in making weekly ETF rebalancing decisions by evaluating recent return, volatility, and risk conditions. The main problem is that a strategy that performed well historically may not continue to perform under changing market conditions, transaction costs, liquidity conditions, or shifts in market regime. The analysis will therefore organize historical ETF and market data into a repeatable workflow that summarizes current conditions and eventually produces forward-looking risk estimates. The goal is not to provide an automatic trading recommendation, but to give the decision maker a structured and interpretable basis for deciding whether portfolio exposure should be maintained, reduced, or reviewed more closely.

## Stakeholder & User
Decision owner: Portfolio Manager

Tool/operator: Investment Analyst

Timing & workflow context: The analysis is reviewed on a weekly basis before portfolio rebalancing decisions are made.

## Useful Answer & Decision
Type: Primarily predictive, supported by descriptive analysis.

Metric or artifact: Weekly return and volatility summaries, forward-looking risk bands or prediction intervals, scenario notes, and clearly defined decision triggers for when the portfolio manager should review current ETF exposure.

## Assumptions & Constraints
1. Historical return and volatility patterns contain some information relevant to near-term risk.
ETF prices and trading data are sufficiently liquid and reliable for analysis.
Transaction costs and market impact are not negligible and must be considered when interpreting a rebalance signal.
2. Relationships observed in historical data may be approximately stable over short horizons, but this assumption must be tested.
3. Data availability and refresh timing must support a weekly decision window.
4. The project is intended as decision support rather than fully automated execution.
Model complexity and runtime should remain manageable enough for a repeatable weekly workflow.

## Known Unknowns / Risks
1. Market regime changes may make historical relationships unstable.
2. The appropriate benchmark for evaluating ETF performance may need further refinement.
3. Transaction costs or liquidity conditions may change over time.
4. Historical data may contain missing values or structural biases.
5. The most appropriate forecasting horizon and evaluation metric may need to be validated empirically.
6. Predictive performance may deteriorate when market conditions differ materially from the training period.

## Lifecycle Mapping
Goal: Support weekly ETF rebalancing decisions
→ Stage 01: Problem Framing & Scoping
→ Deliverable: Scoping paragraph, stakeholder definition, assumptions/risk list, and repo structure

Goal: Obtain reliable ETF and market data
→ Data Acquisition
→ Deliverable: Reproducible raw market dataset

Goal: Prepare reliable modeling inputs
→ Data Preprocessing + EDA
→ Deliverable: Clean dataset and documented data-quality findings

Goal: Identify useful predictive signals
→ Feature Engineering
→ Deliverable: Return, volatility, trend, and market-condition features

Goal: Estimate near-term ETF risk
→ Modeling
→ Deliverable: Forecasts, prediction intervals, or risk bands

Goal: Support portfolio review decisions
→ Evaluation & Risk Communication
→ Deliverable: Performance metrics, scenario analysis, and decision-support summary

## Repo Plan
data/
    raw/
    processed/

src/
    reusable data-processing and modeling functions

notebooks/
    exploratory analysis and model experiments

docs/
    stakeholder memo and project documentation

reports/
    analysis outputs and decision-support summaries

model/
    saved model artifacts 

README.md
    project framing, assumptions, risks, and lifecycle mapping
