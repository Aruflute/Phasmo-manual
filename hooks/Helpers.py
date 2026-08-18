from typing import Optional, Any
from BaseClasses import MultiWorld



def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None
    
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Items import item_name_groups
    from ..Helpers import get_option_value

    # maps
    if category_name == "Tanglewood":
        return get_option_value(multiworld, player, "enable_tanglewood") == 1
    if category_name == "Edgefield":
        return get_option_value(multiworld, player, "enable_edgefield") == 1
    if category_name == "Ridgeview":
        return get_option_value(multiworld, player, "enable_ridgeview") == 1
    if category_name == "Diner":
        return get_option_value(multiworld, player, "enable_nell_diner") == 1
    if category_name == "Grafton":
        return get_option_value(multiworld, player, "enable_grafton") == 1
    if category_name == "Willow street":
        return get_option_value(multiworld, player, "enable_willow") == 1
    if category_name == "Woodwind":
        return get_option_value(multiworld, player, "enable_woodwind") == 1
    if category_name == "Point hope":
        return get_option_value(multiworld, player, "enable_point_hope") == 1
    if category_name == "Bleasdale":
        return get_option_value(multiworld, player, "enable_bleasdale") == 1
    if category_name == "Meadows restricted":
        return get_option_value(multiworld, player, "enable_restricted_meadows") == 1
    if category_name == "Meadows":
        return get_option_value(multiworld, player, "enable_meadows") == 1
    if category_name == "Prison":
        return get_option_value(multiworld, player, "enable_prison") == 1
    if category_name == "Maple lodge":
        return get_option_value(multiworld, player, "enable_maple_lodge") == 1
    if category_name == "High school":
        return get_option_value(multiworld, player, "enable_high_school") == 1

    # objective sanity
    if category_name == "Objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "PhotoObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "photo_objective")
        else:
            return False
    if category_name == "VideoObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "video_objective")
        else:
            return False
    if category_name == "SoundRecObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "recording_objective")
        else:
            return False
    if category_name == "SensorObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "sensor_objective")
        else:
            return False
    if category_name == "CrucifixObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "crucifix_objective")
        else:
            return False
    if category_name == "WitnessObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "ghost_event_objective")
        else:
            return False
    if category_name == "CleanseObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "cleanse_objective")
        else:
            return False
    if category_name == "RepelObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "repel_objective")
        else:
            return False
    if category_name == "FirelightObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "firelight_objective")
        else:
            return False
    if category_name == "EscapeObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "escape_objective")
        else:
            return False
    if category_name == "ParamicObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "parabolic_objective")
        else:
            return False
    if category_name == "SanityObj":
        if get_option_value(multiworld, player, "objective_sanity") == 1:
            return get_option_value(multiworld, player, "sanity_objective")
        else:
            return False

    # cursed posessions sanity
    if category_name == "Cursed posessions":
        if get_option_value(multiworld, player, "posession_sanity") == 1:
            return False
        else:
            return True
            
    # obj sanities
    if category_name == "High school objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Maple lodge objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Prison objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Meadows objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Meadows restricted objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Bleasdale objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Point hope objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Woodwind objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Willow objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Grafton objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Nell objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Ridgeview objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Edgefield objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1
    if category_name == "Tanglewood objectives":
        return get_option_value(multiworld, player, "objective_sanity") == 1

    # posess sanity
    if category_name == "High school posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Maple lodge posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Prison posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Meadows posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Meadows restricted posession":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Bleasdale posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Point hope posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Woodwind posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Willow posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Grafton posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Nell posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Ridgeview posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Edgefield posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1
    if category_name == "Tanglewood posessions":
        return get_option_value(multiworld, player, "posession_sanity") == 1

    # itmes
    if category_name == "LV1":
        return get_option_value(multiworld, player, "enable_lv1_items") == 1
    if category_name == "LV2":
        return get_option_value(multiworld, player, "enable_lv2_items") == 1
    if category_name == "LV3":
        return get_option_value(multiworld, player, "enable_lv3_items") == 1
        
    # yee
    if category_name == "Gambler":
        return get_option_value(multiworld, player, "gambler")
    if category_name == "100":
        return get_option_value(multiworld, player, "hundred_percent")
        
    # Apoc
    if category_name == "Apocalypse":
        return get_option_value(multiworld, player, "enable_apocalypse") == 1
    if category_name == "Apoc I":
        return get_option_value(multiworld, player, "apoc_bronze") == 1
    if category_name == "Apoc II":
        return get_option_value(multiworld, player, "apoc_silver") == 1
    if category_name == "Apoc III":
        return get_option_value(multiworld, player, "apoc_gold") == 1
    return None

def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    from ..Helpers import get_option_value

    if location.get("victory", False):
        return True

    selected_goal = get_option_value(multiworld, player, "goal")
    categories = location.get("category", [])
    goal_number = selected_goal

    if "Apoc III" in categories and goal_number == 3:
        return False
    if "Apoc II" in categories and goal_number == 1:
        return False
    return None

def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
