from django import forms

class ItemsForm(forms.Form):
    item_name = forms.CharField(max_length=64,initial="NA")
    item_description = forms.CharField(max_length=120,initial="NA")
    item_category = forms.CharField(max_length=120,initial="Misc")
    item_price = forms.IntegerField()
    item_stock = forms.IntegerField()


def add_items(self):
    print(f"Adding the item: {self.cleaned_data['item_name']}")
