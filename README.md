# Corsa Studio

Automotive engineering tools inspired by motorsport, built from first principles.

## Features

- **Aerodynamic Drag** — drag force and power from speed, Cd and frontal area
- **Braking & Stopping** — reaction, braking and total stopping distance
- **Power-to-Weight Ratio** — hp/tonne and kg/hp
- **Engine RPM** — wheel and engine RPM from speed, tyres, gear and final drive

## Run the website

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:8000

## Run the calculators from terminal

```bash
python -m calculators.aero_drag
python -m calculators.braking
python -m calculators.power_to_weight_ratio
python -m calculators.rpm_calculator
```

## Deploy to Render

1. Push this repo to GitHub
2. Go to render.com → New Web Service
3. Connect your repo
4. Build: `pip install -r requirements.txt`
5. Start: `gunicorn app:app`

## Author
Siri Tatiparthi
