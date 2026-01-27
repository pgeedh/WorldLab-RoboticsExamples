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

def generate_world_from_text(prompt, display_name, output_dir="worlds/api_renders"):
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
        "model": "Marble 0.1-mini"
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
        scenarios = [
            # --- Domestic & Residential ---
            {
                "name": "domestic_kitchen_robotics",
                "prompt": "**System Role:** Senior Simulation Engineer. **Objective:** Generate a high-fidelity digital twin of a 'Domestic Kitchen for Manipulation Training'. **1. Scene:** Modern kitchen, 1.2m robot-eye height. **2. Lighting:** Even, diffuse studio lighting (HDRI) to minimize shadows. **3. Key Objects:** Granite island surface (Friction coeff: 0.6) containing: Glossy Red Apple (Sub-surface scattering enabled), Matte Ceramic Mug (Handle orientation: 90 deg relative to camera), White Flat Plate. **4. Physics Constraints:** Objects must have realistic mass properties (Apple: 150g, Mug: 300g). **5. Visuals:** 8k texture resolution, no motion blur, clear segmentation boundaries."
            },
            {
                "name": "cluttered_bedroom_manipulation",
                "prompt": "**System Role:** Cloth Simulation Specialist. **Objective:** Generate a 'Complex Deformable Object' environment. **1. Scene:** Messy Bedroom. **2. Objects (Laundry):** Red T-Shirt (Cotton, 200gsm), Blue Jeans (Denim, stiff fabric), White Socks. **3. Layout:** Tangled pile state on an unmade bed (wrinkled linens). **4. Clutter:** Hardcover books and circular rigid plastic toys scattered on floor. **5. Lighting:** Soft morning light (Directional) to create volumetric shadows for geometric reasoning. **6. Complexity:** High-frequency textures for segmentation testing."
            },
            {
                "name": "messy_airbnb_living_room",
                "prompt": "**System Role:** Service Robotics Evaluator. **Objective:** Generate a 'Housekeeping Assessment' scene. **1. Scene:** Lived-in Living Room. **2. Semantic Classes:** 'Trash' (Crumpled Aluminum Soda Cans, Glossy Magazine wrappers) vs 'Personal Items' (Patterned Clothing, Electronics). **3. Layout:** Open suitcase on rug, items spilling out. **4. Visuals:** High dynamic range (HDR) to capture specular reflections on cans vs matte fabrics. Neutral color temperature (5000K)."
            },
            
            # --- Industrial & Logistics ---
            {
                "name": "industrial_warehouse_logistics",
                "prompt": "**System Role:** warehouse Automation Engineer. **Objective:** Generate a 'Path Planning & Localization' environment. **1. Scene:** Industrial Aisle (ISO standard width). **2. Floor:** Polished Concrete with High-Contrast Yellow Safety Tape. **3. Racking:** Metal shelving, populated with uniform Brown Cardboard Boxes (30x30x30cm). **4. Constraints:** Introduce alignment noise (±5 degrees) to boxes. **5. Markers:** AprilTags (Fiducials) visible on rack uprights. **6. Lighting:** Cool White LED strips (6000K), uniform illumination."
            },
            {
                "name": "electronic_assembly_line_pcb",
                "prompt": "**System Role:** Precision Manufacturing Engineer. **Objective:** Generate a 'Micro-Manipulation' workbench. **1. View:** Macro-photography close-up. **2. Subject:** Green PCB (FR4 material) clamped in fixture. **3. Components:** 0402 Resistors (Tray), Soldering Iron (Oxidized tip), Fine-point Tweezers. **4. Solder Joints:** Shiny silver texture (Lead-free). **5. Lighting:** Ring light macro setup to highlight metallic leads. Shallow depth of field (Bokeh background)."
            },
            {
                "name": "data_center_wire_maintenance",
                "prompt": "**System Role:** Senior Simulation Engineer specializing in Deformable Linear Objects (DLOs). **Objective:** Generate a high-fidelity 3D simulation environment for 'Data Center Cable Remediation'. **1. Scene:** Standard 42U Data Center Server Rack. Lighting: Dim, overhead with localized shadowing. Focus: Rack Unit 14 (RU14). Target: Switch Port 12 (empty/highlighted). **2. Object (Cable):** Standard CAT6 Ethernet Cable, Blue (#0000FF). Physics: Deformable Linear Object (DLO) with semi-rigid PVC stiffness (Young's Modulus ~0.05 GPa) to prevent self-intersections. Connector: RJ45 male with a fragile locking clip. **3. Task:** Rear cable management area, chaotic cabling."
            },
            {
                "name": "automotive_assembly_robotic_cell",
                "prompt": "**System Role:** Industrial Robotics Safety Officer. **Objective:** Generate a 'Heavy Industry Welding Cell'. **1. Central Asset:** Raw Steel Car Chassis (White Body). **2. Robots:** 2x KUKA-style Orange Industrial Arms. **3. Effects:** Frozen welding sparks (Particle system). **4. Environment:** Metal Grating floor, Yellow Safety Cages (Mesh texture). **5. Lighting:** High contrast, simulating welding arc brightness."
            },

            # --- Service & Commercial ---
            {
                "name": "hotel_reception_concierge",
                "prompt": "**System Role:** Social Navigation Architect. **Objective:** Generate a 'Human-Robot Interaction' lobby. **1. Surface:** Highly reflective Polished Marble (Ray-tracing enabled). **2. Key Asset:** Mahogany Concierge Desk. **3. Dynamic Agents:** 'Ghost' proxies of humans (Blurred) to indicate crowd density. **4. Obstacles:** Brass Luggage Carts. **5. Atmosphere:** Warm, inviting, architectural lighting (3000K). Wide-angle lens distortion correction."
            },
            {
                "name": "restaurant_dining_service",
                "prompt": "**System Role:** Dynamic Path Planner. **Objective:** Generate a 'Constrained Navigation' dining floor. **1. Density:** High. Round tables with white cloth. **2. LiDAR Challenge:** Transparent Wine Glasses and Silverware. **3. Geometry:** Chairs rotated randomly, narrowing path width to <60cm. **4. Lighting:** Dim/Moody/Candlelight to stress low-light sensors."
            },
            {
                "name": "hospital_corridor_medic",
                "prompt": "**System Role:** Healthcare Logistics Planner. **Objective:** Generate a 'Sterile Delivery Route'. **1. Scene:** Hospital Corridor. **2. Flooring:** High-gloss Vinyl (White/Blue tint). **3. Semantics:** Color-coded wall strips for Wayfinding. **4. Obstacles:** Red Crash Cart, Folded Wheelchair, IV Drip Stand (Thin geometry). **5. Lighting:** Clinical Fluorescent (Flicker-free). **6. Safety:** Convex mirrors at blind corners."
            },
            {
                "name": "retail_supermarket_shelves",
                "prompt": "**System Role:** Retail Inventory Analyst. **Objective:** Generate a 'Planogram Compliance' view. **1. Asset:** Supermarket Gondola Shelving. **2. Stock:** Colorful Cereal Boxes (Dense texture). **3. Task:** intentionally missing items (Out-of-Stock gaps). **4. Details:** Price tags readable on shelf edge. **5. Lighting:** Uniform, flat lighting for OCR/Barcode reading."
            },

            # --- Outdoor & Unstructured ---
            {
                "name": "city_sidewalk_delivery",
                "prompt": "**System Role:** Autonomous Driving Engineer (Last Mile). **Objective:** Generate a 'Urban Sidewalk' segment. **1. View:** Rover First-Person (0.5m height). **2. Material:** Concrete Pavement with cracks and gum stains. **3. Static Obstacles:** Red Fire Hydrant, Gray Parking Meter. **4. Hazards:** Curb drop-off to Tarmac road. **5. Lighting:** Harsh Sunlight (Noon) creating hard, deceptive shadows from tree branches."
            },
            {
                "name": "construction_site_inspection",
                "prompt": "**System Role:** Terrain Locomotion Specialist. **Objective:** Generate a 'Rough Terrain' inspection site. **1. Ground:** Loose Gravel and Sand (Non-rigid). **2. Obstacles:** Piles of Red Bricks, Wooden Pallets, Exposed Steel Rebar (Snag hazard). **3. Lighting:** Overcast/Diffuse (Flat contrast). **4. Requirement:** High geometric complexity for footstep planning."
            },
            {
                "name": "disaster_rubble_search",
                "prompt": "**System Role:** Search & Rescue Coordinator. **Objective:** Generate a 'Collapsed Structure' zone. **1. Terrain:** Broken Concrete Slabs, Twisted Rebar, Shattered Glass. **2. Topology:** Non-convex with deep crevices/voids. **3. Atmosphere:** Heavy Dust/Haze (Visibility <80%). **4. Lighting:** Low-angle Dusk sun, long shadows obscuring depth. **5. Task:** Volumetric void estimation."
            },
            {
                "name": "agricultural_field_crop",
                "prompt": "**System Role:** Precision Agriculture Specialist. **Objective:** Generate a 'Crop Monitoring' dataset. **1. Subject:** Green Corn Crops (Zea mays), 1.5m height. **2. Layout:** Parallel rows, dirt path inter-row. **3. Lighting:** Direct overhead sunlight (High contrast). **4. Variable:** Introduce random Brown Leaves (simulate disease) for anomaly detection."
            }
        ]

        print(f"🤖 Queuing {len(scenarios)} worlds for generation...")
        for s in scenarios:
            if s["name"] in existing_urls:
                print(f"⏭️  Skipping '{s['name']}' (Already generated).")
                continue
            
            generate_world_from_text(s["prompt"], s["name"])
            time.sleep(2) # Add small delay to respect rate limits
