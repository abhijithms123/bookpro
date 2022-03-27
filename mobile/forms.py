from django import forms

class MobileForm(forms.Form):
    Brand = forms.CharField()
    Model = forms.CharField()
    price = forms.FloatField()
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        if price < 0:
            msg = "enter a valid price"
            self.add_error("price", msg)

