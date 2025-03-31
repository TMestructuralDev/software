from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.list import MDListItemTrailingIcon
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RotateBehavior



class ExpansionPanelItem(MDExpansionPanel):
    pass

class TrailingPressedIconButton(ButtonBehavior, RotateBehavior, MDListItemTrailingIcon):

    def tap_expansion_chevron(self, panel: ExpansionPanelItem, chevron: MDListItemTrailingIcon):
            if not panel.is_open:
                panel.open()
                panel.set_chevron_down(chevron)
            else:
                panel.close()
                panel.set_chevron_up(chevron)