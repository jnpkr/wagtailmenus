from __future__ import absolute_import, unicode_literals

from django.conf import settings

ACTIVE_CLASS = getattr(
    settings, 'WAGTAILMENUS_ACTIVE_CLASS', 'active')

ACTIVE_ANCESTOR_CLASS = getattr(
    settings, 'WAGTAILMENUS_ACTIVE_ANCESTOR_CLASS', 'ancestor')

MAINMENU_MENU_ICON = getattr(
    settings, 'WAGTAILMENUS_MAINMENU_MENU_ICON', 'list-ol')

FLATMENU_MENU_ICON = getattr(
    settings, 'WAGTAILMENUS_FLATMENU_MENU_ICON', 'list-ol')

SECTION_ROOT_DEPTH = getattr(
    settings, 'WAGTAILMENUS_SECTION_ROOT_DEPTH', 3)

GUESS_TREE_POSITION_FROM_PATH = getattr(
    settings, 'WAGTAILMENUS_GUESS_TREE_POSITION_FROM_PATH', True)

DEFAULT_MAIN_MENU_TEMPLATE = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_MAIN_MENU_TEMPLATE',
    'menus/main_menu.html')

DEFAULT_FLAT_MENU_TEMPLATE = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_FLAT_MENU_TEMPLATE',
    'menus/flat_menu.html')

DEFAULT_SECTION_MENU_TEMPLATE = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_SECTION_MENU_TEMPLATE',
    'menus/section_menu.html')

DEFAULT_CHILDREN_MENU_TEMPLATE = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_CHILDREN_MENU_TEMPLATE',
    'menus/children_menu.html')

DEFAULT_SUB_MENU_TEMPLATE = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_SUB_MENU_TEMPLATE',
    'menus/sub_menu.html')

DEFAULT_MAIN_MENU_MAX_LEVELS = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_MAIN_MENU_MAX_LEVELS', 2
)

DEFAULT_SECTION_MENU_MAX_LEVELS = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_SECTION_MENU_MAX_LEVELS', 2
)

DEFAULT_CHILDREN_MENU_MAX_LEVELS = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_CHILDREN_MENU_MAX_LEVELS', 1
)

DEFAULT_FLAT_MENU_MAX_LEVELS = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_FLAT_MENU_MAX_LEVELS', 2
)

DEFAULT_MAIN_MENU_USE_SPECIFIC = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_MAIN_MENU_USE_SPECIFIC', False
)

DEFAULT_SECTION_MENU_USE_SPECIFIC = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_SECTION_MENU_USE_SPECIFIC', False
)

DEFAULT_CHILDREN_MENU_USE_SPECIFIC = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_CHILDREN_MENU_USE_SPECIFIC', False
)

DEFAULT_FLAT_MENU_USE_SPECIFIC = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_FLAT_MENU_USE_SPECIFIC', False
)

FLAT_MENUS_FALL_BACK_TO_DEFAULT_SITE_MENUS = getattr(
    settings, 'WAGTAILMENUS_FLAT_MENUS_FALL_BACK_TO_DEFAULT_SITE_MENUS', False
)

FLAT_MENUS_HANDLE_CHOICES = getattr(
    settings, 'WAGTAILMENUS_FLAT_MENUS_HANDLE_CHOICES', None)
