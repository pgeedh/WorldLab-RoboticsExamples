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
        # Enhanced scenarios list for broad robotics applications
        scenarios = [
            # --- Domestic & Residential ---
            {
                "name": "domestic_kitchen_robotics",
                "prompt": "A modern domestic kitchen tailored for robotics training. Clear counters with scattered everyday objects like apples, mugs, and plates. Good lighting, photorealistic, no motion blur. From a robot's eye view level."
            },
            {
                "name": "cluttered_bedroom_manipulation",
                "prompt": "A messy bedroom scene for household robot training. Clothes on the bed, books on the floor, and toys scattered. Realistic lighting and varied textures for object recognition tasks."
            },
            {
                "name": "messy_airbnb_living_room",
                "prompt": "A lived-in Airbnb living room, slightly disorganized with luggage open, magazines on coffee table, and pillows on the floor. Simulation for housekeeping robots."
            },
            
            # --- Industrial & Logistics ---
            {
                "name": "industrial_warehouse_logistics",
                "prompt": "A clean industrial warehouse aisle with clearly marked paths. Shelves stocked with uniform boxes. Concrete floor. Bright overhead lighting. Suitable for autonomous mobile robot navigation testing."
            },
            {
                "name": "electronic_assembly_line_pcb",
                "prompt": "Close-up view of an electronics assembly station. Green PCB boards, soldering irons, small components like capacitors and resistors trays. High detail for fine manipulation tasks."
            },
            {
                "name": "data_center_wire_maintenance",
                "prompt": "Server room aisle in a data center. Racks of servers with complex cable management, some loose ethernet cables, ethernet ports exposed. Cool lighting, metallic surfaces."
            },
            {
                "name": "automotive_assembly_robotic_cell",
                "prompt": "Automotive manufacturing cell with partially assembled car chassis. Welding robot arms visible, heavy machinery, safety cages. Industrial factory setting."
            },

            # --- Service & Commercial ---
            {
                "name": "hotel_reception_concierge",
                "prompt": "Luxury hotel reception area. Marble floors, reception desk with computer monitors, luggage trolley nearby. Open space for social navigation robots."
            },
            {
                "name": "restaurant_dining_service",
                "prompt": "Busy restaurant dining room layout. Tables with white tablecloths, chairs, cutlery, glasses. Narrow paths between tables for waiter robot navigation. Warm lighting."
            },
            {
                "name": "hospital_corridor_medic",
                "prompt": "Sterile hospital corridor. Vinyl flooring, crash carts, wheelchairs parked on sides. Fluorescent lighting. Clear signage. Environment for delivery and assistant robots."
            },
            {
                "name": "retail_supermarket_shelves",
                "prompt": "Supermarket aisle stocked with colorful grocery products. Cans, boxes, bottles. Shelf scanning and stocking robot perspective. Bright uniform lighting."
            },

            # --- Outdoor & Unstructured ---
            {
                "name": "city_sidewalk_delivery",
                "prompt": "A city sidewalk view for delivery robot training. Paved ground, street lamps, building facades, fire hydrants. Empty enough for navigation but realistic urban textures. Day time."
            },
            {
                "name": "construction_site_inspection",
                "prompt": "Active construction site with raw materials, wooden pallets, gravel ground, exposed beams. Rough terrain for quadruped robot inspection."
            },
            {
                "name": "disaster_rubble_search",
                "prompt": "Simulated disaster zone with varying piles of concrete rubble, broken wood, and debris. Low light/dusk setting. For search and rescue robot mobility testing."
            },
            {
                "name": "agricultural_field_crop",
                "prompt": "Rows of crops in a farm field. Corn or leafy green plants. Dirt path between rows. Sunlight. For agricultural monitoring and harvesting robots."
            }
        ]

        print(f"🤖 Queuing {len(scenarios)} worlds for generation...")
        for s in scenarios:
            generate_world_from_text(s["prompt"], s["name"])
