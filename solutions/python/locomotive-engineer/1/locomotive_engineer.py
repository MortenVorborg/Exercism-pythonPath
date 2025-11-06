"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*ids):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *id_list,  = ids

    return id_list


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a,b,*rest = each_wagons_id

    *new_list, = *rest,a,b
    
    a, *rest = new_list

    *new_list, = a,*missing_wagons,*rest

    return new_list


def add_missing_stops(current_stops, **additional_stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    *current_stops["stops"], = *additional_stops.values(),
    return current_stops


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    commbined_dict = {**route, **more_route_information}
    print((commbined_dict))
    return commbined_dict


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    [*first], [*second], [*third] = zip(*wagons_rows)
    return [first, second, third]

    
