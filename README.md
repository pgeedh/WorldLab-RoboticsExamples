# Awesome World Labs Robotics 🌍🤖

> "The definitive resource for Spatial Intelligence in Robotics powered by World Labs."

A curated, community-driven collection of high-fidelity prompts, synthetic world definitions, and scenario blueprints for training the next generation of embodied AI.

## 🚀 Mission
Physical intelligence requires physical data. This repository leverages the **World Labs API** to generate unlimited, photorealistic, and 3D-consistent environments ("Digital Twins") for robotics training—ranging from domestic chores to complex industrial assembly.

## 📸 Visual Catalog & High-Fidelity Prompts
Below are the "Digital Twin" blueprints available in this repository. Each prompt is engineered for specific robotics vision and interaction tasks.

### 🏠 Domestic & Residential

#### Domestic Kitchen (Robotics Training)
> **Prompt**: "A hyper-realistic, robot-centric digital twin of a modern domestic kitchen. Captured from a 1.2m height (robot eye level). Key interaction zones include a granite island with specific grasping targets: a glossy red apple, a matte ceramic mug with a handle facing right, and a white flat plate. Lighting is even, diffuse studio lighting to minimize harsh shadows. The floor is hardwood with clear traction texture. No motion blur. optimized for object detection and depth estimation."

![Domestic Kitchen](worlds/api_renders/domestic_kitchen_robotics_thumbnail.jpg)

#### Cluttered Bedroom (Manipulation)
> **Prompt**: "A physically simulated messy bedroom for high-complexity manipulation training. A tangled pile of laundry (red t-shirt, blue jeans, white socks) rests on an unmade bed with wrinkled linens. The floor is scattered with hardcover books, circular plastic toys, and a charging cable. Textures are high-fidelity to test segmentation algorithms. Soft morning light entering from a window on the left, casting realistic shadows for volumetric reasoning."

![Cluttered Bedroom](worlds/api_renders/cluttered_bedroom_manipulation_thumbnail.jpg)

#### Messy Airbnb (Housekeeping)
> **Prompt**: "A 'lived-in' living room state for housekeeping robots. An open suitcase sits on a rug, spilling patterned clothing. A coffee table is cluttered with empty soda cans, a crumpled magazine, and a TV remote. Cushions are thrown haphazardly on the floor. The scene tests the robot's ability to distinguish between 'trash' (cans) and 'personal items' (clothing). Photorealistic, 8k resolution, neutral color temperature."

![Messy Airbnb](worlds/api_renders/messy_airbnb_living_room_thumbnail.jpg)

### 🏭 Industrial & Logistics

#### Industrial Warehouse (Navigation)
> **Prompt**: "A precision-mapped industrial warehouse aisle. High-contrast yellow safety lines painted on polished concrete floors. Metal racking units on both sides are stocked with brown cardboard boxes of uniform size (30x30cm), some slightly misaligned to test grasping tolerance. Bright, cool-white overhead LED lighting strips to eliminate dark corners. Fiducial markers (QR codes) visible on shelf edges for localization."

![Industrial Warehouse](worlds/api_renders/industrial_warehouse_logistics_thumbnail.jpg)

#### PCB Assembly Line (Fine Motor)
> **Prompt**: "Macro-photography view of an electronics assembly workbench. A green PCB (Printed Circuit Board) is clamped in a holder. Solder flux residue is visible. Nearby components: a tray of tiny 0402 resistors, a soldering iron with a oxidized tip, and a pair of fine-point tweezers. The lighting is a focused ring light to highlight metallic leads and solder joints for defect detection algorithms. Depth of field is shallow, focused on the PCB."

![PCB Assembly](worlds/api_renders/electronic_assembly_line_pcb_thumbnail.jpg)

#### Data Center (Cable Maintenance)
> **Prompt**: "A narrow server aisle in a hyperscale data center. Densely packed server racks with blinking status LEDs (green/amber). The focus is on the rear cable management area: a chaotic mix of blue (CAT6) and orange (Fiber) cables. Some cables are unplugged and hanging loose. The environment is metallic, reflective, and cool-toned. Intricate geometry for occlusion testing. 4k resolution."

![Data Center](worlds/api_renders/data_center_wire_maintenance_thumbnail.jpg)

#### Automotive Robotic Cell (Welding)
> **Prompt**: "A heavy-industry automotive welding cell. A raw steel car chassis acts as the central workspace. Orange industrial robotic arms (KUKA-style) are positioned around it. Sparks from a spot welder are frozen in mid-air (simulated). The floor is metal grating. Warning signs and safety cages are clearly visible globally. High dynamic range lighting to handle the brightness of welding arcs."

![Automotive Cell](worlds/api_renders/automotive_assembly_robotic_cell_thumbnail.jpg)

### 🏥 Service & Commercial

#### Hotel Reception (Concierge)
> **Prompt**: "A 5-star hotel lobby designed for social navigation. Polished marble floors reflecting the environment. A high concierge desk made of mahogany. The space is populated with 'ghost' proxies of people (blurred or static) to simulate crowd density without privacy issues. Luggage carts with brass railings are obstacles. Warm, inviting architectural lighting. Wide angle field of view."

![Hotel Reception](worlds/api_renders/hotel_reception_concierge_thumbnail.jpg)

#### Restaurant Dining (Crowded Nav)
> **Prompt**: "A dense restaurant dining floor layout. Round tables covered in white cloth, set with silverware and transparent wine glasses (challenging for LiDAR). Chairs are pulled out at irregular angles, narrowing the navigation path to <60cm. Ambient lighting is dim/moody, testing low-light camera performance. Background features a blurred busy kitchen pass."

![Restaurant Dining](worlds/api_renders/restaurant_dining_service_thumbnail.jpg)

#### Hospital Corridor (Delivery)
> **Prompt**: "A sterile, bright hospital corridor. High-gloss vinyl flooring. Walls are white with color-coded wayfinding strips. Obstacles include a crash cart, a wheelchair folded against the wall, and an IV drip stand on wheels. Lighting is clinical fluorescent, 5000K temperature. Ceiling convex mirrors are visible at intersections. Designed for autonomous delivery robot verification."

![Hospital Corridor](worlds/api_renders/hospital_corridor_medic_thumbnail.jpg)

#### Supermarket Shelves (Inventory)
> **Prompt**: "A planogram-compliant supermarket aisle. Shelves are fully stocked with colorful cereal boxes, creating a high-frequency visual texture. Several items are intentionally missing (out-of-stock) to test gap detection. Price tags on the shelf edge are legible. The floor is white tile. Lighting is uniform to ensure color accuracy for product recognition."

![Supermarket](worlds/api_renders/retail_supermarket_shelves_thumbnail.jpg)

### 🚧 Outdoor & Unstructured

#### City Sidewalk (Delivery Rover)
> **Prompt**: "First-person view from a delivery rover on a city sidewalk. Paved concrete slabs with cracks and chewing gum stains. A fire hydrant (red) and a parking meter (gray) act as static obstacles. The curb drops off to a tarmac road. Sunlight casts hard shadows from a nearby tree, creating deceptive contrast patterns on the ground. Urban background."

![City Sidewalk](worlds/api_renders/city_sidewalk_delivery_thumbnail.jpg)

#### Construction Site (Quadruped Locomotion)
> **Prompt**: "An active chaotic construction site. Ground is uneven, covered in loose gravel and sand. Piles of red bricks and wooden pallets create traversability barriers. Exposed steel rebar acts as a snagging hazard. Lighting simulates an overcast day (diffuse light). Geometrical complexity is high for testing quadruped locomotion and footstep planning."

![Construction Site](worlds/api_renders/construction_site_inspection_thumbnail.jpg)

#### Disaster Zone (Search & Rescue)
> **Prompt**: "A simulated post-earthquake rubble pile. Broken slabs of concrete, twisted rebar, and shattered glass. The terrain is highly non-convex with deep crevices. Atmospheric dust/haze reduces visibility to 80%. Lighting is low-angle, simulating dusk, casting long shadows that obscure depth. Designed for Search and Rescue (SAR) robot mobility testing."

![Disaster Zone](worlds/api_renders/disaster_rubble_search_thumbnail.jpg)

#### Agricultural Field (Perception)
> **Prompt**: "A robotic agriculture perception dataset. Parallel rows of green corn crops, approximately 1.5m high. The inter-row path is dirt with random weeds. Sunlight is directly overhead (noon), creating high contrast between leaves and shadows. Variable crop health (brown leaves) is visible for disease detection tasks."

![Agricultural Field](worlds/api_renders/agricultural_field_crop_thumbnail.jpg)

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
