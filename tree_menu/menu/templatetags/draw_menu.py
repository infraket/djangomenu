from django import template

from ..models import Item


register = template.Library()


@register.inclusion_tag('menu/menu_tree.html', takes_context=True)
def draw_menu(context, menu: str) -> dict[str]:
    """
    :param context: Данные запроса.
    :param menu: Имя (название) меню для отрисовки.
    :return: Словарь с данными для отрисовки меню.
    """
    try:

        items = Item.objects.filter(menu__title=menu)
        items_values = items.values()
        primary_item = [item for item in items_values.filter(parent=None)]
        selected_item_id = int(context['request'].GET[menu])
        selected_item = items.get(id=selected_item_id)
        selected_item_id_list = get_selected_item_id_list(selected_item,
                                                          primary_item,
                                                          selected_item_id)

        for item in primary_item:
            if item['id'] in selected_item_id_list:
                item['child_items'] = get_child_items(items_values, item['id'],
                                                      selected_item_id_list)
        result_dict = {'items': primary_item}

    except:
        result_dict = {
            'items': [
                item for item in Item.objects.filter(menu__title=menu,
                                                     parent=None).values()
                ]
            }

    result_dict['menu'] = menu
    result_dict['other_args'] = get_other_arg(context, menu)

    return result_dict


def get_other_arg(context, menu: str) -> str:
    """
    :param context: данные запроса.
    :param menu: Имя (название) меню для отрисовки.
    :return: Возвращает строку, содержащую аргументы(если есть) в запросе,
             кроме названия меню.
    """
    querystring_args = []
    for key in context['request'].GET:
        if key != menu:
            querystring_args.append(key + '=' + context['request'].GET[key])
    querystring = '&'.join(querystring_args)
    return querystring


def get_child_items(items_values: dict, current_item_id: int,
                    selected_item_id_list: list) -> list[Item]:
    """
    :param items_values: Список из словарей с данными по меню.
    :param current_item_id: Выбранный элемент в меню.
    :param selected_item_id_list: Список элементов от корня до выделенного.
    :return: Возвращает список экземпляров Item.
    """
    item_list = [item for item in items_values.filter(parent_id=current_item_id)]
    for item in item_list:
        if item['id'] in selected_item_id_list:
            item['child_items'] = get_child_items(items_values, item['id'],
                                                  selected_item_id_list)
    return item_list


def get_selected_item_id_list(parent: Item, primary_item: list[Item],
                              selected_item_id: int) -> list:
    """
    :param parent: Экземпляр таблицы Item.
    :param primary_item: Элементы без родителей.
    :param selected_item_id: id выделенного элемента.
    :return: Возвращает список элементов от корня до выделенного.
    """
    selected_item_id_list = []

    while parent:
        selected_item_id_list.append(parent.id)
        parent = parent.parent
    if not selected_item_id_list:
        for item in primary_item:
            if item['id'] == selected_item_id:
                selected_item_id_list.append(selected_item_id)
    return selected_item_id_list
