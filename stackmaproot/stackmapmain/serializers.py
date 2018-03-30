from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

    def create(self, validated_data):

        # Automatically assign a new group or put them in an existing group if there's space (The last group is the only group that should have space)

        last_group = Group.objects.latest('id')
        if last_group.user_set.count() < 3:
            validated_data['groups'] = [last_group.id]
        else:
            new_group = Group.objects.create(id=last_group.id + 1, name=last_group.id+1)      
            validated_data['groups'] = [new_group.id]

        validated_data['id'] = User.objects.latest('id').id + 1
        return User.objects.create(**validated_data)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

