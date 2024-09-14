from django import forms

OPCOES_CIDADES = (
    ('santos', 'Santos'),
    ('praia grande', 'Praia Grande'),
    ('sao vicente', 'Sao Vicente')
)

class CidadesForms(forms.Form):
    cidade = forms.ChoiceField(
        choices=OPCOES_CIDADES,
        widget=forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'})
    )