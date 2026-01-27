# Awesome World Labs Robotics 🌍🤖

> "The definitive resource for Spatial Intelligence in Robotics powered by World Labs."

A curated, community-driven collection of high-fidelity prompts, synthetic world definitions, and scenario blueprints for training the next generation of embodied AI.

## 🚀 Mission
Physical intelligence requires physical data. This repository leverages the **World Labs API** to generate unlimited, photorealistic, and 3D-consistent environments ("Digital Twins") for robotics training—ranging from domestic chores to complex industrial assembly.

## 📂 Repository Structure

- **`scripts/`**:
    - `generate_with_api.py`: **(Core Tool)** A powerful script pre-loaded with 15+ robotics scenarios (Industrial, Medical, Domestic, etc.) to generate 3D worlds on demand.
- **`prompts/`**:
    - `core_collection.json`: Structured JSON tasks linked to specific environments (e.g., "Plug in ethernet cable" -> "Data Center").
- **`worlds/`**:
    - `api_renders/`: The output directory where your generated world thumbnails and assets are saved.

## 🌍 Supported Scenarios
We have pre-configured blueprints for diverse robotics domains:

### 🏠 Domestic & Residential
- **Domestic Kitchen**: For manipulation (chopping, dishwashing).
- **Cluttered Bedroom**: For complex object segmentation and laundry folding.
- **Messy Airbnb**: For general housekeeping and "tidy-up" tasks.

### 🏭 Industrial & Logistics
- **Warehouse Logistics**: Autonomous Mobile Robot (AMR) navigation and path planning.
- **PCB Assembly Line**: High-precision fine motor control and inspection.
- **Data Center**: Cable management and server maintenance.
- **Automotive Cell**: Heavy lifting and welding simulation targets.

### 🏥 Service & Commercial
- **Hospital Corridor**: Sterile delivery and patient assistance.
- **Hotel Reception**: Social navigation and concierge tasks.
- **Restaurant Dining**: Dynamic obstacle avoidance (chairs/guests).
- **Supermarket**: Shelf inventory scanning and restocking.

### 🚧 Outdoor & Unstructured
- **City Sidewalk**: Last-mile delivery robot training.
- **Construction Site**: Rough terrain locomotion (quadrupeds).
- **Disaster Zone**: Search and Rescue (SAR) in rubble.
- **Agriculture**: Crop monitoring and harvesting.

## ⚡ Quick Start

### 1. Prerequisite
You need a [World Labs Platform](https://platform.worldlabs.ai) account and API key.

1. Create a `.env` file:
   ```bash
   cp .env.example .env
   ```
2. Add your key:
   ```
   WLT_API_KEY=wl_...
   ```

### 2. Generate Worlds
We have automated the creation of reference environments. Run the script to generate verified scenarios:

```bash
# Generates all configured scenarios using the World Labs API
python3 scripts/generation/generate_with_api.py
```

*Note: This utilizes the `Marble 0.1-mini` model for speed and efficiency.*

### 3. Use the Prompts
Load our structured prompts to test your robot's reasoning against these worlds.
```python
import json
with open("prompts/core_collection.json", "r") as f:
    tasks = json.load(f)

# Example: Get a task for the Data Center environment
cable_task = [t for t in tasks[1]["prompts"] if t["id"] == "manip_cable_01"][0]
print(f"Task: {cable_task['task']}")
```

## 🤝 Contributing
Have a new robotics use case?
1. Fork the repo.
2. Add your scenario to `generate_with_api.py`.
3. Add a corresponding task to `prompts/core_collection.json`.
4. Submit a Pull Request!

## 📜 License
MIT License.
