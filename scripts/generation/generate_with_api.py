import os
import requests
import time
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("WLT_API_KEY")
BASE_URL = "https://api.worldlabs.ai/marble/v1"

def check_api_key():
    if not API_KEY:
        print("❌ Error: WLT_API_KEY not found in environment variables.")
        return False
    return True

def generate_world_from_text(prompt, display_name, model_id="Marble 0.1-mini", output_dir="worlds/api_renders"):
    """
    Generates a world using the World Labs API from a text prompt.
    """
    generate_url = f"{BASE_URL}/worlds:generate"
    
    headers = {
        "WLT-Api-Key": API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "display_name": display_name,
        "world_prompt": {
            "type": "text",
            "text_prompt": prompt
        },
        "model": model_id,
        "permission": {
            "public": True
        }
    }
    
    print(f"🚀 Sending request for: '{display_name}'...")
    
    try:
        # 1. Initiate Generation
        response = requests.post(generate_url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        operation_id = data.get("operation_id")
        if not operation_id:
            print("❌ Start failed: No operation ID returned.")
            print(data)
            return

        print(f"⏳ Generation started (Op ID: {operation_id}). Polling for completion...")
        
        # 2. Poll for Completion
        op_url = f"{BASE_URL}/operations/{operation_id}"
        
        while True:
            status_res = requests.get(op_url, headers=headers)
            status_res.raise_for_status()
            op_data = status_res.json()
            
            if op_data.get("done"):
                if op_data.get("error"):
                    print(f"❌ Generation failed: {op_data['error']}")
                else:
                    world_response = op_data.get("response")
                    handle_success(world_response, output_dir, display_name)
                break
            
            # Print progress if available
            metadata = op_data.get("metadata", {})
            if metadata:
                progress = metadata.get("progress", {})
                # print(f"   Status: {progress.get('status')} - {progress.get('description')}")
            
            time.sleep(5) # Poll every 5 seconds
            
    except requests.exceptions.RequestException as e:
        print(f"❌ API Request Error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response Body: {e.response.text}")

def handle_success(world_data, output_dir, base_filename):
    """Downloads assets from the successful world generation."""
    if not world_data:
        print("❌ Error: No world data in response.")
        return

    os.makedirs(output_dir, exist_ok=True)
    
    assets = world_data.get("assets", {})
    
    # 1. Save Thumbnail
    thumb_url = assets.get("thumbnail_url")
    if thumb_url:
        download_file(thumb_url, os.path.join(output_dir, f"{base_filename}_thumbnail.jpg"))
        
    world_url = world_data.get('world_marble_url')
    print(f"✅ World '{world_data.get('display_name')}' generated successfully!")
    print(f"   View in Marble: {world_url}")
    
    # Save URL to file
    try:
        data = {}
        if os.path.exists("generated_urls.json"):
            with open("generated_urls.json", "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    pass
        
        data[base_filename] = world_url
        
        with open("generated_urls.json", "w") as f:
            json.dump(data, f, indent=2)
            
    except Exception as e:
        print(f"❌ Failed to save URL to file: {e}")

def download_file(url, filepath):
    try:
        r = requests.get(url)
        r.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(r.content)
        print(f"   Saved asset: {filepath}")
    except Exception as e:
        print(f"   Failed to download {filepath}: {e}")

if __name__ == "__main__":
    if check_api_key():
        # Load existing URLs to avoid regenerating
        existing_urls = {}
        if os.path.exists("generated_urls.json"):
            try:
                with open("generated_urls.json", "r") as f:
                    existing_urls = json.load(f)
            except:
                pass

        # Enhanced scenarios with "Senior Simulation Engineer" level detail for robotics training
        # Enhanced scenarios with "World Guide" narrative prompts for high-fidelity realism
        # "Corner Case" scenarios designed to break perception and control algorithms
        scenarios = [
            # --- Domestic & Residential ---
            {
                "name": "domestic_kitchen_robotics",
                "prompt": "**System Role:** Senior Perception Engineer. **Scene:** A neglected 1BHK kitchen in chaotic disarray. **Atmosphere:** Post-dinner catastrophe. **Details:** The laminate counter is slick with spilled oil (hazard for suction cups). A stack of white ceramic plates is precariously balanced, ready to topple. A clear glass bowl is virtually invisible against the wet sink. On the floor, a silver spoon lies hidden in a pattern of linoleum cracks—a geometric trap for wheel odometry. **Lighting:** Single flickering fluorescent bulb, creating strobing shadows."
            },
            {
                "name": "cluttered_bedroom_manipulation",
                "prompt": "**System Role:** Cloth Manipulation Specialist. **Scene:** A severe 'hoarder-lite' bedroom scenario. **Atmosphere:** Overwhelming textural density. **Details:** The bed is buried under a mountain of inter-tangled fabrics: stiff denim jeans knotted around sheer silk scarves (high friction variance). The hardwood floor is covered in a minefield of small, rigid LEGO bricks and slippery glossy magazine pages. **Lighting:** Harsh dawn sunlight beaming directly into the sensor, causing lens flare and blindness."
            },
            {
                "name": "messy_airbnb_living_room",
                "prompt": "**System Role:** Service Logic Architect. **Scene:** A party aftermath in a rental. **Atmosphere:** Semantic nightmare. **Details:** The visual clutter is deceptive: a 'valuable' open laptop is nearly indistinguishable from 'trash' pizza boxes due to similar matte black textures. A patterned Persian rug hides small dropped items like keys and coins (camouflaged objects). **Lighting:** Mixed color temperature—warm tungsten lamps vs. cool daylight window, confusing white balance."
            },
            
            # --- Industrial & Logistics ---
            {
                "name": "industrial_warehouse_logistics",
                "prompt": "**System Role:** Safety Systems Validator. **Scene:** A dilapidated, high-traffic logistics hub. **Atmosphere:** Hazardous and degraded. **Details:** The concrete floor is not just scuffed but pitted with potholes (1cm deep) that destabilize caster wheels. A puddle of hydraulic fluid creates a zero-friction zone. The cardboard boxes on shelves are crushed, torn, and have peeling barcodes that are essentially unreadable. **Lighting:** High-bay lights with significant glare on the wet floor spots."
            },
            {
                "name": "electronic_assembly_line_pcb",
                "prompt": "**System Role:** Micro-Precision QC. **Scene:** A defective electronics rework station. **Atmosphere:** High-stress precision failure. **Details:** The green PCB is covered in flux residue (sticky). The 0402 resistors are spilled and lying upside down (black side up, white text hidden). The soldering iron tip is severely oxidized and black. A rogue wire clipping bridges two critical pads—a short circuit hazard waiting to be detected. **Lighting:** Intense specular reflection from the solder mask, blinding standard RGB cameras."
            },
            {
                "name": "data_center_wire_maintenance",
                "prompt": "**System Role:** DLO Simulation Lead. **Scene:** A 'Spaghetti Cable' disaster zone in a server rack. **Atmosphere:** Maintenance impossibility. **Details:** Hundreds of CAT6 cables are effectively knotted into a rigid, impenetrable mass blocking airflow. The target cable (Blue) is woven *behind* three other taut cables (Red, Yellow, Black), requiring non-linear extraction logic. The connector tab is broken off. **Lighting:** Pitch blackness, illuminated only by blinking green status LEDs (dynamic noise)."
            },
            {
                "name": "automotive_assembly_robotic_cell",
                "prompt": "**System Role:** Industrial Safety Officer. **Scene:** An active welding cell mid-malfunction. **Atmosphere:** Dangerous and chaotic. **Details:** The car chassis is misaligned by 5 degrees on the jig. Splatter from previous welds covers the optical sensors. A hydraulic hose has burst, spraying dark fluid across the yellow safety cage. The robotic arms are frozen in a near-collision state. **Lighting:** Stroboscopic welding arcs occurring at 20Hz, creating rolling shutter artifacts on cameras."
            },

            # --- Service & Commercial ---
            {
                "name": "hotel_reception_concierge",
                "prompt": "**System Role:** Social Interaction Designer. **Scene:** A grand hotel lobby during a crisis evacuation drill. **Atmosphere:** Kinetic and confusing. **Details:** The highly reflective marble floor creates perfect 'phantom' obstacles via reflection. Luggage carts are overturned. 'Ghost' pedestrians are moving erratically and fast (1.5m/s), violating all social force models. **Lighting:** Emergency strobe lights activated, washing out color consistency."
            },
            {
                "name": "restaurant_dining_service",
                "prompt": "**System Role:** Navigation Planner. **Scene:** A claustrophobic fine-dining layout. **Atmosphere:** Worst-case traversability. **Details:** The gap between chairs is exactly 45cm (robot width: 50cm). Tablecloths hang low, obscuring chair legs (hidden obstacles). Tables are covered in purely transparent crystal glasses and mirrors—an absolute nightmare for LiDAR and Depth sensors. **Lighting:** Candlelight only (0.5 lux), pushing ISO capabilities to the limit."
            },
            {
                "name": "hospital_corridor_medic",
                "prompt": "**System Role:** Emergency Logistics Planner. **Scene:** A hospital corridor during a 'Code Blue'. **Atmosphere:** Maximum urgency and obstruction. **Details:** The floor is strewn with discarded medical gloves and saline puddles (slip hazards). A gurney has been left diagonally across the path, blocking 80% of the width. Hanging IV lines dangle at head-height, invisible to ground LiDAR. **Lighting:** harsh, sterile white, but with significant glare on the wet floor."
            },
            {
                "name": "retail_supermarket_shelves",
                "prompt": "**System Role:** Inventory Audit Specialist. **Scene:** A grocery aisle after an earthquake simulation. **Atmosphere:** Structural entropy. **Details:** Glass jars of pasta sauce have fallen and shattered—red liquid and broken glass cover the floor. Cereal boxes are crushed. The shelves themselves are warped and leaning. Price tags are ripped or fallen. **Lighting:** Flickering overhead tube, simulating a failing ballast."
            },

            # --- Outdoor & Unstructured ---
            {
                "name": "city_sidewalk_delivery",
                "prompt": "**System Role:** Urban Autonomy Lead. **Scene:** A city sidewalk during a heavy rainstorm aftermath. **Atmosphere:** Wet, reflective, and deceptive. **Details:** Large puddles reflect the sky, appearing as 'holes' to stereo cameras. Wet leaves cover the path, hiding the curb edge. A scooter is parked horizontally across the path. Manhole covers are slick metal. **Lighting:** Overcast, but with high-glare reflections from wet surfaces."
            },
            {
                "name": "construction_site_inspection",
                "prompt": "**System Role:** Quadruped Locomotion Expert. **Scene:** A 'Torture Test' construction ground. **Atmosphere:** Mechanically hostile. **Details:** Deep sticky clay mud (sinkage >5cm). Hidden loose rebar spikes buried just below the sand surface (impaling hazard). Unstable stacks of bricks that will collapse if touched. Sharp metal scrap everywhere. **Lighting:** Blind blinding sun glare off a sheet of galvanized steel."
            },
            {
                "name": "disaster_rubble_search",
                "prompt": "**System Role:** USAR Robotics Lead. **Scene:** A text book 'pancake collapse' reinforced concrete structure. **Atmosphere:** Claustrophobic and toxic. **Details:** Narrow void spaces (<40cm) lined with sharp, rusted rebar mesh. Pulverized drywall dust hangs in the air, scattering all active depth sensors (LiDAR bloom). **Lighting:** Total darkness, requiring the robot's onboard floodlight which reflects off the dust."
            },
            {
                "name": "agricultural_field_crop",
                "prompt": "**System Role:** Ag-Bot Perception Lead. **Scene:** A cornfield devastated by wind damage (lodging). **Atmosphere:** Tangled biological chaos. **Details:** The corn stalks are not upright; they are bent at 45-degree angles, creating an impenetrable web. Weeds match the crop color perfectly (Green-on-Green segmentation challenge). **Lighting:** Dappled sunlight through the canopy, creating high-frequency shadow noise."
            }
        ]

        print(f"🤖 Queuing {len(scenarios)} worlds for generation...")
        for s in scenarios:
            if s["name"] in existing_urls:
                print(f"⏭️  Skipping '{s['name']}' (Already generated).")
                continue
            
            generate_world_from_text(s["prompt"], s["name"], s.get("model", "Marble 0.1-mini"))
            time.sleep(2) # Add small delay to respect rate limits
