# API Usage Guide

## Base URL
http://127.0.0.1:8000

## Health Check
GET /health

Response:
{
  "status": "OK",
  "message": "API is healthy"
}

## Summarize Terms & Conditions
POST /summarize

Request Body:
{
  "text": "Terms and Conditions text",
  "url": null,
  "summary_type": "simple"
}

summary_type values:
- simple
- simplified
- risk

Response:
{
  "summary": "Summarized text",
  "key_points": [],
  "risk_notes": []
}

## Dataset Summary (Optional)
GET /summarize-data-file

Description:
Summarizes the dataset stored in data/data.txt
