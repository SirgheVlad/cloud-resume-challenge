# Cloud Resume Challenge - Visitor Counter

[![Build Status](https://github.com/SirgheVlad/cloud-resume-challenge/actions/workflows/pipeline.yml/badge.svg)](https://github.com/YOUR_USERNAME/cloud-resume-challenge/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the infrastructure and code for the visitor counter component of the Cloud Resume Challenge, implemented using AWS Serverless Application Model (SAM). The project demonstrates Infrastructure as Code (IaC), API integration, and automated deployment with GitHub Actions.

## Live Demo
Visit my resume site: [https://sirghevladaws.com/](https://sirghevladaws.com/) to see the visitor counter in action!

## Project Overview
- **Purpose**: A serverless visitor counter for my resume website, incrementing with each page load.
- **Technologies**:
  - AWS SAM for IaC.
  - AWS Lambda (Python 3.9) for the counter logic.
  - Amazon DynamoDB for storing the visitor count.
  - Amazon API Gateway for the REST endpoint.
  - GitHub Actions for CI/CD.

## Architecture
- **DynamoDB Table**: `VisitorCountNew` stores the count with `id: "resume"` as the key.
- **Lambda Function**: `updateVisitorCountNew` increments the count and returns it via API.
- **API Gateway**: Exposes the `/count` endpoint at `https://o1ck7ephj0.execute-api.us-east-1.amazonaws.com/Prod/count`.
- **Frontend**: JavaScript on the resume site fetches and displays the count.

## Setup Instructions
1. **Prerequisites**:
   - AWS CLI configured with credentials.
   - SAM CLI installed (`brew install aws-sam-cli` on macOS).
   - Git and a GitHub account.
2. **Installation**:
   - Clone this repository:
     ```bash
     git clone https://github.com/SirgheVlad/cloud-resume-challenge.git
     cd visitor-counter
