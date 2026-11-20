{
    "name": "ikon Backend Look",
    "version": "19.0.1.0.0",
    "category": "Technical",
    "license": "LGPL-3",
    "author": "ikon",
    "summary": "Render the backend with the standard Odoo webclient layout",
    "description": """
ikon Backend Look
=================

The ikon team is trained on the standard (community) Odoo backend. This
module restores that layout -- the classic navbar with an apps dropdown
instead of the full-screen home menu -- while leaving every installed
Enterprise feature in place and fully functional.

It works by reversing a single asset operation. ``web_enterprise`` declares::

    web.assets_web: [
        (replace, web/static/src/main.js,
                    web_enterprise/static/src/main.js),
    ]

which boots ``WebClientEnterprise`` instead of ``WebClient``. This module
simply swaps that entry back. No Enterprise source file is patched and no
module is uninstalled, so uninstalling this module restores the Enterprise
layout exactly.

Scope: presentation only. This module does not alter, mask or filter the
server version, the edition, the subscription state, or anything reported
by About / version_info / session_info.
    """,
    "depends": ["web_enterprise"],
    "assets": {
        # --- palette -------------------------------------------------
        # Override, never remove. Other bundles anchor operations on the
        # enterprise variable files -- web.dark_mode_variables declares
        #   (before, web_enterprise/.../primary_variables.scss,
        #              web_enterprise/.../primary_variables.dark.scss)
        # -- so removing them makes web.assets_web_dark fail to resolve and
        # dark mode breaks. Placing our own file first wins on !default
        # ordering while every enterprise file stays in the bundle.
        "web._assets_primary_variables": [
            ("before",
             "web_enterprise/static/src/scss/primary_variables.scss",
             "ikon_backend_look/static/src/scss/community_palette.scss"),
        ],
        # --- login page ----------------------------------------------
        # The login page is the only backend-styled page an anonymous
        # visitor sees; these two drag in the enterprise look (including
        # the background-light.svg request).
        "web.assets_frontend": [
            ("remove", "web_enterprise/static/src/webclient/home_menu/home_menu_background.scss"),
            ("remove", "web_enterprise/static/src/webclient/navbar/navbar.scss"),
        ],
        # --- backend component styling -------------------------------
        # web_enterprise restyles the standard components on top of the
        # community rules (it is loaded after `web`). Dropping its scss
        # lets the community styling show through again -- most visibly
        # the solid brand-coloured main navbar.
        # Explicit paths, not globs: a glob that matches nothing in the
        # bundle makes the remove operation fail.
        # Only .scss is dropped; every enterprise js/xml asset stays, so
        # no component loses its behaviour.
        "web.assets_backend": [
            ("remove", "web_enterprise/static/src/webclient/navbar/navbar.scss"),
            ("remove", "web_enterprise/static/src/webclient/home_menu/home_menu.scss"),
            ("remove", "web_enterprise/static/src/webclient/home_menu/home_menu_background.scss"),
            ("remove", "web_enterprise/static/src/webclient/home_menu/expiration_panel.scss"),
            ("remove", "web_enterprise/static/src/core/notebook/notebook.scss"),
            ("remove", "web_enterprise/static/src/views/kanban/kanban_view.scss"),
            ("remove", "web_enterprise/static/src/views/list/list_controller.scss"),
        ],
        # --- webclient class -----------------------------------------
        "web.assets_web": [
            ("replace",
             "web_enterprise/static/src/main.js",
             "web/static/src/main.js"),
        ],
    },
    "installable": True,
    "auto_install": False,
    "application": False,
}
