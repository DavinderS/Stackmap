from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from stackmapmain.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    def destroy(self, request, *args, **kwargs):
        # Delete the group and put the leftover users in another group to even things back out
        user_id = kwargs['pk']
        print(user_id)
        deleted_user = User.objects.get(id=user_id)
        print(deleted_user.groups.all()[0].user_set)
        for user in deleted_user.groups.all()[0].user_set.all():
        	print(user)



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Just using this to refresh the tables. Won't need this in production version
class ResetViewSet():
	Group.objects.all().delete()

	user_set = User.objects.all()
	group_index = 0
	group = None

	for user_index, user in enumerate(user_set):
		if user_index % 3 == 0:
			group = Group.objects.create(**{'id': group_index, 'name': group_index})
			group_index = group_index + 1
		group.user_set.add(user)


	queryset = Group.objects.all()

class RearrangeViewSet():
	group_set = Group.objects.all()
	last_group = Group.objects.latest('id')
	total_groups = group_set.count()

	print('total_groups')
	print(total_groups)
	for group in group_set:
		for user in group.user_set.all():
			print(user)

	queryset = group_set


