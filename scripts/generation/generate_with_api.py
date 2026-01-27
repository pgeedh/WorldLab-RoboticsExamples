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
        
    print(f"✅ World '{world_data.get('display_name')}' generated successfully!")
    print(f"   View in Marble: {world_data.get('world_marble_url')}")

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
        # Enhanced scenarios with "Digital Twin" level detail for robotics training
        scenarios = [
            # --- Domestic & Residential ---
            {
                "name": "domestic_kitchen_robotics",
                "prompt": "A hyper-realistic, robot-centric digital twin of a modern domestic kitchen. Captured from a 1.2m height (robot eye level). Key interaction zones include a granite island with specific grasping targets: a glossy red apple, a matte ceramic mug with a handle facing right, and a white flat plate. Lighting is even, diffuse studio lighting to minimize harsh shadows. The floor is hardwood with clear traction texture. No motion blur. optimized for object detection and depth estimation."
            },
            {
                "name": "cluttered_bedroom_manipulation",
                "prompt": "A physically simulated messy bedroom for high-complexity manipulation training. A tangled pile of laundry (red t-shirt, blue jeans, white socks) rests on an unmade bed with wrinkled linens. The floor is scattered with hardcover books, circular plastic toys, and a charging cable. Textures are high-fidelity to test segmentation algorithms. Soft morning light entering from a window on the left, casting realistic shadows for volumetric reasoning."
            },
            {
                "name": "messy_airbnb_living_room",
                "prompt": "A 'lived-in' living room state for housekeeping robots. An open suitcase sits on a rug, spilling patterned clothing. A coffee table is cluttered with empty soda cans, a crumpled magazine, and a TV remote. Cushions are thrown haphazardly on the floor. The scene tests the robot's ability to distinguish between 'trash' (cans) and 'personal items' (clothing). Photorealistic, 8k resolution, neutral color temperature."
            },
            
            # --- Industrial & Logistics ---
            {
                "name": "industrial_warehouse_logistics",
                "prompt": "A precision-mapped industrial warehouse aisle. High-contrast yellow safety lines painted on polished concrete floors. Metal racking units on both sides are stocked with brown cardboard boxes of uniform size (30x30cm), some slightly misaligned to test grasping tolerance. Bright, cool-white overhead LED lighting strips to eliminate dark corners. Fiducial markers (QR codes) visible on shelf edges for localization."
            },
            {
                "name": "electronic_assembly_line_pcb",
                "prompt": "Macro-photography view of an electronics assembly workbench. A green PCB (Printed Circuit Board) is clamped in a holder. Solder flux residue is visible. Nearby components: a tray of tiny 0402 resistors, a soldering iron with a oxidized tip, and a pair of fine-point tweezers. The lighting is a focused ring light to highlight metallic leads and solder joints for defect detection algorithms. Depth of field is shallow, focused on the PCB."
            },
            {
                "name": "data_center_wire_maintenance",
                "prompt": "A narrow server aisle in a hyperscale data center. Densely packed server racks with blinking status LEDs (green/amber). The focus is on the rear cable management area: a chaotic mix of blue (CAT6) and orange (Fiber) cables. Some cables are unplugged and hanging loose. The environment is metallic, reflective, and cool-toned. Intricate geometry for occlusion testing. 4k resolution."
            },
            {
                "name": "automotive_assembly_robotic_cell",
                "prompt": "A heavy-industry automotive welding cell. A raw steel car chassis acts as the central workspace. Orange industrial robotic arms (KUKA-style) are positioned around it. Sparks from a spot welder are frozen in mid-air (simulated). The floor is metal grating. Warning signs and safety cages are clearly visible globally. High dynamic range lighting to handle the brightness of welding arcs."
            },

            # --- Service & Commercial ---
            {
                "name": "hotel_reception_concierge",
                "prompt": "A 5-star hotel lobby designed for social navigation. Polished marble floors reflecting the environment. A high concierge desk made of mahogany. The space is populated with 'ghost' proxies of people (blurred or static) to simulate crowd density without privacy issues. Luggage carts with brass railings are obstacles. Warm, inviting architectural lighting. Wide angle field of view."
            },
            {
                "name": "restaurant_dining_service",
                "prompt": "A dense restaurant dining floor layout. Round tables covered in white cloth, set with silverware and transparent wine glasses (challenging for LiDAR). Chairs are pulled out at irregular angles, narrowing the navigation path to <60cm. Ambient lighting is dim/moody, testing low-light camera performance. Background features a blurred busy kitchen pass."
            },
            {
                "name": "hospital_corridor_medic",
                "prompt": "A sterile, bright hospital corridor. High-gloss vinyl flooring. Walls are white with color-coded wayfinding strips. Obstacles include a crash cart, a wheelchair folded against the wall, and an IV drip stand on wheels. Lighting is clinical fluorescent, 5000K temperature. Ceiling convex mirrors are visible at intersections. Designed for autonomous delivery robot verification."
            },
            {
                "name": "retail_supermarket_shelves",
                "prompt": "A planogram-compliant supermarket aisle. Shelves are fully stocked with colorful cereal boxes, creating a high-frequency visual texture. Several items are intentionally missing (out-of-stock) to test gap detection. Price tags on the shelf edge are legible. The floor is white tile. Lighting is uniform to ensure color accuracy for product recognition."
            },

            # --- Outdoor & Unstructured ---
            {
                "name": "city_sidewalk_delivery",
                "prompt": "First-person view from a delivery rover on a city sidewalk. Paved concrete slabs with cracks and chewing gum stains. A fire hydrant (red) and a parking meter (gray) act as static obstacles. The curb drops off to a tarmac road. Sunlight casts hard shadows from a nearby tree, creating deceptive contrast patterns on the ground. Urban background."
            },
            {
                "name": "construction_site_inspection",
                "prompt": "An active chaotic construction site. Ground is uneven, covered in loose gravel and sand. Piles of red bricks and wooden pallets create traversability barriers. Exposed steel rebar acts as a snagging hazard. Lighting simulates an overcast day (diffuse light). Geometrical complexity is high for testing quadruped locomotion and footstep planning."
            },
            {
                "name": "disaster_rubble_search",
                "prompt": "A simulated post-earthquake rubble pile. Broken slabs of concrete, twisted rebar, and shattered glass. The terrain is highly non-convex with deep crevices. Atmospheric dust/haze reduces visibility to 80%. Lighting is low-angle, simulating dusk, casting long shadows that obscure depth. Designed for Search and Rescue (SAR) robot mobility testing."
            },
            {
                "name": "agricultural_field_crop",
                "prompt": "A robotic agriculture perception dataset. Parallel rows of green corn crops, approximately 1.5m high. The inter-row path is dirt with random weeds. Sunlight is directly overhead (noon), creating high contrast between leaves and shadows. Variable crop health (brown leaves) is visible for disease detection tasks."
            }
        ]

        print(f"🤖 Queuing {len(scenarios)} worlds for generation...")
        for s in scenarios:
            generate_world_from_text(s["prompt"], s["name"])
