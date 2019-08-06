# -*- coding: utf-8 -*
from __future__ import print_function
import idaapi
import os

# IDA/
# └── plugins/
#     ├── diaphora_loader.py
#     └── diaphora/
#         └── diaphora.py

class diaphoraPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = 'diaphora - powerful bindiff for IDA pro'
    help = 'diaphora Plugin'
    wanted_name = 'diaphora'
    wanted_hotkey = ''
    dialog = None

    def init(self):
        action = idaapi.action_desc_t(
            'diaphora:proxy',             # The action name. This acts like an ID and must be unique
            'Run diaphora',               # The action text.
            runHandler(),                 # The action handler.
            None,                         # Optional: the action shortcut
            'Run diaphora'                # Optional: the action tooltip (available in menus/toolbar)
        )
        idaapi.register_action(action)
        idaapi.attach_action_to_menu(
            'File',                       # The relative path of where to add the action
            'diaphora:proxy',             # The action ID
            idaapi.SETMENU_APP)
        print("Diaphora :: Plugin loaded")
        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        diaphora = runHandler()
        diaphora.activate(self)

    def term(self):
        pass

class runHandler(idaapi.action_handler_t):
    def __init__(self):
        idaapi.action_handler_t.__init__(self)

    def activate(self, ctx):
        g = globals()
        script = os.path.join(idaapi.idadir("plugins"), "diaphora", "diaphora.py")
        idaapi.IDAPython_ExecScript(script, g)

    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS

def PLUGIN_ENTRY():
    return diaphoraPlugin()
