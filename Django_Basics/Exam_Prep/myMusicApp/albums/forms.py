from django import forms

from albums.models import Album
from myMusicApp.mixins import PlaceholderMixin, ReadOnlyMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)


class AlbumCreateForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    read_only_fields = ['album_name', 'artist', 'genre', 'price', 'description']

