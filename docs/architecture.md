# Project Architecture

## Overview
This project is a Terms & Conditions Summarizer that simplifies legal documents
using an LLM-based pipeline.

The system follows a modular architecture to ensure clarity, scalability,
and teamwork.

## Architecture Flow

User / Frontend
↓
API Layer (FastAPI)
↓
Core Pipeline
↓
Services (Scraper, Cleaner, Chunker, Summarizer)
↓
LLM / Mock Model
↓
Response to User

## Folder Structure

- api/        : Handles HTTP requests and responses
- core/       : Contains the main pipeline logic
- services/   : Individual processing units
- models/     : Model loading and configuration
- data/       : Sample and real datasets
- frontend/   : User interface
- tests/      : Unit and integration tests
- docs/       : Project documentation

## Design Principles

- Separation of concerns
- Reusability of components
- Easy testing and maintenance
