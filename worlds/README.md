# 🌍 World Labs Robotics Dataset

This directory contains the "Digital Twin" environments generated via the World Labs API.
These images represent 3D-consistent worlds used for:
- **Navigation Training** (Obstacle avoidance, Path planning)
- **Manipulation Tasks** (Object detection, Grasping)
- **Scene Understanding** (Segmentation, Semantics)

## 📂 File Structure
All generated assets are stored in `api_renders/`.
The naming convention is:
- `{scenario_name}_thumbnail.jpg`: Preview of the world.
- `{scenario_name}_pano.jpg`: 360° panoramic view (if available).

## 🏷️ Scenario Classification

### Domestic
- `domestic_kitchen_robotics`
- `cluttered_bedroom_manipulation`
- `messy_airbnb_living_room`

### Industrial
- `industrial_warehouse_logistics`
- `electronic_assembly_line_pcb`
- `data_center_wire_maintenance`
- `automotive_assembly_robotic_cell`

### Commercial
- `hotel_reception_concierge`
- `restaurant_dining_service`
- `hospital_corridor_medic`
- `retail_supermarket_shelves`

### Outdoor
- `city_sidewalk_delivery`
- `construction_site_inspection`
- `disaster_rubble_search`
- `agricultural_field_crop`

## 🛠️ Usage
To regenerate or extend this dataset, run:
```bash
python3 ../scripts/generation/generate_with_api.py
```
