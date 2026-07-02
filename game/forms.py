from django import forms

class JoinRoomForm(forms.Form):
    room_code = forms.CharField(max_length=6,label="Room Code")