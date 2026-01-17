# Dashboard Assets Manifest

## Overview
Repository containing graphic assets for Home Assistant floorplans, room renders, and infrastructure icons.

## Directory Structure & Previews

### 1. Levels & Overview
| Asset Name | Preview | Description |
| :--- | :--- | :--- |
| `level01.png` | <img src="level01.png" width="200"/> | Ground floor plan |
| `level02.png` | <img src="level02.png" width="200"/> | First floor plan |
| `attic.png` | <img src="attic.png" width="200"/> | Attic/Storage area |
| `home-01.png` | <img src="home-01.png" width="200"/> | Property overview |
| `home-garden.png` | <img src="home-garden.png" width="200"/> | Garden layout |
| `home-japan.png` | <img src="home-japan.png" width="200"/> | Japanese garden section |
| `townhouse.png` | <img src="townhouse.png" width="200"/> | External building view |

### 2. Living Spaces
| Asset Name | Preview | Description |
| :--- | :--- | :--- |
| `living-room-2.png` | <img src="living-room-2.png" width="200"/> | Main Living Room |
| `tv-lounge.png` | <img src="tv-lounge.png" width="200"/> | TV Lounge area |
| `tv-room.png` | <img src="tv-room.png" width="200"/> | Dedicated TV Room |
| `kitchen-1.png` | <img src="kitchen-1.png" width="200"/> | Kitchen view 1 |
| `kitchen-2.png` | <img src="kitchen-2.png" width="200"/> | Kitchen view 2 |
| `master-bedroom.png` | <img src="master-bedroom.png" width="200"/> | Master Bedroom |
| `bedroom.png` | <img src="bedroom.png" width="200"/> | Standard Bedroom |
| `guest-room.png` | <img src="guest-room.png" width="200"/> | Guest Room |
| `office-01.png` | <img src="office-01.png" width="200"/> | Office / Study 1 |
| `office-02.png` | <img src="office-02.png" width="200"/> | Office / Study 2 |
| `bathroom-ground.png` | <img src="bathroom-ground.png" width="200"/> | Ground Floor Bathroom |
| `bathroom-upper.png` | <img src="bathroom-upper.png" width="200"/> | Upper Bathroom |
| `bathroom-upstairs.png` | <img src="bathroom-upstairs.png" width="200"/> | Upstairs Bathroom |
| `wardrobe.png` | <img src="wardrobe.png" width="200"/> | Walk-in Wardrobe |

### 3. Circulation & Entry
| Asset Name | Preview | Description |
| :--- | :--- | :--- |
| `entrance.png` | <img src="entrance.png" width="200"/> | Main Entrance |
| `entryway.png` | <img src="entryway.png" width="200"/> | Entryway |
| `vestibule.png` | <img src="vestibule.png" width="200"/> | Windbreaker |
| `stairs.png` | <img src="stairs.png" width="200"/> | Main Stairs |
| `under-stairs.png` | <img src="under-stairs.png" width="200"/> | Storage under stairs |
| `garage-hallway.png` | <img src="garage-hallway.png" width="200"/> | Hallway to garage |

### 4. Technical Infrastructure
| Asset Name | Preview | Description |
| :--- | :--- | :--- |
| `servers.png` | <img src="servers.png" width="200"/> | Server Room overview |
| `server-cabinet.png` | <img src="server-cabinet.png" width="200"/> | Rack/Cabinet detail |
| `boiler-room.png` | <img src="boiler-room.png" width="200"/> | Heating system |
| `recuperator.png` | <img src="recuperator.png" width="200"/> | Ventilation unit |
| `hvac-01.png` | <img src="hvac-01.png" width="200"/> | HVAC system |
| `pv.png` | <img src="pv.png" width="200"/> | Photovoltaics |
| `system.png` | <img src="system.png" width="200"/> | System overview |
| `system02.png` | <img src="system02.png" width="200"/> | System detail |
| `3dprinter-prusa.png` | <img src="3dprinter-prusa.png" width="200"/> | 3D Printer |

### 5. Garage & Exterior
| Asset Name | Preview | Description |
| :--- | :--- | :--- |
| `garage-home.png` | <img src="garage-home.png" width="200"/> | Home Garage |
| `garage-01.png` | <img src="garage-01.png" width="200"/> | Garage 1 |
| `garage-zs.png` | <img src="garage-zs.png" width="200"/> | Garage Szczecin |
| `garden-shed-01.png` | <img src="garden-shed-01.png" width="200"/> | Garden Shed |
| `terrace.png` | <img src="terrace.png" width="200"/> | Terrace |
| `gate-01.png` | <img src="gate-01.png" width="200"/> | Main Gate |
| `gate-02.png` | <img src="gate-02.png" width="200"/> | Side Gate |
| `grill.png` | <img src="grill.png" width="200"/> | BBQ Area |
| `grill-02.png` | <img src="grill-02.png" width="200"/> | BBQ Detail |
| `kia.png` | <img src="kia.png" width="200"/> | Car |
| `waste.png` | <img src="waste.png" width="200"/> | Waste Management |
| `laundry.png` | <img src="laundry.png" width="200"/> | Utility Room |

## Asset Generation

### Fallout Style Prompt Template
To generate consistent room renders matching the project aesthetic, use the following parameterised prompt. Replace `{ROOM_NAME}` with the specific area (e.g., "Server Room", "Master Bedroom").

> A cinematic wide shot of a {ROOM_NAME} designed in a Fallout Vault style. Aesthetic: Retro-futuristic 1950s Atom-punk, post-apocalyptic shelter, gritty and industrial. Environment: Rusted metal bulkhead walls, exposed ventilation pipes, concrete floor with metal grating, heavy vault-tec architectural elements. Lighting: Dim atmospheric lighting with a dominant phosphor-green radioactive glow, flickering fluorescent tube lights, volumetric fog. Furniture & Props: Worn mid-century modern furniture, bulky analog computer terminals with vacuum tubes and green screens, analog pressure gauges, loose wires, scattered Nuka-Cola bottles. Texture quality: Unreal Engine 5 render, 8k resolution, hyper-realistic, detailed textures of rust and peeling paint, ray-tracing. --ar 16:9 --v 6.0

