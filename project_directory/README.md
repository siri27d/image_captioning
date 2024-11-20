# Multilingual Assistive Model

## Overview
This project provides a multilingual assistive web application that helps visually impaired users by:
1. Describing images in multiple Indian languages.
2. Narrating the descriptions via audio.

## Workflow
1. Image Captioning: Using BLIP or Vision Transformer to generate captions.
2. Translation: Translating captions into Indian languages using IndicTrans2.
3. Audio Narration: Converting translated text to speech using Whisper.

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

## Deployment
Package the project and deploy it to Render or a similar platform.
