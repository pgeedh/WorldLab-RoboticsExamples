<div align="center">

# 🌍🤖 World Labs Robotics Examples

**Hyper-realistic "Digital Twins" for robotics training generated via World Labs LWMs**  
*Powered by [World Labs](https://www.worldlabs.ai/)*

[![World Labs API](https://img.shields.io/badge/World%20Labs-API%20v1-black?style=for-the-badge&logo=openai&logoColor=white)](https://platform.worldlabs.ai)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-green?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

[**📚 Documentation**](https://docs.worldlabs.ai) | [**🚀 Get Started**](#-quick-start) | [**🐙 GitHub Repo**](https://github.com/pgeedh/WorldLab-RoboticsExamples)

</div>

---

## 📖 About
**WorldLab Robotics Examples** bridges the gap between **Generative AI** and **Embodied Intelligence**. Traditional simulations are too sterile; real-world data is too expensive. We use **World Labs' Large World Models (LWMs)** to generate "Physically Grounded Digital Twins"—chaotic, photorealistic, and 3D-consistent environments engineering-grade spatial reasoning.

Whether you are testing a **quadruped on a construction site**, a **manipulator in a messy bedroom**, or a **social robot in a hotel lobby**, this repository provides the "Digital Twin" blueprints you need.
Physical intelligence requires physical data. This repository leverages the **World Labs API** to generate unlimited, photorealistic, and 3D-consistent environments ("Digital Twins") for robotics training—ranging from domestic chores to complex industrial assembly.

## 📸 Visual Catalog & High-Fidelity Prompts
Below are the "Digital Twin" blueprints available in this repository. Each prompt is engineered for specific robotics vision and interaction tasks.

### 🏠 Domestic & Residential

#### Domestic Kitchen (Robotics Training)
> **Prompt**: "A hyper-realistic, robot-centric digital twin of a modern domestic kitchen. Captured from a 1.2m height (robot eye level). Key interaction zones include a granite island with specific grasping targets..."

[![Domestic Kitchen](worlds/api_renders/domestic_kitchen_robotics_thumbnail.jpg)](https://marble.worldlabs.ai/world/7d2f87be-7c76-4367-873c-e6833b8965e5)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/7d2f87be-7c76-4367-873c-e6833b8965e5)**

#### Cluttered Bedroom (Manipulation)
> **Prompt**: "A physically simulated messy bedroom for high-complexity manipulation training... A tangled pile of laundry (red t-shirt, blue jeans, white socks) rests on an unmade bed..."

[![Cluttered Bedroom](worlds/api_renders/cluttered_bedroom_manipulation_thumbnail.jpg)](https://marble.worldlabs.ai/world/627c431e-1d72-4337-b524-48aeba0d8036)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/627c431e-1d72-4337-b524-48aeba0d8036)**

#### Messy Airbnb (Housekeeping)
> **Prompt**: "A 'lived-in' living room state for housekeeping robots. An open suitcase sits on a rug, spilling patterned clothing... The scene tests the robot's ability to distinguish between 'trash' and 'personal items'..."

[![Messy Airbnb](worlds/api_renders/messy_airbnb_living_room_thumbnail.jpg)](https://marble.worldlabs.ai/world/dc8c046a-f4ad-438f-afc7-e2bc5b124333)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/dc8c046a-f4ad-438f-afc7-e2bc5b124333)**

### 🏭 Industrial & Logistics

#### Industrial Warehouse (Navigation)
> **Prompt**: "A precision-mapped industrial warehouse aisle. High-contrast yellow safety lines painted on polished concrete floors. Metal racking units... Fiducial markers (QR codes) visible on shelf edges..."

[![Industrial Warehouse](worlds/api_renders/industrial_warehouse_logistics_thumbnail.jpg)](https://marble.worldlabs.ai/world/ab364263-7f65-4b97-b414-7773f1ae3fcd)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/ab364263-7f65-4b97-b414-7773f1ae3fcd)**

#### PCB Assembly Line (Fine Motor)
> **Prompt**: "Macro-photography view of an electronics assembly workbench. A green PCB (Printed Circuit Board) is clamped in a holder... Nearby components: a tray of tiny 0402 resistors..."

[![PCB Assembly](worlds/api_renders/electronic_assembly_line_pcb_thumbnail.jpg)](https://marble.worldlabs.ai/world/63914b19-8036-46a3-8d83-87bf29ab046a)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/63914b19-8036-46a3-8d83-87bf29ab046a)**

#### Data Center (Cable Maintenance)
> **Prompt**: "**System Role:** Senior Simulation Engineer specializing in Deformable Linear Objects (DLOs)... **Objective:** Generate a high-fidelity 3D simulation environment for 'Data Center Cable Remediation'..."

[![Data Center](worlds/api_renders/data_center_wire_maintenance_thumbnail.jpg)](https://marble.worldlabs.ai/world/fcc76d94-2e36-4bae-bd34-65a725b4df50)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/fcc76d94-2e36-4bae-bd34-65a725b4df50)**

#### Automotive Robotic Cell (Welding)
> **Prompt**: "A heavy-industry automotive welding cell. A raw steel car chassis acts as the central workspace. Orange industrial robotic arms (KUKA-style)... Sparks from a spot welder are frozen in mid-air..."

[![Automotive Cell](worlds/api_renders/automotive_assembly_robotic_cell_thumbnail.jpg)](https://marble.worldlabs.ai/world/f6291ad6-b1de-4a84-b4d7-def1f3374777)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/f6291ad6-b1de-4a84-b4d7-def1f3374777)**

### 🏥 Service & Commercial

#### Hotel Reception (Concierge)
> **Prompt**: "A 5-star hotel lobby designed for social navigation. Polished marble floors reflecting the environment... The space is populated with 'ghost' proxies of people... Luggage carts with brass railings..."

[![Hotel Reception](worlds/api_renders/hotel_reception_concierge_thumbnail.jpg)](https://marble.worldlabs.ai/world/ea143b63-9aaa-4731-82fa-699d319e3467)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/ea143b63-9aaa-4731-82fa-699d319e3467)**

#### Restaurant Dining (Crowded Nav)
> **Prompt**: "A dense restaurant dining floor layout. Round tables covered in white cloth... Chairs are pulled out at irregular angles, narrowing the navigation path to <60cm. Ambient lighting is dim/moody..."

[![Restaurant Dining](worlds/api_renders/restaurant_dining_service_thumbnail.jpg)](https://marble.worldlabs.ai/world/68cd246f-e7c0-4d70-a4a3-8114ca718fe1)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/68cd246f-e7c0-4d70-a4a3-8114ca718fe1)**

#### Hospital Corridor (Delivery)
> **Prompt**: "A sterile, bright hospital corridor. High-gloss vinyl flooring. Walls are white with color-coded wayfinding strips. Obstacles include a crash cart... Lighting is clinical fluorescent..."

[![Hospital Corridor](worlds/api_renders/hospital_corridor_medic_thumbnail.jpg)](https://marble.worldlabs.ai/world/5d1910e6-388c-427e-b46b-3afcd3f37da1)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/5d1910e6-388c-427e-b46b-3afcd3f37da1)**

#### Supermarket Shelves (Inventory)
> **Prompt**: "A planogram-compliant supermarket aisle. Shelves are fully stocked with colorful cereal boxes... Several items are intentionally missing (out-of-stock) to test gap detection. Price tags on the shelf edge are legible..."

[![Supermarket](worlds/api_renders/retail_supermarket_shelves_thumbnail.jpg)](https://marble.worldlabs.ai/world/617f71d8-cdc2-482a-9404-f7b52742b7f5)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/617f71d8-cdc2-482a-9404-f7b52742b7f5)**

### 🚧 Outdoor & Unstructured

#### City Sidewalk (Delivery Rover)
> **Prompt**: "First-person view from a delivery rover on a city sidewalk. Paved concrete slabs with cracks and chewing gum stains. A fire hydrant (red) and a parking meter (gray) act as static obstacles..."

[![City Sidewalk](worlds/api_renders/city_sidewalk_delivery_thumbnail.jpg)](https://marble.worldlabs.ai/world/f55d87b3-5b04-4957-b0c6-c5b61b2515cc)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/f55d87b3-5b04-4957-b0c6-c5b61b2515cc)**

#### Construction Site (Quadruped Locomotion)
> **Prompt**: "An active chaotic construction site. Ground is uneven, covered in loose gravel and sand. Piles of red bricks and wooden pallets create traversability barriers. Exposed steel rebar acts as a snagging hazard..."

[![Construction Site](worlds/api_renders/construction_site_inspection_thumbnail.jpg)](https://marble.worldlabs.ai/world/34fa8a79-cf28-4301-bf4d-18dad73beae3)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/34fa8a79-cf28-4301-bf4d-18dad73beae3)**

#### Disaster Zone (Search & Rescue)
> **Prompt**: "A simulated post-earthquake rubble pile. Broken slabs of concrete, twisted rebar, and shattered glass... Atmospheric dust/haze reduces visibility to 80%. Lighting is low-angle, simulating dusk..."

[![Disaster Zone](worlds/api_renders/disaster_rubble_search_thumbnail.jpg)](https://marble.worldlabs.ai/world/c1960823-f5ab-408c-b105-1db841f49276)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/c1960823-f5ab-408c-b105-1db841f49276)**

#### Agricultural Field (Perception)
> **Prompt**: "A robotic agriculture perception dataset. Parallel rows of green corn crops, approximately 1.5m high. The inter-row path is dirt with random weeds. Sunlight is directly overhead (noon)..."

[![Agricultural Field](worlds/api_renders/agricultural_field_crop_thumbnail.jpg)](https://marble.worldlabs.ai/world/0b265eee-01c6-4c5c-8a0b-8ec9ac53d9da)
👉 **[Click to Explore 3D World](https://marble.worldlabs.ai/world/0b265eee-01c6-4c5c-8a0b-8ec9ac53d9da)**

---

## 📂 Repository Structure

- **`scripts/`**:
    - `generate_with_api.py`: **(Core Tool)** A powerful script pre-loaded with 15+ robotics scenarios to generate 3D worlds on demand.
- **`prompts/`**:
    - `core_collection.json`: Structured JSON tasks linked to specific environments (e.g., "Plug in ethernet cable" -> "Data Center").
- **`worlds/`**:
    - `api_renders/`: The output directory where your generated world thumbnails and assets are saved.

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

---

<div align="center">
  <b>Made with ❤️ by <a href="https://github.com/pgeedh">Pruthvi Geedh</a></b>
</div>
